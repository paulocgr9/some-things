import random

characters = int(input("How many characters must your password have?"))
upper = input("Uppercase? \n(y)yes (n)no ")
lower = input("Lowercase? \n(y)yes (n)no ")
num = input("Numbers? \n(y)yes (n)no ")
char = input("Special Characters? \n(y)yes (n)no ")

p = []
if upper != "n" and upper == "y":
    with open('Password/upper.txt', 'r') as u:
        up = u.readlines()
        for i in up:
            p.append(i)
if lower != "n" and lower == "y":
    with open('Password/lower.txt', 'r') as l:
        lo = l.readlines()
        for i in lo:
            p.append(i)
if num != "n" and num == "y":
    with open('Password/num.txt', 'r') as n:
        nu = n.readlines()
        for i in nu:
            p.append(i)
if char != "n" and char == "y":
    with open('Password/special.txt', 'r') as s:
        sp = s.readlines()
        for i in sp:
            p.append(i)

m = ""
for i in range(characters):
    m = m.join(random.choice(p)).strip("\n")

print(m)