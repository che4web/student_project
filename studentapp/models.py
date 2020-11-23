from django.db import models

# Create your models here.

class CommonInfo(models.Model):
    name = models.CharField(max_length=255,verbose_name="ФИО")
    age = models.IntegerField(blank=True,null=True,verbose_name="возраст")
    class Meta:
        abstract = True

class Group(models.Model):
    name = models.CharField(max_length=255,verbose_name="Название группы")



class Student(CommonInfo):
    group = models.ForeignKey(Group,on_delete=models.PROTECT)
    def __str__(self):
        return 'Студент '+self.name

    class Meta:
        verbose_name ='Студент'
        verbose_name_plural ='Студенты'

class Proffessor(CommonInfo):
    def __str__(self):
        return "Профессор" + self.name


class Course(models.Model):
    name = models.CharField(max_length=255,verbose_name="Название предмета")

class Mark(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    score =  models.IntegerField()

    def __str__(self):
        return "{}, {}".format(self.course.name,self.score)
