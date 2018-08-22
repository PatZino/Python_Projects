"""
s= int(input("Enter your number\n"))
if(s%4==0):
    print("This is a leap year")
else:
    print("The year is normal")

sen = "how"
print("length of sentence = ", len(sen))

if len(sen) > 5:
    print("The len of this sentence is greater than 5")
else:
    print("It is lesser than 5")
"""

name= input("Enter your name\n")
score=0
Q1=input("Which of the following options is the closest in meaning to the phrase underlined in the sentence below? It"
         " is fascinating to see life forms cope with varied environmental conditions.\n" "(A) adopt to\n (B) adapt to"
         "\n (C) adept in\n (D) accept with\n Enter your answer here :\n ")
if Q1 == "B":
    print("Correct")
    score += 1
    print("Your score is", score)
else:
    print("Wrong")
    print("Your score is", score)

Q2=input("In a press meet on the recent scam, the minister said, The buck stops here. What did the minister convey by" \
        " the statement?\n " " (A) He wants all the money\n (B) He will return the money\n  (C) He will assume final\n " \
        "responsibility\n (D) He will resist all enquiries\n Enter your answer here :\n")
if(Q2=="C"):
    print("Correct")
    score+=1
    print("Your score is", score)
else:
    print("Wrong")
    print("Your score is", score)

Q3=input("IF (z + 1/z)2 = 98, compute (z2 + 1/z2)" " (A) 96\n (B) 99\n (C) 100\n (D) 94\n Enter your answer here :\n")
if(Q2=="A"):
    print("Correct")
    score+=1
    print("Your score is", score)
else:
    print("Wrong")
    print("Your score is", score)
print(name, " your score is", score)

