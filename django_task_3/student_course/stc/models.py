from django.db import models

# Create your models here.
class Course(models.Model):
    course_name=models.CharField(max_length=80)
    def __str__(self):
        return self.course_name
class Teacher(models.Model):
    tname=models.CharField(max_length=50)
    phone_number=models.IntegerField()
    temail=models.EmailField()
    tcourse=models.ForeignKey(Course,on_delete=models.CASCADE)
    def __str__(self):
        return self.tname
class Student(models.Model):
    sname=models.CharField(max_length=50)
    phone_number=models.IntegerField()
    semail=models.EmailField()
    scourse=models.ManyToManyField(Course)
    def __str__(self):
        return self.sname