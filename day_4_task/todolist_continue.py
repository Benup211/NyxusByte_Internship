class TodoList:
    def __init__(self):
        self.help_message()
        self.Todolist_Innitialization()
    def help_message(self):
        print(f"{'Todo List Program':#^100}")
        print(f"{'add->add a task to the to-do list':-^100}")
        print(f"{'complete->mark a task as complete':-^100}")
        print(f"{'delete->Delete the todo list and take it to the bin if its not permanent':-^100}")
        print(f"{'viewall->view the current task in the todo list':-^100}")
        print(f"{'viewcomplete->view the completed task in todo list':-^100}")
        print(f"{'viewimcomplete->view all the imcomplete task in the todo list':-^100}")
        print(f"{'viewbin->view all the task that are deleted and are currently in the bin'}")
        print(f"{'restore->restore the deleted task from the bin':-^100}")
        print(f"{'clearbin->delete all the to-dos that are presented in the bin':-^100}")
        print(f"{'help->display all the help message':-^100}")
        print(f"{'exit->exit the program':-^100}")
    def Todolist_Innitialization(self):
        self._todo_list=list()
        self._todo_bin=list()
        print("Initialize todo empty list and bin")
    def add(self,task_name,description):
        if len(self._todo_list)>0:
            matched_task=False
            for task in self._todo_list:
                if task_name==task['task']:
                    matched_task=True
            if (matched_task):
                print("Same task cannot be added twice")
            else:
                self._todo_list.append({'task':task_name,'description':description,'status':'incomplete'})
                print(f"{'Task Sucessfully added':*^100}")
        else:
            self._todo_list.append({'task':task_name,'description':description,'status':'incomplete'})
            print(f"{'Task Sucessfully added':*^100}")
    def complete(self,task_name):
        if len(self._todo_list)>0:
            matched_task=False
            for task in self._todo_list:
                if task_name==task['task']:
                    matched_task=True
                    break
            if(matched_task):
                task['status']='complete'
                print(f"{task_name} status is updated")
            else:
                print(f"{'Task is not found':#^100}")
        else:
            print(f"{'Todo List is empty':#^100}")
    def view_all(self):
        if len(self._todo_list)>0:
            print(f"{'Todo list All task':#^100}")
            for task in self._todo_list:
                print(f"Task name={task['task']},Description={task['description']},status={task['status']}")
        else:
            print(f"{'Todo List is empty':#^100}")
    def competed_view(self):
        if len(self._todo_list)>0:
            print(f"{'Todo list Completed task':#^100}")
            for task in self._todo_list:
                if task['status']=='complete':
                    print(f"Task name={task['task']},Description={task['description']},status={task['status']}")
        else:
            print(f"{'Todo List is empty':#^100}")
    def delete_task(self,task_name):
        if len(self._todo_list)>0:
            matched_task=False
            for task in self._todo_list:
                if task['task']==task_name:
                    matched_task=True
                    break
            if matched_task:
                choice=input("Do you want to delete permanently[yes/no]:").lower()
            if choice=='yes' or choice=='y':
                self._todo_list.remove(task)
                print(f"{'Task is deleted permanently':#^100}")
            else:
                self._todo_bin.append(task)
                self._todo_list.remove(task)
                print(f"{'Task is added to bin':#^100}")
        else:
            print(f"{'Todo List is empty':#^100}")
    def incompleted_view(self):
        if len(self._todo_list)>0:
            print(f"{'Todo list Incompleted task':#^100}")
            for task in self._todo_list:
                if task['status']=='incomplete':
                    print(f"Task name={task['task']},Description={task['description']},status={task['status']}")
        else:
            print(f"{'Todo List is empty':#^100}")
    def view_bin(self):
        if len(self._todo_bin)>0:
            print(f"{'Todo Bin':#^100}")
            for task in self._todo_bin:
                print(f"Task name={task['task']},Description={task['description']},status={task['status']}")
        else:
            print(f"{'Todo Bin is empty':#^100}")
    def restore(self,task_name):
        matched_task=False
        if len(self._todo_bin)>0:
            for task in self._todo_bin:
                if task['task']==task_name:
                    matched_task=True
                    break
            if matched_task:
                self._todo_list.append(task)
                self._todo_bin.remove(task)
                print(f"{'Task Restored Sucessfully':#^100}")
            else:
                print(f"Given {task_name} task is not in the bin")
        else:
            print(f"{'Todo Bin is empty':#^100}")
    def clearbin(self):
        self._todo_bin=list()
        print(f"{'Todo Bin is cleared sucessfully':#^100}")
    def invalid_view(self):
        print(f"{'Invalid command':#^100}")
        self.help_message()
Todo_ins=TodoList()
while(1):
    command=input("Enter your command [add,complete,delete,viewall,viewcomplete,viewincomplete,restore,viewbin,clearbin,help,exit]:")
    match command:
        case 'add':
            tsk_name=input("Enter a task name:")
            task_desc=input("Enter description:")
            Todo_ins.add(tsk_name,task_desc)
        case 'complete':
            tsk_name=input("Enter a task to set it complete:")
            Todo_ins.complete(tsk_name)
        case 'delete':
            tsk_name=input("Enter a task name:")
            Todo_ins.delete_task(tsk_name)
        case 'viewall':
            Todo_ins.view_all()
        case 'viewcomplete':
            Todo_ins.competed_view()
        case 'viewincomplete':
            Todo_ins.incompleted_view()
        case 'restore':
            tsk_name=input("Enter a task name:")
            Todo_ins.restore(tsk_name)
        case 'viewbin':
            Todo_ins.view_bin()
        case 'clearbin':
            Todo_ins.clearbin()
        case 'help':
            Todo_ins.help_message()
        case 'exit':
            choice=input("Are you sure you want to exit[yes/no]:").lower()
            if choice=='yes' or choice=='y':
                del Todo_ins
                break
            else:
                print("Continuing....")
        case default:
            Todo_ins.invalid_view()