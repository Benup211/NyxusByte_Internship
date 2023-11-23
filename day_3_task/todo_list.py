class TodoList:
    def __init__(self):
        self.help_message()
        self._todo_list=list()
    def help_message(self):
        print(f"{'Todo List Program':#^100}")
        print(f"{'add->add a task to the to-do list':-^100}")
        print(f"{'complete->mark a task as complete':-^100}")
        print(f"{'viewall->view the current task in the todo list':-^100}")
        print(f"{'viewcomplete->view the completed task in todo list':-^100}")
        print(f"{'viewimcomplete->view all the imcomplete task in the todo list':-^100}")
        print(f"{'help->display all the help message':-^100}")
        print(f"{'exit->exit the program':-^100}")
    def Todolist_Innitialization(self):
        self._todo_list=dict()
        print("Initialize todo empty list")
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
    def incompleted_view(self):
        if len(self._todo_list)>0:
            print(f"{'Todo list Incompleted task':#^100}")
            for task in self._todo_list:
                if task['status']=='incomplete':
                    print(f"Task name={task['task']},Description={task['description']},status={task['status']}")
        else:
            print(f"{'Todo List is empty':#^100}")
    def invalid_view(self):
        print(f"{'Invalid command':#^100}")
        self.help_message()
Todo_ins=TodoList()
while(1):
    command=input("Enter your command [add,complete,viewall,viewcomplete,viewincomplete,help,exit]:")
    match command:
        case 'add':
            tsk_name=input("Enter a task name:")
            task_desc=input("Enter description:")
            Todo_ins.add(tsk_name,task_desc)
        case 'complete':
            tsk_name=input("Enter a task to set it complete:")
            Todo_ins.complete(tsk_name)
        case 'viewall':
            Todo_ins.view_all()
        case 'viewcomplete':
            Todo_ins.competed_view()
        case 'viewincomplete':
            Todo_ins.incompleted_view()
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