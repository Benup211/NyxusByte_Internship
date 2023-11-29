from Report_Generation import reportGeneration
class LibrarySystem(reportGeneration):
    def __init__(self):
        super().__init__()
Nyxus_library=LibrarySystem()
while(1):
    command=input("Enter above avaliable command:")
    match command:
        case 'addBook':
            Nyxus_library.addNewBook()
        case 'updateBook':
            Nyxus_library.updateBook()
        case 'removeBook':
            Nyxus_library.removeBook()
        case 'addMember':
            Nyxus_library.addMember()
        case 'updateMember':
            Nyxus_library.updateMember()
        case 'removeMember':
            Nyxus_library.removeMember()
        case 'br':
            Nyxus_library.updateBookQuantity()
        case 'bookReport':
            Nyxus_library.bookInventory()
        case 'memberReport':
            Nyxus_library.memberBorrowReport()
        case 'exit':
            choice=input("Are you sure you want to exit[yes/no]:").lower()
            if choice=='yes' or choice=='y':
                del Nyxus_library
                break
            else:
                print("Continuing....")
        case default:
            print(f"{'Enter valid choice':#^100}")