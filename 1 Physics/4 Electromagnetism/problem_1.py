import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants (modifiable for parameter exploration)
q = 1.6e-19  # Charge of the particle (C)
m = 9.11e-31  # Mass of the particle (kg)
B = np.array([0, 0, 1])  # Uniform magnetic field (T)
E = np.array([0, 0, 0])  # Electric field (V/m)
v0 = np.array([1e6, 0, 0])  # Initial velocity (m/s)
r0 = np.array([0, 0, 0])  # Initial position (m)
dt = 1e-10  # Time step (s)
n_steps = 1000  # Number of time steps

def lorentz_force(q, v, E, B):
    """Computes the Lorentz force."""
    return q * (E + np.cross(v, B))

def simulate_motion(q, m, E, B, v0, r0, dt, n_steps):
    """Simulates the motion of a charged particle in E and B fields."""
    r = np.zeros((n_steps, 3))
    v = np.zeros((n_steps, 3))
    r[0] = r0
    v[0] = v0

    for i in range(1, n_steps):
        F = lorentz_force(q, v[i-1], E, B)
        a = F / m
        v[i] = v[i-1] + a * dt
        r[i] = r[i-1] + v[i] * dt

    return r, v

# Run simulation
r, v = simulate_motion(q, m, E, B, v0, r0, dt, n_steps)

# Visualization
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot(r[:, 0], r[:, 1], r[:, 2], label='Particle Trajectory')
ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_zlabel('Z (m)')
ax.set_title('Charged Particle Motion in a Magnetic Field')
ax.legend()
plt.show()