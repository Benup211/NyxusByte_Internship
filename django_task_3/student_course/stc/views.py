from django.shortcuts import render
from django.views import View
from .models import Course,Teacher,Student
# Create your views here.
class Home(View):
    stu_dict=dict()
    teacher_dict=dict()
    stu=Student.objects.prefetch_related('scourse').all()
    th=Teacher.objects.select_related('tcourse').all()
    for s in stu:
        name=s.sname
        c_list = [c.course_name for c in s.scourse.all()]
        stu_dict[name]=c_list
    for t in th:
        name=t.tname
        ct_list=t.tcourse.course_name
        teacher_dict[name]=ct_list
    def get(self,request,*args,**kwargs):
        return render(request,'stc/home.html',{'stu_val':self.stu_dict,'t_val':self.teacher_dict})