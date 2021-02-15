#!/usr/bin/env python
# coding: utf-8

# In[22]:


import numpy as np
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex

x = [1,2,3,4,2,1]

N = len(x)
def h(N):
	h = []
	for i in range(N):
		out = 0;
		if i >= 0:
			out = out+((-0.5)**i)
		if i-2 >= 0:
			out = out+((-0.5)**(i-2))
		h.append(out)
		
	return h

def DFT(x):
	X = []
	N = len(x)
	for k in range(N):
		out = 0 * 1j
		for n in range(N):
			out=out+(x[n]*np.exp(-1j*2*np.pi*k*n/N))
		X.append(out)
	return X

print("DFT of x(n)\n"+str(DFT(x)))
print()
print("DFT of h(n)\n"+str(DFT(h(N))))

fig , ax = plt.subplots(nrows = 3, ncols = 2, figsize=(12,14))

ax[0][0].stem(range(0,N),x)
ax[0][0].set_title(r'$x(n)$')
ax[0][0].grid()

ax[0][1].stem(range(0,N),h(N))
ax[0][1].set_title(r'$h(n)$')
ax[0][1].grid()
ax[1][0].stem(range(0,N),np.abs(DFT(h(N))))
ax[1][0].set_title(r'$|(H(k))|$')
ax[1][0].grid()
ax[1][1].stem(range(0,N),np.angle(DFT(h(N))))
ax[1][1].set_title(r'$\angle{H(k)}$')
ax[1][1].grid()
ax[2][0].stem(range(0,N),np.abs(DFT(x)))
ax[2][0].set_title(r'$|X(k)|$')
ax[2][0].grid()
ax[2][1].stem(range(0,N),np.angle(DFT(x)))
ax[2][1].set_title(r'$\angle{X(k)}$')
ax[2][1].grid()


#If using termux
plt.savefig('../figs/ee18btech11007.png')
plt.savefig('../figs/ee18btech11007.eps')
subprocess.run(shlex.split("termux-open ../figs/ee18btech11007.pdf"))
else
plt.show()


# In[ ]:




