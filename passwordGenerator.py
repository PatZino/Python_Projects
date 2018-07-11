import string
from random import *


characters = string.ascii_letters + string.digits + string.punctuation
password = "".join(choice(characters) for x in range(randint(8, 16)))

print(password)


characters2 = "patricia@$^Ewoma-zinoEdaware201807"
password2 = "".join(choice(characters2) for i in range(randint(8, 16)))

print(password2)


password3 = ""
characters3 = "Ronke@$^Ewoma-zinoEdaware201807"
for i in range(randint(8, 16)):
    password3 += choice(characters3)
print(password3)

print("_"*50)

print("Print a random number in  the range of 1 - 20: ")
randomNumber = randint(1, 20)
print(randomNumber)






