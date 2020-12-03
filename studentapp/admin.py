from django.contrib import admin
from studentapp.models import Student,Proffessor,Group,Course,Mark,Checkpoint
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

class CheckpointInline(admin.TabularInline):
    model = Checkpoint

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines=[
        CheckpointInline
    ]

@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    pass
