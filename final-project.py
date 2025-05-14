

from finalproject import books

b = books()
v=""
 
v = input ("would you like to add a book? 'yes', 'no' ")
if v == "yes":
    c = b.add()
v= input ("would you like to remove a book?")
if v == "yes":
    c = b.sell()
 


