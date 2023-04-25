import random

def sub(string, posição, substituto):
    a = list(string)
    a[posição] = substituto
    lines = "".join(a)
    return lines
theme = int(input("Choose a theme:\n(1)Fruits (2)Countries (3)Animals (4)Elements "))
if theme == 1:
    with open('fruits.txt', 'r') as fruits:
        m = fruits.readlines()
if theme == 2:
    with open('countries.txt', 'r') as countries:
        m = countries.readlines()
if theme == 3:
    with open('animals.txt', 'r') as animals:
        m = animals.readlines()
if theme == 4:
    with open('elements.txt', 'r') as elements:
        m = elements.readlines()

answer = random.choice(m).strip("\n")
    
lines = ""
for i in list(answer):
    if i == " ":
        lines += " "
    else:
        lines += "_"

print(lines)
errors = 0

while lines != answer:
    letter = input("Chose a letter: ")
    if letter in list(answer):
        for posicao, a in enumerate(list(answer)):
            if a == letter:
                lines = sub(lines, posicao, letter)
        print(lines)
    else:
        print("Try again!")
        errors += 1
        print(f"Errors: {errors}/5")
    if errors == 5:
        print("You lost!")
        print(f"The answer was {answer}")
        break