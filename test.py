from __future__ import division

import numpy as np
import scipy as scp
import pylab as pyl
import matplotlib.pyplot as plt

from nt_toolbox.general import *
from nt_toolbox.signal import *

#%matplotlib inline
#%load_ext autoreload
#%autoreload 2

n = 128
c = [100,200]
f0 = load_image("bruit.png")
f0 = rescale(f0[c[0]-n//2:c[0]+n//2, c[1]-n//2:c[1]+n//2])


plt.figure(figsize = (5,5))
imageplot(f0)

sigma = .04

from numpy import random
f = f0 + sigma*random.standard_normal((n,n))

plt.figure(figsize = (5,5))
imageplot(clamp(f))

w = 3
w1 = 2*w + 1

[X,Y,dX,dY] = np.meshgrid(np.arange(1,n+1),np.arange(1,n+1),np.arange(-w,w+1),np.arange(-w,w+1))
X = X + dX
Y = Y + dY

X[X < 1] = 2-X[X < 1]
Y[Y < 1] = 2-Y[Y < 1]
X[X > n] = 2*n-X[X > n]
Y[Y > n] = 2*n-Y[Y > n]

I = (X - 1) + (Y - 1) * n
for i in range(n // w):
    for j in range(n // w):
        I[i, j] = np.transpose(I[i, j])

patch = lambda f: np.ravel(f)[I]

P = patch(f)

from numpy import random

plt.figure(figsize = (5,5))

for i in range(16):
    x = random.randint(n)
    y = random.randint(n)
    imageplot(P[x, y], '', [4, 4, i+1])

d = 25

resh = lambda P: np.transpose((np.reshape(P, (n*n,w1*w1), order="F")))

remove_mean = lambda Q: Q - np.tile(np.mean(Q,0),(w1*w1,1))

P1 = remove_mean(resh(P))
C = np.dot(P1,np.transpose(P1))

from numpy import linalg

[D,V] = linalg.eig(C)
D = np.sort(D)[::-1]
I = np.argsort(D)[::-1]
V = V[I,:]


plt.plot(D, linewidth = 2)
plt.ylim(0,max(D))
plt.show()

plt.figure(figsize = (5,5))
for i in range(16):
    imageplot(abs(np.reshape(V[:,i], (w1,w1))), '', [4, 4, i+1])

iresh = lambda Q: np.reshape(np.transpose(Q),(n,n,d),order="F")
descriptor = lambda f: iresh(np.dot(np.transpose(V[: ,:d]),remove_mean(resh(P))))


H = descriptor(f)

distance = lambda i: np.sum((H - np.tile(H[i[0],i[1],:], (n,n,1)))**2, 2)/(w1*w1)

normalize = lambda K: K/np.sum(K)
kernel = lambda i,tau: normalize(np.exp(-distance(i)/(2*tau**2)))

tau = .05
i = [83,72]
D = distance(i)
K = kernel(i, tau)

plt.figure(figsize = (10,10))
imageplot(D, 'D', [1, 2, 1])
imageplot(K, 'K', [1, 2, 2])


q = 14

selection = lambda i: np.array((clamp(np.arange(i[0]-q,i[0] + q + 1), 0, n-1), clamp(np.arange(i[1]-q,i[1] + q + 1), 0, n-1)))

def distance_0(i,sel):
    H1 = (H[sel[0],:,:])
    H2 = (H1[:,sel[1],:])
    return np.sum((H2 - np.tile(H[i[0],i[1],:],(len(sel[0]),len(sel[1]),1)))**2,2)/w1*w1

distance = lambda i: distance_0(i, selection(i))
kernel = lambda i, tau: normalize(np.exp(-distance(i)/ (2*tau**2)))

D = distance(i)
K = kernel(i, tau)

plt.figure(figsize = (10,10))

imageplot(D, 'D', [1, 2, 1])
imageplot(K, 'K', [1, 2, 2])


def NLval_0(K,sel):
    f_temp = f[sel[0],:]
    return np.sum(K*f_temp[:, sel[1]])

NLval = lambda i, tau: NLval_0(kernel(i, tau), selection(i))


[Y, X] = np.meshgrid(np.arange(0,n),np.arange(0,n))

def arrayfun(f,X,Y):
    n = len(X)
    p = len(Y)
    R = np.zeros([n,p])
    for k in range(n):
        for l in range(p):
            R[k,l] = f(k,l)
    return R

NLmeans = lambda tau: arrayfun(lambda i1, i2: NLval([i1,i2], tau), X, Y)

tau = .03

plt.figure(figsize = (5,5))
imageplot(NLmeans(tau))