from django.shortcuts import render
from studentapp.models import Student,Course,Mark,Checkpoint
from studentapp.forms import SearchForm,StudentForm
from django.db.models import Max
from django.views.generic import DetailView,ListView
from django.http import JsonResponse

from rest_framework import viewsets
from django_filters.rest_framework  import FilterSet,DjangoFilterBackend
from django_filters import rest_framework as filters
from studentapp.serializers import CourseSerializer,CheckpointSerializer
# Create your views here.
def index(request):
    if request.GET:
        form = SearchForm(request.GET)
    else:
        form = SearchForm()

    form_student = StudentForm()
    context = {'form':form}
    context['from_student'] = {'form_student':form_student}
    if form.is_valid():
        search = form.cleaned_data['search']
        context['student_list'] = Student.objects.filter(name__icontains=search)
    else:
        context['error'] = form.errors
        context['student_list'] = Student.objects.all()

    return render(request,'index.back',context)
def index_vue(request):
    return render(request,'index.html')



def student_json(request):
    if request.GET:
        form = SearchForm(request.GET)
    else:
        form = SearchForm()

    form_student = StudentForm()
    offset = 0
    if form.is_valid():
        search = form.cleaned_data['search']
        queryset = Student.objects.filter(name__icontains=search)
        offset = form.cleaned_data['offset']

        if offset:
            offset = int(offset)
        else:
            offset= 0
    else:
        queryset = Student.objects.all()
    student_list = list(queryset.values('id','name'))
    return JsonResponse(student_list,safe=False)

def course_json(request):
    if request.GET:
        form = SearchForm(request.GET)
    else:
        form = SearchForm()

    form_student = StudentForm()
    offset = 0
    if form.is_valid():
        search = form.cleaned_data['search']
        queryset = Course.objects.filter(name__icontains=search)
        offset = form.cleaned_data['offset']

        if offset:
            offset = int(offset)
        else:
            offset= 0
    else:
        queryset = Course.objects.all()
    student_list = list(queryset.values('id','name'))
    return JsonResponse(student_list,safe=False)







class CourseList(ListView):
    model = Course
    paginate_by = 10

class CourseDetail(DetailView):
    model = Course

    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        course = self.get_object()
        student_list = course.student_set.all()
        checkpoint_list = course.checkpoint_set.all()
        table = []
        for student in student_list:
            mark_data = []
            for checkpoint in checkpoint_list:
                mark = student.mark_set.filter(checkpoint=checkpoint)
                if mark.exists():
                    score = mark.first()
                else:
                    score = Mark(checkpoint=checkpoint,student=student)
                mark_data.append(score)
            table.append({'name':student.name,
                          'id':student.id,
                          'mark_data':mark_data})



        context['table'] = table
        context['checkpoint_list'] = checkpoint_list
        return context

def post_mark(request):
    score = request.POST.get('score')
    checkpoint  = request.POST.get('checkpoint')
    student  = request.POST.get('student')
    mark,created =  Mark.objects.get_or_create(student_id=student,checkpoint_id =checkpoint)
    mark.score=score
    mark.save()
    res = {
        'student':mark.student.id,
        'checkpoint':mark.checkpoint.id,
        'score':mark.score,
        'date':mark.date,
           }
    return JsonResponse(res,safe=False)

def post_mark2(request):
    score = request.POST.get('score')
    checkpoint  = request.POST.get('checkpoint')

    checkpoint =  Checkpoint.objects.get(id=checkpoint)
    res = []
    for student in  checkpoint.course.student.all():
        mark,created =  Mark.objects.get_or_create(student=student,checkpoint_id =checkpoint)
        mark.score=score*2
        mark.save()
        data = {
            'student':mark.student.id,
            'checkpoint':mark.checkpoint.id,
            'score':mark.score,
            'date':mark.date,
           }

        res.append(data)
    return JsonResponse(res,safe=False)



class StudentDetail(DetailView):
    model = Student
class CourseSetFilter(FilterSet):
    search = filters.CharFilter(field_name="name",lookup_expr="icontains")
    student_num = filters.CharFilter(method="get_student_num")
    def get_student_num(self, queryset, name, value):
        # construct the full lookup expression.
        if value:
            queryset=queryset.filter(student__gte=value)
        return queryset
    class Meta:
        model = Course
        fields = '__all__'
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    model = Course
    serializer_class = CourseSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class  = CourseSetFilter

class CheckpointSetFilter(FilterSet):
    class Meta:
        model = Checkpoint
        fields = '__all__'
class CheckpointViewSet(viewsets.ModelViewSet):
    queryset = Checkpoint.objects.all()
    model = Checkpoint
    serializer_class = CheckpointSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class  = CheckpointSetFilter
   # permission_classes = [IsAuthenticated,DjangoModelPermissions]
