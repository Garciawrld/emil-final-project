
class books():
    def __init__(self):
        self.author = ""
        self.title = ""
        self.price = 0 
        self.books = {}

    def hey(self):
        self.title = input ("add a book")
        self.author = input ("enter a author ")
        self.price =  input ("$10")
        self.books[self.title] = {"author": self.author,"price": self.price }
        print (self.books)
 
     
"""
    def (self):

        self.title = input ('divine comedy:\n')
        self.author = input ("Dante alighiei: \n ")
        self.price = input ("$10: \n ")

dict = self.title or {("author")}
 
"""