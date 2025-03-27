import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import os
import imageio.v2 as imageio
import tempfile

image_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'docs', '1 Physics', '2 Gravity', 'pics')
os.makedirs(image_dir, exist_ok=True)

G = 6.67430e-11  
M_earth = 5.972e24  
M_sun = 1.989e30  

def calculate_period(radius, central_mass):
    return 2 * np.pi * np.sqrt(radius**3 / (G * central_mass))

def simulate_circular_orbit(radius, central_mass, num_points=1000):
    period = calculate_period(radius, central_mass)
    
    velocity = 2 * np.pi * radius / period
    
    theta = np.linspace(0, 2*np.pi, num_points)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    
    return x, y, period, velocity

planet_data = {
    'Mercury': {'radius': 5.79e10, 'color': 'gray'},
    'Venus': {'radius': 1.08e11, 'color': 'orange'},
    'Earth': {'radius': 1.496e11, 'color': 'blue'},
    'Mars': {'radius': 2.28e11, 'color': 'red'},
    'Jupiter': {'radius': 7.78e11, 'color': 'brown'},
    'Saturn': {'radius': 1.43e12, 'color': 'gold'},
    'Uranus': {'radius': 2.87e12, 'color': 'lightblue'},
    'Neptune': {'radius': 4.5e12, 'color': 'darkblue'}
}

plt.figure(figsize=(12, 12))

plt.scatter(0, 0, s=200, color='yellow', label='Sun')

for planet, data in planet_data.items():
    x, y, period, _ = simulate_circular_orbit(data['radius'], M_sun)
    plt.plot(x, y, color=data['color'], label=f'{planet} (T = {period/86400/365.25:.2f} years)')

plt.grid(True, linestyle='--', alpha=0.7)
plt.xlabel('Distance (m)')
plt.ylabel('Distance (m)')
plt.title('Orbits of Planets in the Solar System')
plt.axis('equal')
plt.legend(loc='upper right')
plt.savefig(os.path.join(image_dir, 'solar_system_orbits.png'), dpi=300, bbox_inches='tight')

radii = np.linspace(0.1e11, 5e12, 100)
periods = [calculate_period(r, M_sun) for r in radii]
periods_years = np.array(periods) / (86400 * 365.25)  
radii_au = np.array(radii) / 1.496e11  

periods_squared = periods_years**2
radii_cubed = radii_au**3

plt.figure(figsize=(12, 8))

plt.plot(radii_cubed, periods_squared, 'b-', linewidth=2)

planet_positions = {}

for planet, data in planet_data.items():
    radius_au_cubed = (data['radius']/1.496e11)**3
    period_years_squared = (calculate_period(data['radius'], M_sun)/86400/365.25)**2
    plt.scatter(radius_au_cubed, period_years_squared, color=data['color'], s=80)
    planet_positions[planet] = (radius_au_cubed, period_years_squared)

label_offsets = {
    'Mercury': (10, 10),
    'Venus': (15, -25),
    'Earth': (-50, 20),
    'Mars': (20, 30),
    'Jupiter': (15, -30),
    'Saturn': (-70, -20),
    'Uranus': (20, 25),
    'Neptune': (-80, -30)
}

for planet, (x, y) in planet_positions.items():
    plt.annotate(planet, 
                xy=(x, y),
                xytext=label_offsets[planet], 
                textcoords='offset points',
                arrowprops=dict(arrowstyle='->', lw=1.5, color=planet_data[planet]['color']),
                fontsize=12,
                fontweight='bold')

plt.grid(True)
plt.xlabel('Orbital Radius Cubed (AU³)', fontsize=12)
plt.ylabel('Orbital Period Squared (years²)', fontsize=12)
plt.title('Verification of Kepler’s Third Law: T² ∝ r³', fontsize=14)

plt.text(0.05, 0.95, 'T² = (4π²/GM) × r³', transform=plt.gca().transAxes, 
        fontsize=12, verticalalignment='top', 
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

plt.xlim(-5, max(radii_cubed) * 1.1)
plt.ylim(-100, max(periods_squared) * 1.1)

plt.tight_layout()
plt.savefig(os.path.join(image_dir, 'keplers_third_law.png'), dpi=300, bbox_inches='tight')

plt.figure(figsize=(10, 6))
plt.loglog(radii_au, periods_years, 'b-', linewidth=2)

for planet, data in planet_data.items():
    period_years = calculate_period(data['radius'], M_sun) / (86400 * 365.25)
    radius_au = data['radius'] / 1.496e11
    plt.scatter(radius_au, period_years, color=data['color'])
    plt.annotate(planet, (radius_au, period_years), xytext=(5, 5), textcoords='offset points')

plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.xlabel('Orbital Radius (AU) - Log Scale')
plt.ylabel('Orbital Period (years) - Log Scale')
plt.title('Kepler’s Third Law: Log-Log Plot')
plt.savefig(os.path.join(image_dir, 'keplers_law_loglog.png'), dpi=300, bbox_inches='tight')

plt.figure(figsize=(10, 10))

plt.scatter(0, 0, s=200, color='blue', label='Central Body')

orbit_radius = 1.0
theta = np.linspace(0, 2*np.pi, 100)
x_orbit = orbit_radius * np.cos(theta)
y_orbit = orbit_radius * np.sin(theta)
plt.plot(x_orbit, y_orbit, 'k--', alpha=0.3)

angles = [0, np.pi/4, np.pi/2, 3*np.pi/4]
colors = ['red', 'green', 'purple', 'orange']

for i, angle in enumerate(angles):
    x = orbit_radius * np.cos(angle)
    y = orbit_radius * np.sin(angle)
    
    vx = -np.sin(angle) * 0.3
    vy = np.cos(angle) * 0.3
    
    ax_val = -np.cos(angle) * 0.3
    ay_val = -np.sin(angle) * 0.3
    
    plt.scatter(x, y, color=colors[i], s=100, zorder=10)
    
    plt.arrow(0, 0, x, y, color=colors[i], width=0.01, length_includes_head=True, alpha=0.7, label='Position' if i == 0 else '')
    
    plt.arrow(x, y, vx, vy, color='green', width=0.01, length_includes_head=True, alpha=0.7, label='Velocity' if i == 0 else '')
    
    plt.arrow(x, y, ax_val, ay_val, color='blue', width=0.01, length_includes_head=True, alpha=0.7, label='Acceleration' if i == 0 else '')

plt.grid(True, linestyle='--', alpha=0.7)
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.axis('equal')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Circular Orbit Dynamics')
plt.legend(loc='upper right')
plt.savefig(os.path.join(image_dir, 'orbit_dynamics.png'), dpi=300, bbox_inches='tight')

def create_orbit_animation():
    with tempfile.TemporaryDirectory() as tmpdirname:
        fig, ax = plt.subplots(figsize=(10, 10))
        
        n_frames = 50
        frames_filenames = []
        
        central_body = plt.scatter([], [], s=200, color='blue', label='Central Body')
        satellite = plt.scatter([], [], color='red', s=100, label='Satellite')
        position = plt.Line2D([], [], color='red', lw=2, label='Position')
        velocity = plt.Line2D([], [], color='green', lw=2, label='Velocity')
        acceleration = plt.Line2D([], [], color='blue', lw=2, label='Acceleration')
        
        for i in range(n_frames):
            ax.clear()
            
            angle = 2 * np.pi * i / n_frames
            
            ax.scatter(0, 0, s=200, color='blue')
            
            orbit_radius = 1.0
            theta = np.linspace(0, 2*np.pi, 100)
            x_orbit = orbit_radius * np.cos(theta)
            y_orbit = orbit_radius * np.sin(theta)
            ax.plot(x_orbit, y_orbit, 'k--', alpha=0.3)
            
            x = orbit_radius * np.cos(angle)
            y = orbit_radius * np.sin(angle)
            
            vx = -np.sin(angle) * 0.3
            vy = np.cos(angle) * 0.3
            
            ax_val = -np.cos(angle) * 0.3
            ay_val = -np.sin(angle) * 0.3
            
            ax.scatter(x, y, color='red', s=100, zorder=10)
            
            ax.arrow(0, 0, x, y, color='red', width=0.01, length_includes_head=True, 
                     alpha=0.7)
            
            ax.arrow(x, y, vx, vy, color='green', width=0.01, length_includes_head=True, 
                     alpha=0.7)
            
            ax.arrow(x, y, ax_val, ay_val, color='blue', width=0.01, length_includes_head=True, 
                     alpha=0.7)
            
            ax.set_xlim(-1.5, 1.5)
            ax.set_ylim(-1.5, 1.5)
            ax.set_aspect('equal')
            ax.grid(True, linestyle='--', alpha=0.7)
            ax.set_xlabel('x', fontsize=12)
            ax.set_ylabel('y', fontsize=12)
            ax.set_title('Circular Orbit Dynamics', fontsize=14)
            
            ax.legend(handles=[central_body, satellite, position, velocity, acceleration], 
                      loc='upper right')
            
            frame_filename = os.path.join(tmpdirname, f'frame_{i:03d}.png')
            plt.savefig(frame_filename, dpi=100, bbox_inches='tight')
            frames_filenames.append(frame_filename)
        
        with imageio.get_writer(os.path.join(image_dir, 'orbit_dynamics.gif'), mode='I', duration=0.1, loop=0) as writer:
            for frame_filename in frames_filenames:
                image = imageio.imread(frame_filename)
                writer.append_data(image)
        
        plt.savefig(os.path.join(image_dir, 'orbit_dynamics.png'), dpi=300, bbox_inches='tight')

masses = [1e24, 5e24, 1e25, 5e25, 1e26]
radii = np.linspace(1e7, 1e8, 100)

plt.figure(figsize=(10, 6))

for mass in masses:
    periods = [calculate_period(r, mass) for r in radii]
    plt.plot(radii/1000, np.array(periods)/3600, label=f'Mass = {mass:.1e} kg')

plt.grid(True)
plt.xlabel('Orbital Radius (km)')
plt.ylabel('Orbital Period (hours)')
plt.title('Effect of Central Mass on Orbital Period')
plt.legend()
plt.savefig(os.path.join(image_dir, 'different_masses.png'), dpi=300, bbox_inches='tight')

M_moon = 7.342e22  
earth_moon_distance = 3.844e8  

barycenter_distance = earth_moon_distance * M_moon / (M_earth + M_moon)

earth_orbit_radius = barycenter_distance
earth_x, earth_y, _, _ = simulate_circular_orbit(earth_orbit_radius, 1, num_points=100)

moon_orbit_radius = earth_moon_distance - barycenter_distance
moon_x, moon_y, _, _ = simulate_circular_orbit(moon_orbit_radius, 1, num_points=100)

earth_x = earth_x - barycenter_distance
moon_x = moon_x + (earth_moon_distance - barycenter_distance)

plt.figure(figsize=(10, 8))
plt.plot(earth_x, earth_y, 'b-', label='Earth')
plt.plot(moon_x, moon_y, 'gray', label='Moon')
plt.scatter(0, 0, c='k', s=20, label='Barycenter')
plt.scatter(earth_x[0], earth_y[0], c='b', s=100)
plt.scatter(moon_x[0], moon_y[0], c='gray', s=30)

for i in range(0, 100, 10):
    plt.plot([earth_x[i], moon_x[i]], [earth_y[i], moon_y[i]], 'k--', alpha=0.3)

plt.grid(True)
plt.axis('equal')
plt.xlabel('Distance (m)')
plt.ylabel('Distance (m)')
plt.title('Earth-Moon System Orbiting Around Common Barycenter')
plt.legend()
plt.savefig(os.path.join(image_dir, 'earth_moon_system_actual.png'), dpi=300, bbox_inches='tight')

def create_earth_moon_animation():
    with tempfile.TemporaryDirectory() as tmpdirname:
        fig, ax = plt.subplots(figsize=(10, 10))
        
        n_frames = 50
        frames_filenames = []
        
        earth_dot = plt.scatter([], [], s=200, color='blue', label='Earth')
        moon_dot = plt.scatter([], [], s=100, color='gray', label='Moon')
        barycenter_dot = plt.scatter([], [], s=30, color='black', label='Barycenter')
        
        visualization_earth_radius = 0.3  
        visualization_moon_radius = 1.0  
        
        for i in range(n_frames):
            ax.clear()
            
            angle = 2 * np.pi * i / n_frames
            
            earth_x = visualization_earth_radius * np.cos(angle)
            earth_y = visualization_earth_radius * np.sin(angle)
            
            moon_x = visualization_moon_radius * np.cos(angle + np.pi)
            moon_y = visualization_moon_radius * np.sin(angle + np.pi)
            
            theta = np.linspace(0, 2*np.pi, 100)
            earth_path_x = visualization_earth_radius * np.cos(theta)
            earth_path_y = visualization_earth_radius * np.sin(theta)
            ax.plot(earth_path_x, earth_path_y, 'b--', alpha=0.5)
            
            moon_path_x = visualization_moon_radius * np.cos(theta + np.pi)
            moon_path_y = visualization_moon_radius * np.sin(theta + np.pi)
            ax.plot(moon_path_x, moon_path_y, 'gray', linestyle='--', alpha=0.5)
            
            ax.scatter(earth_x, earth_y, s=200, color='blue')
            ax.scatter(moon_x, moon_y, s=80, color='gray')
            
            ax.scatter(0, 0, s=30, color='black')
            
            ax.plot([earth_x, moon_x], [earth_y, moon_y], 'k-', alpha=0.7)
            
            ax.set_xlim(-1.5, 1.5)
            ax.set_ylim(-1.5, 1.5)
            ax.set_aspect('equal')
            ax.grid(True, linestyle='--', alpha=0.7)
            ax.set_xlabel('Distance (arbitrary units)', fontsize=12)
            ax.set_ylabel('Distance (arbitrary units)', fontsize=12)
            ax.set_title('Earth-Moon System Orbiting Around Common Barycenter\n(Not to scale - for educational purposes only)', fontsize=14)
            
            ax.legend(handles=[earth_dot, moon_dot, barycenter_dot], loc='upper right')
            
            ax.text(0.02, 0.02, 'Note: Visualization not to actual scale', 
                    transform=ax.transAxes, fontsize=10, 
                    bbox=dict(facecolor='white', alpha=0.7))
            
            frame_filename = os.path.join(tmpdirname, f'frame_{i:03d}.png')
            plt.savefig(frame_filename, dpi=100, bbox_inches='tight')
            frames_filenames.append(frame_filename)
        
        with imageio.get_writer(os.path.join(image_dir, 'earth_moon_system.gif'), mode='I', duration=0.1, loop=0) as writer:
            for frame_filename in frames_filenames:
                image = imageio.imread(frame_filename)
                writer.append_data(image)
        
        plt.savefig(os.path.join(image_dir, 'earth_moon_system.png'), dpi=300, bbox_inches='tight')

# Run the animation functions
create_orbit_animation()
create_earth_moon_animation()

print(f"Images saved to {image_dir}")
