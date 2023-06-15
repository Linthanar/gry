import numpy as np

nthrows = 10
ndice = 2

throws = np.random.randint(1,7,size=(nthrows,ndice))
print(throws)

succes = np.where(throws[:,0]==throws[:,1],1,0)

succes = np.where(throws[:,0]> 4,1,0)
print(succes)