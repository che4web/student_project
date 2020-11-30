from django.shortcuts import render
from studentapp.models import Student,Course
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

    return JsonResponse(student_list,safe=False)




class CourseList(ListView):
    model = Course
    paginate_by = 10

class CourseDetail(DetailView):
    model = Course

    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['add_vart'] ="traa tata "
        return context

class StudentDetail(DetailView):
    model = Student
