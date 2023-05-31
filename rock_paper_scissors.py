import random

win = False
ppoints = 0
rpoints = 0

while not(win):

    print('points: ' + str(ppoints) + "-" + str(rpoints))
    ppoints = int(ppoints)
    rpoints = int(rpoints)
    choose = int(input("Choose 1/Papper, 2/Rock or 3/Scissors: "))
    rbot = random.randrange(1,4)
    
    print(choose)
    print(rbot)
    if choose == rbot:
        print('remis')
        ppoints += 1
        rpoints += 1

        if ppoints > 2 and rpoints > 2 and ppoints == rpoints:
            print("Draw -> play again")
        continue

    if rbot == 1:
        if choose == 3:
            print('player win')
            ppoints += 1
        else:
            print('robot win')
            rpoints += 1
    if rbot == 2:
        if choose == 1:
            print('player win')
            ppoints += 1
        else:
            print('robot win')
            rpoints += 1
    if rbot == 3:
        if choose == 2:
            print('player win')
            ppoints += 1
        else:
            print('robot win')
            rpoints += 1

    if ppoints > 2:
        print('Szymon.K win')
        win = True

    if rpoints > 2:
        print('Robot win')
        win = True