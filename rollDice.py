import numpy as np
import matplotlib.pyplot as plt

nthrows = 1000001
ndice = 2
throws = np.random.randint(1,7,size=(nthrows,ndice))
print(throws)

succes = np.where(throws[:,0]==throws[:,1],1,0)

print(succes)

print('prawdopodobieeństwo wynisi {0} '.format(succes.sum()/nthrows))

succes = succes.cumsum()
succes = succes / np.arange(1,nthrows+1,1)
plt.plot(succes[:20000])
plt.show()