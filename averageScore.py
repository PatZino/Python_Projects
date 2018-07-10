"""
step:
1.  Enter the number of subjects
2.  Enter the scored earned in each score
3.  The program calculates the average score
"""

n = int(input("Enter the number of subjects: "))

score = 0
for i in range(n):
    score += float(input("Enter the scores: "))
Average = score / n
print("The total score = ", score)
print("The average score = ", Average)


