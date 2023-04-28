import random

characters = int(input("How many characters must your password have?"))
upper = input("Uppercase? \n(y)yes (n)no ")
lower = input("Lowercase? \n(y)yes (n)no ")
num = input("Numbers? \n(y)yes (n)no ")
char = input("Special Characters? \n(y)yes (n)no ")

if upper == "y" and lower =="n" and num == "n" and char == "n":
    with open('abbb.txt', 'r') as abbb:
        e = abbb.readlines()
elif upper == "n" and lower =="y" and num == "n" and char == "n":
    with open('babb.txt', 'r') as babb:
        e = babb.readlines()
        
l = []
for i in range(characters):
    l.append(random.choice(e).strip("\n"))
    password = "".join(l)
    
print(password)