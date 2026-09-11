import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

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

# Create a combined figure with 1 row and 2 columns
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.5))

# ---------------- PLOT (a) ----------------
contour = ax1.contourf(X, Y, T, levels=20, cmap='viridis')

# Use make_axes_locatable to stop the colorbar from shrinking/warping the main axes
divider = make_axes_locatable(ax1)
cax = divider.append_axes("right", size="5%", pad=0.15)
fig.colorbar(contour, cax=cax)

# Add contour lines for better visibility
contour_lines = ax1.contour(X, Y, T, levels=10, colors='white', alpha=0.5, linewidths=0.8)
ax1.clabel(contour_lines, inline=True, fmt='%.1f')

ax1.set_title('(a) Contours of Collision Time T')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.grid(True, linestyle='--', alpha=0.3)
ax1.axhline(0, color='black', linewidth=0.5)
ax1.axvline(0, color='black', linewidth=0.5)
ax1.set_aspect('equal', adjustable='box')

# ---------------- PLOT (b) ----------------
theta_vals = np.linspace(0, np.pi, 500)
A_vals = A(theta_vals)
ax2.plot(theta_vals, A_vals)
ax2.set_ylabel('A')
ax2.set_xlabel(r"$\theta$")
ax2.set_xticks([0, np.pi/2, np.pi])
ax2.set_xticklabels([r"$0$", r"$\frac{\pi}{2}$", r"$\pi$"])
ax2.set_title('(b) Angular factor A')
ax2.grid(True)

# Adjust layout and save combined image
plt.tight_layout()
plt.savefig("TA.png", dpi=300)
plt.close()
