from Borrow_Return_System import borrow_return
class reportGeneration(borrow_return):
    def __init__(self):
        super().__init__()
        print(f"{'Report Management':#^100}")
        print(f"{'bookReport->Book Inventory Report':-^100}")
        print(f"{'memberReport->Member Report':-^100}\n")
    def bookInventory(self):
        books=super().getbookList()
        if len(books)>0:
            print(f"{'Book Inventory':#^100}")
            for index,book in enumerate(books):
                if book['quantity']>0:
                    print(f"Book {index+1}")
                    print(f"Book name:{book['name']}")
                    print(f"Book author:{book['author']}")
                    print(f"Book quantity:{book['quantity']}")
                    print(f"Book isbn:{book['isbn']}")
            print("#"*100)
        else:
            print(f"{'Book Inventory is empty':#^100}")
    def memberBorrowReport(self):
        members=super().getMemberList()
        if len(members)>0:
            print(f"{'Book Borrow List':#^100}")
            for index,member in enumerate(members):
                if member['borrowBook']!=None:
                    print(f"Memeber {index+1}")
                    print(f"Member name:{member['name']}")
                    print(f"Member role:{member['role']}")
                    print(f"Member borrowed book:{member['borrowBook']}")
            print("#"*100)     
        else:
            print(f"{'Library Member are none':#^100}")