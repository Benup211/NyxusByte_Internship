class library:
    def __init__(self):
        print("Library management instance created")
        self.book_inventory()
        self.help_message()
    def help_message(self):
        print(f"{'Library Book Management Command':#^100}")
        print(f"{'add->add a book from the inventory':-^100}")
        print(f"{'remove->remove a book from the inventory':-^100}")
        print(f"{'display->display the current books in the inventory':-^100}")
        print(f"{'exit->exit the program':-^100}")
    def book_inventory(self):
        self._books=list()
        print("Empty book list created")
    def book_addition(self,book_name,author_name):
        self._books.append([book_name,author_name])
    def book_removal(self,book_name):
        if len(self._books)>0:
            for i in range(len(self._books)):
                if book_name in self._books[i][0]:
                    print(f"The {self._books[i][0]} book with {self._books[i][1]} author is removed.")
                    self._books.pop(i)
                    break
                else:
                    print("Book is not found in inventory")
        else:
            print("Book inventory is empty")
    def inventory_display(self):
        if len(self._books)>0:
            print("Book Inventory:")
            for i in range(len(self._books)):
                print(f"{i+1} Book={self._books[i][0]} Author={self._books[i][1]}")
        else:
            print("Book Inventory is empty")
Nyxus_library=library()
while(1):
    command=input("Enter your command [add,remove,display,exit]:")
    match command:
        case 'add':
            add_book=input("Enter book name to add in the inventory:")
            add_author=input(f"Enter {add_book} author:")
            Nyxus_library.book_addition(add_book,add_author)
        case 'remove':
            remove_book=input("Enter book name to remove from inventory:")
            Nyxus_library.book_removal(remove_book)
        case 'display':
            Nyxus_library.inventory_display()
        case 'exit':
            choice=input("Are you sure you want to exit[yes/no]:").lower()
            if choice=='yes' or choice=='y':
                del Nyxus_library
                break
            else:
                print("Continuing....")
        case default:
            print("Enter correct command [add,remove,display,exit]")