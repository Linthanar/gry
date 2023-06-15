
import random

death = False
x = 0
fate = 0
colt = ["O","O","B","B","O","O"]

def moveBulets(x):
    for i in range(x):
        colt.append(colt[0])
        colt.pop(0)

while death == False:
    fate = input('podaj s albo p: ')

    if fate == "s":
        x = random.randrange(1,6)
    else:
        x = 1
    moveBulets(x)

    if colt[0] == "B":
        death = True
        print("You die")



print(colt)
print(x)
print(fate)