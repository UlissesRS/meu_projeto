import matplotlib.pyplot as plt 
import numpy as np 


x = np.linspace(0,10,100)
y = x**2

plt.figure(figsize = [10,8])

plt.plot(x,y, lw = 2, zorder = 2)
plt.show()
