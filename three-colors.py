import random
win = False
numberofcarts = 0
deck = ['0','0','0']
RGB = ['R','B']

simon = []
simon.append(random.choice(RGB))
simon.append(random.choice(RGB))
simon.append(random.choice(RGB))

if simon[1]=='R':
    inverted = 'B'
else:
    inverted = 'R'

peter = [inverted,simon[0],simon[1]]

print('deck: ',deck[-1], deck[-2], deck[-3],'hand peter',peter,'hand simon',simon)

while win == False:

    deck.append(random.choice(RGB))
    numberofcarts += 1

    if simon[0] == deck[-3]:
        if simon[1] == deck[-2]:
            if simon[2] == deck[-1]:
                win = True
                print("Simon wins"," cards",deck[-3],deck[-2],deck[-1]," time to win",numberofcarts)
    if peter[0] == deck[-3]:
        if peter[1] == deck[-2]:
            if peter[2] == deck[-1]:
                win = True
                print(deck)
                print("Peter wins"," cards",deck[-3],deck[-2],deck[-1]," time to win",numberofcarts)
                