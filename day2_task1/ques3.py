class library:
    def __init__(self):
        print("Library management instance created")
        self.help_message()
    def help_message(self):
        print(f"{'Library Book Management Command':#^100}")
        print(f"{'add->add a book from the inventory':-^100}")
        print(f"{'remove->remove a book from the inventory':-^100}")
        print(f"{'display->display the current books in the inventory':-^100}")
        print(f"{'exit->exit the program':-^100}")
    def book_inventory(self):
        