import math


def exponentialFunc(x1,x2):

    result = (3 * math.pow((1-x1), 2))*math.exp(math.pow(x1, 2) + math.pow((x2+1), 2)) - \
             10 * ((x1/5)-math.pow(x1, 3) - math.pow(x2, 5)) * math.exp(math.pow(x1, 2) + math.pow(x2, 2)) - \
             ((1/3) * math.exp((math.pow((x1 + 1), 2) + math.pow(x2, 2))))
    print(result)


a = float(input("Enter a value for a: "))
b = float(input("Enter a value for b: "))
exponentialFunc(a, b)

