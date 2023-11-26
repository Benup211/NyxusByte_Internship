from copy import deepcopy
class Student:
    _student_list=list()
    def __init__(self):
        _student_list=list()
    def __str__(self):
        print(f"{'Student Management System':#^100}")
    def AddStudent(self):
        name=input("Enter student name:")
        try:
            roll_no=int(input("Enter Student roll no:"))
            if len(self._student_list)>0:
                match_found=False
                for student in self._student_list:
                    if student['roll_no']==roll_no:
                        match_found=True
                        break
                if match_found:
                    print(f"Given Roll no:{roll_no} is already assigned to student")
                    return
            mark=int(input("Enter mark of given student:"))
            dict_value={'name':name,'roll_no':roll_no,'mark':mark}
            self._student_list.append(dict_value)
        except Exception as E:
            print(f"Error occur:{E}")
    def view_student(self):
        if len(self._student_list)>0:
            print("#"*100)
            for index,student in enumerate(self._student_list):
                print(f"Student {index+1}")
                print(f"Student name:{student['name']}")
                print(f"Student roll_no:{student['roll_no']}")
                print(f"Student marks:{student['mark']}\n")
            print("#"*100)
        else:
            print(f"{'Student List is empty':#^100}")
    def search_student(self,roll_no):
        if len(self._student_list)>0:
            match_student=False
            for student in self._student_list:
                if student['roll_no']==roll_no:
                    match_student=True
                    break
            if match_student:
                print(f"{'Student Sucessfully found':#^100}")
                print(f"Student name:{student['name']}")
                print(f"Student roll_no:{student['roll_no']}")
                print(f"Student marks:{student['mark']}\n")
                print("#"*100)
            else:
                print(f"Given Roll_no:{roll_no} Student not found")
        else:
            print(f"{'Student List is empty':#^100}")
    def update_student(self,roll_no):
        if len(self._student_list)>0:
            match_student=False
            for student in self._student_list:
                if student['roll_no']==roll_no:
                    match_student=True
                    break
            if match_student:
                try:
                    name=input("Enter new name:")
                    mark=int(input("Enter new mark:"))
                    dict_value={'name':name,'roll_no':roll_no,'mark':mark}
                    self._student_list.remove(student)
                    self._student_list.append(dict_value)
                except Exception as E:
                    print("Error occur:{E}")
            else:
                print(f"Given Roll_no:{roll_no} Student not found")
        else:
            print(f"{'Student List is empty':#^100}")
    def remove_student(self,roll_no):
        if len(self._student_list)>0:
            match_student=False
            for student in self._student_list:
                if student['roll_no']==roll_no:
                    match_student=True
                    break
            if match_student:
                self._student_list.remove(student)
                print(f"Student having roll no:{roll_no} is sucessfully removed")
            else:
                print(f"Given Roll_no:{roll_no} Student not found")
        else:
            print(f"{'Student List is empty':#^100}")
    def sorting(self):
        if len(self._student_list)>0:
            dup_student_list=list()
            for student in self._student_list:
                if len(dup_student_list)==0:
                    dup_student_list.append(student)
                else:
                    for index,dup_student in enumerate(dup_student_list):
                        if student['mark']>dup_student['mark']:
                            dup_student_list.insert(index,student)
                            break
                    if not student in dup_student_list:
                        dup_student_list.append(student)          
            print("#"*100)
            for index,student in enumerate(dup_student_list):
                print(f"Student {index+1}")
                print(f"Student name:{student['name']}")
                print(f"Student roll_no:{student['roll_no']}")
                print(f"Student marks:{student['mark']}\n")
            print("#"*100)
        else:
            print(f"{'Student List is empty':#^100}")
student_manage=Student()
while(1):
    command=input("Enter your command [add,view,search,update,delete,sort,exit]:")
    match command:
        case 'add':
            student_manage.AddStudent()
        case 'view':
            student_manage.view_student()
        case 'search':
            roll_no=int(input("Enter roll no to search:"))
            student_manage.search_student(roll_no)
        case 'update':
            roll_no=int(input("Enter roll no to update:"))
            student_manage.update_student(roll_no)
        case 'delete':
            roll_no=int(input("Enter roll no to delete:"))
            student_manage.remove_student(roll_no)
        case 'sort':
            student_manage.sorting()
        case 'exit':
            choice=input("Are you sure you want to exit[yes/no]:").lower()
            if choice=='yes' or choice=='y':
                del student_manage
                break
            else:
                print("Continuing....")
        case default:
            print(f"{'Enter valid choice':#^100}")