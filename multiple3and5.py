"""
Muliples of three and 5 sum below 1000
see eulerproject.com


author: snashalk@tcd.ie
"""
import numpy as np

x = np.arange(1,1000,1)
threey = []
fivey = []
for i in range(999):
    if int(x[i])%5==0:
        #print x[i]
        fivey.append(x[i])
print sum(fivey)

for i in range(999):
    if int(x[i])%3==0:
        #print x[i]
        threey.append(x[i])
print sum(threey)

