## c = colors
## n = numbers 
import random

deck = {}
color = ['S','M','D','C']
special = 'JQKA'
score = [11, 12, 13, 14]

# fill out the deck with cards
def fillCards():
    for c in range(0,4):
        p = 0
        for n in range(2,11):
            deck[color[c]+str(n)] = n
       
        for s in special:
       
            deck[color[c] + s]  = score[p]
            p += 1

p_one = []

p_two = []

def deal():
    pass

fillCards()
 
l = list(deck.items())
random.shuffle(l)
deck = dict(l)

li = list(deck.items())
for y in range(0,26):
    p_one.append(li[y])

for x in range(26,52):
    p_two.append(li[x])

p_one = dict(p_one)

p_two = dict(p_two)

print(p_one)
# print(len(p_one))

print(p_two)
# print(len(p_two))
score_p1 = 0

score_p2 = 0

print(list(p_one)[-1]) # zwraca klucz ostatniego elementu

nrcard = -1

for x in range(26):
    if p_one.get(list(p_one)[nrcard]) > p_two.get(list(p_two)[nrcard]):
        print('gracz 1 wins')
        score_p1 += 1
        # pop p1 card
        # pop p2 card
        # stworzyc nowe elementy wygANYCH kart w captured cards p1 
    elif p_one.get(list(p_one)[nrcard]) < p_two.get(list(p_two)[nrcard]):
        print('gracz 2 wins')
        score_p2 += 1
    else:
        print('remis')
        score_p2 += 1
    nrcard -= 1

print(str(score_p1) + "Punkty gracza pierwszego")
print(str(score_p2) + "Punkty gracza drugiego")

if score_p1 > score_p2:
    print('Gracz pierwszy wygrywa')
elif score_p1 == score_p2:
    print('Remis')
else:
    print('Gracz drugi wygrywa')
#usuwamy po kluczu element z reki
# p_one.pop(list(p_one)[-1]) 
# print(p_one)