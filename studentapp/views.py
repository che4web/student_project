from django.shortcuts import render
from studentapp.models import Student,Course
from studentapp.forms import SearchForm,StudentForm
from django.db.models import Max
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

def course_list(request):
    if request.GET:
        form = SearchForm(request.GET)
    else:
        form = SearchForm()
    context = {'form':form}
    course_list =   Course.objects.all()
    if form.is_valid():
        search = form.cleaned_data['search']
        course_list = course_list.filter(name__icontains=search)
    else:
        context['error'] = form.errors
    context['course_list'] = course_list

    return render(request,'course_list.html',context)

