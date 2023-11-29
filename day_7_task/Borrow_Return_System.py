from Book_Management_System import book
from Member_Management_System import libraryMember

class borrow_return(book,libraryMember):
    def __init__(self):
        super().__init__()
        print(f"{'Borrow Return Management':#^100}")
        print(f"{'br->borrow or return book':-^100}\n")
    def checkBook(self):
        if len(self._book_list)>0:
            check_book_name=input("Enter book name to check in Book Inventory:")
            match_found=False
            for book in self._book_list:
                if book['name']==check_book_name:
                    match_found=True
                    break
            if match_found:
                print(f"Given book {check_book_name} is avaliable")
                return check_book_name
            else:
                print(f"Given book {check_book_name} is not avaliable")
        else: 
            print(f"{'Book inventory is empty':#^100}")
    def updateBookQuantity(self):
        book_name=self.checkBook()
        if book_name!=None:
            while(1):
                choice=input("Do you want to borrow book[y/n]:").lower()
                match choice:
                    case 'y':
                        name=input("Enter you name:")
                        check_Library_member=super().checkMember(name)
                        if check_Library_member:
                            super().memberRegisterBook(name,book_name)
                            super().giveBook(book_name)
                            print(f"Book {book_name} borrowed by {name}")
                            break
                    case 'n':
                        break
                    case default:
                        print("Enter correct command")
            while(1):
                choice=input("Do you want to return book[y/n]:").lower()
                match choice:
                    case 'y':
                        name=input("Enter you name:")
                        check_Library_member=super().checkMember(name)
                        if check_Library_member:
                            super().memberDeregisterBook(name)
                            super().havebook(book_name)
                            print(f"Book {book_name} returned by {name}")
                            break
                    case 'n':
                        break
                    case default:
                        print("Enter correct command")
        else:
            print("Book Inventory is empty")