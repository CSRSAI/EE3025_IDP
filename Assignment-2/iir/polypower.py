import numpy as np
#If using termux
import subprocess
import shlex
#end if
def polypower(v,N):
    x=np.array([1])
    if N>0:
        for i in range(1,N+1):
            x = np.convolve(x,v)
    return x
