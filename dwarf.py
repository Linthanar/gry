# Importing the statistics module
import statistics
import random
symulacja = []
Val = [] # zbirór 4 statystyk postaci
divider = 1000000
main = 0 #
R0 = []
R1 = []
R2 = []
R3 = []
R4 = []
R5 = []
R6 = []
R7 = []
R8 = []
R9 = []

for it in range(divider):
    Val = []
    # rzuty kostką dla kadej cechy(10)
    for sequence in range(4):
        R0.append(random.randrange(1,11) +random.randrange(1,11))
        R1.append(random.randrange(1,11) +random.randrange(1,11))
        R2.append(random.randrange(1,11) +random.randrange(1,11))
        R3.append(random.randrange(1,11) +random.randrange(1,11))
        R4.append(random.randrange(1,11) +random.randrange(1,11))
        R5.append(random.randrange(1,11) +random.randrange(1,11))
        R6.append(random.randrange(1,11) +random.randrange(1,11))
        R7.append(random.randrange(1,11) +random.randrange(1,11))
        R8.append(random.randrange(1,11) +random.randrange(1,11))
        R9.append(random.randrange(1,11) +random.randrange(1,11))

    # print(R0,R1,R2,R3,R4,R5,R6,R7,R8,R9)

    for app in range(4):
        # cztery razy powtarzamy: wyciągnięcie najmniejszej wartości, dodanie rzędu cech w liczbę, 
        # odejmujemy najmniejszą wartość i dodajemy nową
        min_r = min(R0[app],R1[app],R2[app],R3[app],R4[app],R5[app],R6[app],R7[app],R8[app],R9[app])
        plas = R0[app] + R1[app] + R2[app] + R3[app] + R4[app] + R5[app] + R6[app] + R7[app] + R8[app] + R9[app]
        plas = plas - min_r + random.randrange(1,11) + random.randrange(1,11)
        # print(plas)
        Val.append(plas)
    result = max(Val[0],Val[1],Val[2],Val[3])
    # main = main + result

    #print(Val)
    # print(main) # suma wszystkich wartości

    # print('divider w pętli ma: ',divider)
    # print('it w pętli ma: ',it)
    
    symulacja.append(result)
# print('divider ma: ',divider)
# print("wynik to -",main/divider)
print('min: ',min(symulacja))
print('max: ',max(symulacja))
print('mean: ',statistics.mean(symulacja))
