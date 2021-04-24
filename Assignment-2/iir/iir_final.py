import numpy as np
from lp_stable_cheb import *
from lpbp import *
from bilin import * 
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if

epsilon = 0.4
p,G_lp = lp_stable_cheb(epsilon,N)
Omega_L = np.arange(0,2.01,0.01)
H_analog_lp = G_lp*np.abs(1/np.polyval(p,1j*Omega_L))
plt.plot(Omega_L,H_analog_lp);
plt.xlabel('\Omega')
plt.ylabel('|H_{a,LP}(j\Omega)|')
plt.show()
num,den,G_bp = lpbp(p,Omega_0,B,Omega_p1)
Omega = np.arange(-0.65,0.66,0.01)
plt.plot(Omega,H_analog_bp);
plt.xlabel('\Omega')
plt.ylabel('|H_{a,BP}(j\Omega)|')
plt.show()
plt.savefig('../figs/iir/BP_analog.eps')
plt.savefig('../figs/iir/BP_analog.pdf')
H_analog_bp = G_bp*np.abs(np.polyval(num,1j*Omega)/np.polyval(den,1j*Omega))
dignum,digden,G = bilin(den,omega_p1)
omega = np.arange(-2*np.pi/5,2*np.pi/5+np.pi/1000,np.pi/1000)
H_dig_bp = G*np.abs(np.polyval(dignum,np.exp(-1j*omega))/np.polyval(digden,np.exp(-1j*omega)))
plt.plot(omega/np.pi,H_dig_bp)
plt.xlabel('\omega/\pi')
plt.ylabel('|H_{d,BP}(\omega)|')
plt.show()
iir_num = G*dignum
iir_den = digden

np.savetxt('dignum.dat',dignum,delimiter=',')
np.savetxt('G.dat',G,delimiter=',')
np.savetxt('digden.dat',digden,delimiter=',')
np.savetxt('iir_num.dat',iir_num,delimiter=',')
