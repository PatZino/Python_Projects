import math


b = 5
a = math.factorial(b)
print("the factorial of %d =" % b, a)

print("___________________________________")

list1 = [12, 2, 12]
for x in range(len(list1)):
    print(list1[x])

print("___________________________________")

for i in range(4):
    print(i)

print("___________________________________")

mylist = [x*x for x in range(3)]
for i in mylist:
    print(i)

print("___________________________________")

for i in range(3):
    for j in range(2):
        d = i * j
        print(d)
    print("**")

print("_________________Reverse a string : 1__________________")


def reverse(sentence):
    sentence = sentence[::-1]
    return sentence


sen = input("Enter a sentence : ")
print(sen)
print("the reverse string is : ")

print(reverse(sen))

print("_________________Reverse a string : 2__________________")


def reverse2(sentence):
    sentence = "".join(reversed(sentence))
    return sentence


sen = input("Enter a sentence : ")
print(sen)
print("the reverse string is : ")

print(reverse2(sen))


print("_________________Reverse a string : 3__________________")


result = " "
reverseword = " "
mylist = "She is a girl"
# mylist = input("Enter a sentence: ")
for i in range(1):
    result += mylist[::-1]
print(result)

print("_________________Reverse each word in a string__________________")

p = " "
print(mylist.split(" "))
d = mylist.split(" ")
for j in range(len(d)):
    reverseword += d[j][::-1] + " "
print(reverseword)




