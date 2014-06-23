# -*- coding: utf-8 -*-
"""
Created on Sat Jun 21 21:08:06 2014

@author: snashalk@tcd.ie
"""


def fib():
    a, b = 0, 1
    while 1:
        yield a
        a, b = b, a + b
x = fib()
y=[]
while x.next() < 4000000:
    y.append(x.next())
z=[]
for i in range(len(y)):
    if y[i]%2==0:
        z.append(y[i])
        
print sum(z)