import  datetime


# Gets the user name from a prompt

userName = input("Login: ")

# allowed user name
user1 = "Pat"
user2 = "Tricia"

if userName == user1:
    print("Access granted")
elif userName == user2:
    print("Welcome on board")
else:
    print("Access denied")


# working with date and time

now = datetime.datetime.now()
print("-" * 25)
print("1 week ago was it: ", now - datetime.timedelta(weeks=1))
print("100 days ago was: ", now - datetime.timedelta(days=100))
print("1 week from now is it: ",  now + datetime.timedelta(weeks=1))
print("In 1000 days from now is it: ", now + datetime.timedelta(days=1000))

print("-" * 25)
birthday = datetime.datetime(2019, 0o04, 21)

print(birthday)
print("Birthday in ... ", birthday - now)
print("-" * 25)

print("-" * 25)
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)


def printdoc():
    """
    Trying to print doc
    Hello Ifeanyi
    """


print(printdoc.__doc__)
