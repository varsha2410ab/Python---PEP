# Parent class - (Abstraction)
class LibraryItem:
    def __init__(self, days):
        self._days = days          #Encapsulation 

    def calculate_charge(self):
        pass                       #Abstraction

# Child class - (Inheritance)
class Book(LibraryItem):
    def calculate_charge(self):    #Polymorphism
        return self._days * 10


class Magazine(LibraryItem):
    def calculate_charge(self):    
        return self._days * 15

# Main class 
class LibraryApp:
    def __init__(self, item):
        self.item = item           #HAS-A 

    def show_details(self, item_type):
        print("Item Type:", item_type)
        print("Borrow Days:", self.item._days)
        print("Borrowing Charge:", self.item.calculate_charge())

book = Book(5)
app1 = LibraryApp(book)
app1.show_details("Book")
print()