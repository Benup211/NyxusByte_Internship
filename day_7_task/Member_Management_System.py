class libraryMember:
    _member_list=list()
    def __init__(self):
        print("Member instance")
    def addMember(self):
        name=input("Enter your name to register in library:")
        role=input("Enter your role in the library:")
        if len(self._member_list)>0:
            match_found=False
            for member in self._member_list:
                if member['name']==name:
                    match_found=False
                    break
            if match_found:
                print(f"Memeber {name} is already added")
            else:
                self._member_list.append({'name':name,'role':role,'borrowBook':''})
                print(f"Member {name} sucessfully added")
        else:
            self._member_list.append({'name':name,'role':role,'borrowBook':''})
            print(f"Member {name} sucessfully added")
    def getMemberList(self):
        return self._member_list
    def updateMember(self):
        name=input("Enter your name to update to the library:")
        if len(self._member_list)>0:
            match_found=False
            for member in self._member_list:
                if member['name']==name:
                    match_found=False
                    break
            if match_found:
                name=input("Enter your updated name:")
                role=input("Enter your updated role in the library:")
                self._member_list.remove(member)
                self._member_list.append({'name':name,'role':role,'borrowBook':''})
            else:
                print(f"Member {name} not found")
        else:
            print(f"{'Member List of library is empty':#^100}")
    def memberRegisterBook(self,name,book_name):
        for member in self._member_list:
                if member['name']==name:
                    break
        self._member_list.remove(member)
        member['borrowBook']=book_name
        self._member_list.append(member)
    def memberDeregisterBook(self,name):
        for member in self._member_list:
                if member['name']==name:
                    break
        self._member_list.remove(member)
        member['borrowBook']=''
        self._member_list.append(member)
    def checkMember(self,name):
        if len(self._member_list)>0:
            match_found=False
            for member in self._member_list:
                if member['name']==name:
                    match_found=True
                    break
            if match_found:
                print(f"Memeber {name} is in list")
                return True
            else:
                print("Member not in List.Redirecting to registering")
                self.addMember()
                return False
        else:
            print(f"{'Member list is empty':#^100}")
    def removeMember(self):
        name=input("Enter your name to remove member of library:")
        if len(self._member_list)>0:
            match_found=False
            for member in self._member_list:
                if member['name']==name:
                    match_found=False
                    break
            if match_found:
                if member['borrowBook']=='':
                    self._member_list.remove(member)
                    print(f"Member {name} sucessfully removed")
                else:
                    print(f"Return Book before Clearing Your Member List in the Library")
            else:
                print(f"Member {name} not found")
        else:
            print(f"{'Member List of library is empty':#^100}")
