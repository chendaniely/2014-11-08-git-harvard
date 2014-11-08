import numpy as np
import matplotlib.pyplot
import pylab as pl

T_star = 5000
pi = 3.141592654
H = 1
sfb = 1

def dlnh_dlnr(h0, h1, r0, r1):
	val = (np.ln(h1) - np.ln(h0))/(np.ln(r1)-np.ln(r0))
	return val

def mu(T0, T1, r0, r1):
	h0 = h(T0, r0)
	h1 = h(T0, r1)
	mu = h0/(2*r0)*(dlnh_dlnr(h0, h1, r0, r1) - 1)
	return mu

def h(T, r):
	h = H*T^(0.5)*r^(1.5)
	return h

def Firr(T0, T1, r0, r1):
	Firr = sfb*T_star^4*mu(T0, T1, r0, r1)/r0^2
	return Firr

step=10
init_T = 1
init_h = 1

r_grid = np.arange(0,200,step)

T_grid = np.arange(0,200,step)
T_grid[0] = init_T

h_grid = np.arange(0,1,step)
h_grid[0] = init_h

for i, r in enumerate(r_grid[:-1]):
	T_grid[i+1]=dx1dt*step+x1_grid[i]

pl.show()