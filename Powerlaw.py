from scipy.stats import powerlaw
import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline
fig, ax = plt.subplots(1, 1)



def generate_uniform(power_law, low, high):
    y = np.random.uniform(0., 1.)
    alpha = power_law+1.
    if power_law==0.:
        x = np.random.uniform(low, high)
    elif power_law==-1.:
        norm = np.log(high/low) 
        x = low * np.exp( y*np.log(high/low) ) 
    else:
        norm = (high/low)**alpha - 1.
        x = low * ( norm*y + 1. ) ** (1./alpha)
    return x 
    

list1=[]
np.random.seed(35)
for i in range(1000): 
    list1.append(generate_uniform(-2.5, .1, .5))

                 
                 
ax.hist(list1, bins=100, normed=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
plt.show() 

    


