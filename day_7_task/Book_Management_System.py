class book:
    _book_list=list()
    def __init__(self):
        print(f"{'Book Management':#^100}")
        print(f"{'addBook->add a book to Inventory':-^100}")
        print(f"{'updateBook->update a book to Inventory':-^100}")
        print(f"{'removeBook->add a book to Inventory':-^100}\n")
        print(f"{'Member Management':#^100}")
        print(f"{'addMember->register a member':-^100}")
        print(f"{'updateMember->update a member':-^100}")
        print(f"{'removeMember->remove a member':-^100}\n")
    def addNewBook(self):
        book_name=input("Enter name of the book:")
        try:
            isbn=input("Enter isbn no. of the book:")
        except Exception as E:
            print(f"Error {E}!Try again")
            return
        author=input("Enter author of the book:")
        if len(self._book_list)>0:
            match_found=False
            for book_item in self._book_list:
                if book_item['name']==book_name:
                    match_found=True
                    break
            if match_found:
                print(f"Given book {book_name} is already in the Book list")
                self._book_list.remove(book_item)
                book_item['quantity']+=1
                self._book_list(book_item)
            else:
                self._book_list.append({'name':book_name,'author':author,'quantity':1,'isbn':isbn})
                print(f"Book {book_name} sucessfully Added")
        else:
            self._book_list.append({'name':book_name,'author':author,'quantity':1,'isbn':isbn})
            print(f"Book {book_name} sucessfully Added")
    def getbookList(self):
        return self._book_list
    def updateBook(self):
        if len(self._book_list)>0:
            book_name=input("Enter name of the book to update:")
            match_found=False
            for book_item in self._book_list:
                if book_item['name']==book_name:
                    match_found=True
                    break
            if match_found:
                book_name=input("Enter update name of the book:")
                author=input("Enter update author of the book:")
                try:
                    quantity=int(input("Enter updated quantity of the book:"))
                    isbn=int(input("Enter updated isbn no of the book:"))
                except Exception as E:
                    print(f"Error {E}!Try again")
                    return
                self._book_list.remove(book_item)
                self._book_list.append({'name':book_name,'author':author,'quantity':quantity,'isbn':isbn})
                print(f"Book {book_name} sucessfully Added")
            else:
                print(f"{'Book not found':#^100}")
        else:
            print(f"{'Book List is empty':#^100}")
    def removeBook(self):
        if len(self._book_list)>0:
            book_name=input("Enter name of the book to remove:")
            match_found=False
            for book_item in self._book_list:
                if book_item['name']==book_name:
                    match_found=True
                    break
            if match_found:
                self._book_list.remove(book_item)
                print(f"Book {book_name} sucessfully removed")
            else:
                print(f"Book {book_name} not found")
        else:
            print(f"{'Book List is empty':#^100}")
    def giveBook(self,book):
        for book_item in self._book_list:
            if book_item['name']==book:
                break
        self._book_list.remove(book_item)
        book_item['quantity']-=1
        self._book_list.append(book_item)
    def havebook(self,book):
        for book_item in self._book_list:
            if book_item['name']==book:
                break
        self._book_list.remove(book_item)
        book_item['quantity']+=1
        self._book_list.append(book_item)