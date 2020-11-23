from django.shortcuts import render
from studentapp.models import Student
from studentapp.forms import SearchForm,StudentForm
# Create your views here.
def index(request):
    if request.GET:
        form = SearchForm(request.GET)
    else:
        form = SearchForm()

    form_student = StudentForm()
    context = {'form':form}
    context = {'form_student':form_student}
    if form.is_valid():
        search = form.cleaned_data['search']
        student_id= form.cleaned_data['student_id']
        if not student_id:
            context['student_list'] = Student.objects.filter(name__icontains=search)
        else:
            context['student_list'] = Student.objects.filter(id=student_id)
    else:
        context['error'] = form.errors

    return render(request,'index.html',context)
