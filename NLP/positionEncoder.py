
import matplotlib.pyplot as plt
import numpy as np

ids=range(0,512)
pos=range(0,20)
imgs=np.zeros(shape=(len(ids),len(pos)))

d_model=512
for i in ids:
    for p in pos:
        if i%2==0:
            imgs[i][p]=np.sin(p/(10000**(2*i/d_model)))
        else:
            imgs[i][p] = np.cos(p / (10000 ** (2 * i / d_model)))


plt.figure()
plt.imshow(imgs,cmap=plt.get_cmap('summer'))
plt.xlabel('pos')
plt.ylabel('feature')
plt.show()

