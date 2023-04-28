import random

characters = int(input("How many characters must your password have?"))
upper = input("Uppercase? \n(y)yes (n)no ")
lower = input("Lowercase? \n(y)yes (n)no ")
num = input("Numbers? \n(y)yes (n)no ")
char = input("Special Characters? \n(y)yes (n)no ")

p = []
if upper == "y":
    with open('upper.txt', 'r') as u:
        up = u.readlines()
        p = p.append(up)
if lower == "y":
    with open('lower.txt', 'r') as l:
        lo = l.readlines()
        p = p.append(lo)
if num == "y":
    with open('num.txt', 'r') as n:
        nu = n.readlines()
        p = p.append(nu)
if char == "y":
    with open('special.txt', 'r') as s:
        sp = s.readlines()
        p = p.append(sp)

final = []
for i in range(characters):
    final.append(random.choice(p).strip("\n"))
    password = "".join(final)
    
print(password)