from django.contrib import admin
from studentapp.models import Student,Proffessor,Group,Course,Mark
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('name','age')

@admin.register(Proffessor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display=('name','age')

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass

@admin.register(Course)
class GroupAdmin(admin.ModelAdmin):
    pass

@admin.register(Mark)
class GroupAdmin(admin.ModelAdmin):
    pass
