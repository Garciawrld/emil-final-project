
class books():
    def __init__(self):
        self.author = ""
        self.title = ""
        self.price = 0 
        self.books = {}
        self.name = ""

    def hey(self):
        self.title = input ("add a book")
        self.author = input ("enter a author ")
        self.price =  input ("$10")
        self.books[self.title] = {"author": self.author,"price": self.price }
        print (self.books)
 
     

def add (self):

    self.title = input ('enter the name of the book you would like to add\n')
    self.author = input ("enter the author of the bookyou just add \n ")
    self.price=float (input ("enter the price of the book \n "))
    self.books[self.title]= {'author': self.author, 'price': self.price}
    

    def sell(self):
        self.delete=input("what you would like to sell?\n")
        try:
            str(self.name)
            if self.name in self.books:
                self.books.pop(self.name)
            print("the remaining books are:",self.books)
        except:
            print("please enter a book tittle ")

def showbooks (self):
     print(self.books ['Author'])     
     print(self.books ['price'])    

def options (self):

     