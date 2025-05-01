

from finalproject import books

b = books()

 
v = input ("would you like to add a book? 'yes', 'no' ")
if v == "yes":
    c = b.hey()

elif v == "no":
    c = b.minus()