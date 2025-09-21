import numpy as np
import matplotlib.pyplot as plt

tau=2 #Taking the initial value of lifetime as 2ms

b1=0.01
b2=0.5
b3=0.999

t1=2/np.sqrt(1-(b1)**2)
t2=2/np.sqrt(1-(b2)**2)
t3=2/np.sqrt(1-(b3)**2)

x=[b1,b2,b3]
y=[t1,t2,t3]
plt.plot(x,y,'o--')
plt.xlabel(r'$\frac{v}{c}$',size=18)
plt.ylabel(r'$\tau$',size=18)
plt.title('Variation of lifetime of the particle in different velocities')
plt.show()
