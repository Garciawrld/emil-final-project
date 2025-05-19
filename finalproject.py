
class books():
    def __init__(self):
        self.author = ""
        self.title = ""
        self.price = 0 
        self.books = {}
        self.name = ""

    def hey(self):
        self.title = input ("add a book").upper()
        self.author = input ("enter a author ").upper()
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

    def showbook  (self):
        for x in self.books:
            print (x)
            print(self.books [x] ['author'])     
            print(self.books [x] ['price'])    


     
    def options(self):
       v= (self.books[a] [price])
       myfile = open('myfile.txt', 'w')
       for a in self.books:
            myfile.write(a)
            myfile.write("\n")
            myfile.write(self.books[a]["author"])
            myfile.write("\n")
            myfile.write(self.books[a]["price"])
            myfile.write("\n")
            myfile.close()
            myfile.write("\n")
            print(myfile)
