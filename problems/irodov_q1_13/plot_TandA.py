import numpy as np
import matplotlib.pyplot as plt

# Parameters
v = 5.0
u = 3.0

def A(theta):
    ratio = u / v
    return (1 / v) * (1 + ratio * np.cos(theta)) / (1 - ratio**2)

x = np.linspace(-10, 10, 400)
y = np.linspace(-10, 10, 400)
X, Y = np.meshgrid(x, y)

# Convert Cartesian meshgrid (X, Y) to polar coordinates (R, Theta)
R = np.sqrt(X**2 + Y**2)
Theta = np.arctan2(Y, -X)

# Calculate time to collision T(r, theta) = r * A(theta)
T = R * A(Theta)
# Plotting the contours
plt.figure(figsize=(6, 6))
contour = plt.contourf(X, Y, T, levels=20, cmap='viridis')
plt.colorbar(contour)

# Add contour lines for better visibility
contour_lines = plt.contour(X, Y, T, levels=10, colors='white', alpha=0.5, linewidths=0.8)
plt.clabel(contour_lines, inline=True, fmt='%.1f')

plt.title(f'(a) Contours of Time T for v = {v}, u = {u}')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True, linestyle='--', alpha=0.3)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.gca().set_aspect('equal', adjustable='box')

plt.savefig("plotT.png")
plt.close()
plt.cla()

plt.figure(figsize=(6, 5.5))
theta_vals = np.linspace(0, np.pi, 500)
A_vals = A(theta_vals)
plt.plot(theta_vals, A_vals)
plt.xlabel('theta')
plt.ylabel('A')
plt.xlabel(r"$\theta$")
plt.xticks([0, np.pi/2, np.pi],
           [r"$0$", r"$\frac{\pi}{3}$", r"$\pi$"])
plt.title(f'(b) Angular factor A for v = {v}, u = {u}')
plt.grid()
plt.tight_layout()
plt.savefig("plotA.png")
plt.close()
