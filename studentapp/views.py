from django.shortcuts import render
from studentapp.models import Student,Course
from studentapp.forms import SearchForm,StudentForm
from django.db.models import Max
from django.views.generic import DetailView,ListView
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

class CourseList(ListView):
    model = Course
    paginate_by = 1

class CourseDetail(DetailView):
    model = Course

    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['add_vart'] ="traa tata "
        return context
