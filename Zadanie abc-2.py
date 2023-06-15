
input = ['a','b','c','d']
list = []
asslist = []
list = input[:2]
print(list)
for x in range(len(list)):
    list.append(list[0])
    list.pop(0)

    for x in range(3):
        list.insert(x,input[2])
        #print(list)
        asslist.extend(list)
        #list.pop(x)
        for y in range(4):
            list.insert(y,input[3])
            print(list)
            asslist.extend(list)
            list.pop(y)
        list.pop(x)
            
#print(list)
print(asslist)