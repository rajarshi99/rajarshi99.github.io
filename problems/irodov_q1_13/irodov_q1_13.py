import numpy as np
import matplotlib.pyplot as plt

from numSol import numSol 

# Prob params
u = 3
v = 5
l = 10

# Analytical sol
T_final = l*v / (v*v - u*u)

# Solver param
dt = 0.01
n, r, theta = numSol(3, 5, 10, dt)
t = dt * np.arange(n)

plt.rcParams['font.size'] = 18
plt.rcParams['savefig.bbox'] = 'tight'

plt.plot(t, r)
plt.xlabel(r"$t$")
plt.ylabel(r"$r$")
plt.grid()
plt.axvline(T_final, ls="dashed")
plt.savefig("r_vs_t.png")
plt.close()

plt.plot(t, theta)
plt.xlabel(r"$t$")
plt.ylabel(r"$\theta$")
plt.yticks([0, np.pi/4, np.pi/2],
           [r"$0$", r"$\frac{\pi}{4}$", r"$\frac{\pi}{2}$"])
plt.grid()
plt.axvline(T_final, ls="dashed")
plt.savefig("theta_vs_t.png")
plt.close()
