from django import forms
from studentapp.models import Student
class BootstapForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class' : 'form-control'})


class SearchForm(BootstapForm):
    search = forms.CharField(label='Имя студента', max_length=100)
    student_id= forms.IntegerField(label='id Стeднетa',required=False)
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields= "__all__"
