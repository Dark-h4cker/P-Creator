import string
from random import *
characters = string.ascii_letters + string.digits + string.hexdigits
password =  "".join(choice(characters) for x in range(randint(15, 15)))
print ("      ")
print (password)