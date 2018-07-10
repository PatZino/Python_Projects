"""
Exhaustive search. Works until a target string is found.
Checks all (26 + 1)**14 possible strings.
Should be run in a terminal for the best effect.

"""
from __future__ import print_function

import sys
import time
import string
import itertools

TARGET = "CHARLES DARWIN"
CHARACTERS = string.ascii_uppercase + " "

"""

# exhaustive search -----------------------------------------------------------
for candidate in itertools.product(CHARACTERS, repeat=len(TARGET)):
    candidate = "".join(candidate)
    print(candidate, end="\r")
    if candidate == TARGET:
        break
        
# Random search ----------------------------------------------------------------
def evaluate(solution):
    return sum(1 for s,t in zip(solution, TARGET) if s != t)


best = len(TARGET)

while(True):
    candidate = [random.choice(CHARACTERS) for i in range(len(TARGET))]
    distance = evaluate(candidate)

    if distance < best:
        best = distance
        print("{0:02} {1}".format(distance, "".join(candidate)))
        
# C-style distance calculation ---------------------------------------------------------------------
def evaluate(solution):
  distance = 0

  for i in range(len(TARGET)):
    if solution[i] != TARGET[i]:
      distance += 1

  return distance
"""


def evaluate(solution):
    return sum(1 for s, t in zip(solution, TARGET) if s != t)


best = len(TARGET)

for candidate in itertools.product(CHARACTERS, repeat=len(TARGET)):
    distance = evaluate(candidate)
    if distance < best:
        best = distance
        print("{0:02} {1}".format(distance, "".join(candidate)))
