from django.shortcuts import render
from studentapp.models import Student,Course,Mark
from studentapp.forms import SearchForm,StudentForm
from django.db.models import Max
from django.views.generic import DetailView,ListView
from django.http import JsonResponse
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

    return render(request,'index.html',context)
def student_json(request):
    if request.GET:
        form = SearchForm(request.GET)
    else:
        form = SearchForm()

    form_student = StudentForm()
    if form.is_valid():
        search = form.cleaned_data['search']
        queryset = Student.objects.filter(name__icontains=search)
    else:
        queryset = Student.objects.all()
    student_list = list(queryset.values('id','name'))
    offset = form.cleaned_data['offset']
    if offset:
        offset = int(offset)
    else:
        offset= 0
    return JsonResponse(student_list[offset:offset+2],safe=False)




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
