
input = ['a','b','c','d']
list = []
asslist = []
list = input[:2]
#print(list)
for x in range(len(list)):
    list.append(list[0])
    list.pop(0)

    for x in range(3):
        list.insert(x,"c")
        #print(list)
        asslist.extend(list)
        #list.pop(x)
        for y in range(4):
            list.insert(y,"d")
            print(list)
            asslist.extend(list)
            list.pop(y)
        list.pop(x)
            
#print(list)
print(asslist)