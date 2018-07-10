import random


minimum = 1
maximum = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print("Rolling the dices...")
    print("The values are....")
    print(random.randint(minimum, maximum))
    print(random.randint(minimum, maximum))

    roll_again = input("Roll the dices again?")
