market = [1,2,3,4,5]
market2 = [5,4,3,2,1]
market3 = [5,3,6,1,5]
market4 = [1,2,5,3,4]
market5 = [5,0,5,0,5]

def stock(l):
    print(l)
    diff = []
    start = 0
    end = 0
    mid = 0
    for x in range(5):
        #print("1====: {}".format(x))
        for i in range(4-x):
            #  print("2: {}".format(i))
            start = l[x] 
            end = l[x+i+1]
            mid = end - start
            #print(start,end,mid)
            diff.append(mid)
    if max(diff) > 0:
        return max(diff)
    else:
        return 0

print(stock(market))
print('=================')
print(stock(market2))
print('=================')
print(stock(market3))
print('=================')
print(stock(market4))
print('=================')
print(stock(market5))

for element in market:
    print(element, market.index(element))