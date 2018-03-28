from __future__ import print_function
import itertools
import random

list_of_seals = ["Ox", "Hare", "Tiger", "Snake", "Boar", "Dog", "Rat", "Horse", "Bird", "Monkey", "Ram", "Dragon"]

number = random.randint(1, 7)

initial = []

for i in range(number):
    initial.append(random.choice(list_of_seals))

#remove consecutive duplicates
jutsu = [k for k, g in itertools.groupby(initial)]

#for purposes of adding arrows
for seal in range(len(jutsu)):
    if len(jutsu) == 1:
        print(*jutsu)
    elif seal == len(jutsu) - 1:
        print(jutsu[seal], end='')
    else:
        print(jutsu[seal] + " -> ", end='')