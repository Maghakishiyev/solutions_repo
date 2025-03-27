import numpy as np
import matplotlib.pyplot as plt
import os
import imageio
import tempfile
from mpl_toolkits.mplot3d import Axes3D

image_dir = os.path.join('docs', '1 Physics', '2 Gravity', 'pics')
os.makedirs(image_dir, exist_ok=True)

G = 6.67430e-11  

celestial_bodies = {
    'Earth': {
        'mass': 5.972e24,  
        'radius': 6.371e6, 
        'color': 'blue',
        'escape_velocity': None,  
        'orbital_velocity_leo': None,  
    },
    'Moon': {
        'mass': 7.342e22,  
        'radius': 1.737e6, 
        'color': 'gray',
        'escape_velocity': None,
        'orbital_velocity_leo': None,
    },
    'Mars': {
        'mass': 6.39e23,  
        'radius': 3.389e6, 
        'color': 'red',
        'escape_velocity': None,
        'orbital_velocity_leo': None,
    },
    'Jupiter': {
        'mass': 1.898e27,  
        'radius': 6.9911e7,  
        'color': 'orange',
        'escape_velocity': None,
        'orbital_velocity_leo': None,
    },
    'Sun': {
        'mass': 1.989e30,  
        'radius': 6.957e8,  
        'color': 'yellow',
        'escape_velocity': None,
        'orbital_velocity_leo': None,
    },
    'Mercury': {
        'mass': 3.285e23,  
        'radius': 2.439e6,  
        'color': 'darkgray',
        'escape_velocity': None,
        'orbital_velocity_leo': None,
    },
    'Venus': {
        'mass': 4.867e24,  
        'radius': 6.051e6,  
        'color': 'gold',
        'escape_velocity': None,
        'orbital_velocity_leo': None,
    },
    'Saturn': {
        'mass': 5.683e26,  
        'radius': 5.8232e7,  
        'color': 'khaki',
        'escape_velocity': None,
        'orbital_velocity_leo': None,
    },
    'Uranus': {
        'mass': 8.681e25,  
        'radius': 2.5362e7,  
        'color': 'lightblue',
        'escape_velocity': None,
        'orbital_velocity_leo': None,
    },
    'Neptune': {
        'mass': 1.024e26,  
        'radius': 2.4622e7,  
        'color': 'darkblue',
        'escape_velocity': None,
        'orbital_velocity_leo': None,
    }
}

solar_system = {
    'Sun': {
        'mass': 1.989e30,  
        'radius': 6.957e8,  
    },
    'Earth': {
        'distance_from_sun': 1.496e11, 
    },
    'Jupiter': {
        'distance_from_sun': 7.785e11, 
    }
}

def calculate_first_cosmic_velocity(mass, radius):
    return np.sqrt(G * mass / radius)

def calculate_second_cosmic_velocity(mass, radius):
    return np.sqrt(2 * G * mass / radius)

def calculate_third_cosmic_velocity(distance_from_sun=solar_system['Earth']['distance_from_sun']):
    sun_mass = solar_system['Sun']['mass']
    return np.sqrt(2 * G * sun_mass / distance_from_sun)

for body, data in celestial_bodies.items():
    data['first_cosmic_velocity'] = calculate_first_cosmic_velocity(data['mass'], data['radius'])
    
    data['second_cosmic_velocity'] = calculate_second_cosmic_velocity(data['mass'], data['radius'])
    
    leo_altitude = 400e3  
    data['orbital_velocity_leo'] = calculate_first_cosmic_velocity(data['mass'], data['radius'] + leo_altitude)

earth_third_cosmic = calculate_third_cosmic_velocity(solar_system['Earth']['distance_from_sun'])
jupiter_third_cosmic = calculate_third_cosmic_velocity(solar_system['Jupiter']['distance_from_sun'])

plt.figure(figsize=(12, 8))
bodies = [body for body in celestial_bodies.keys() if body != 'Sun']
escape_velocities = [celestial_bodies[body]['second_cosmic_velocity'] / 1000 for body in bodies]  # Convert to km/s
colors = [celestial_bodies[body]['color'] for body in bodies]

bars = plt.bar(bodies, escape_velocities, color=colors)
plt.ylabel('Escape Velocity (km/s)', fontsize=12)
plt.title('Escape Velocities (Second Cosmic Velocity) for Different Celestial Bodies', fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.7)

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 0.5,
            f'{height:.1f}',
            ha='center', va='bottom', fontsize=10)

plt.savefig(os.path.join(image_dir, 'escape_velocities.png'), dpi=300, bbox_inches='tight')

plt.figure(figsize=(10, 6))

planets = ['Earth', 'Jupiter']
first_cosmic = [celestial_bodies['Earth']['first_cosmic_velocity'] / 1000, 
                celestial_bodies['Jupiter']['first_cosmic_velocity'] / 1000]  
second_cosmic = [celestial_bodies['Earth']['second_cosmic_velocity'] / 1000, 
                 celestial_bodies['Jupiter']['second_cosmic_velocity'] / 1000]  
third_cosmic = [earth_third_cosmic / 1000, jupiter_third_cosmic / 1000]  

bar_width = 0.25
r1 = np.arange(len(planets))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]

plt.bar(r1, first_cosmic, color='blue', width=bar_width, edgecolor='grey', label='First Cosmic Velocity')
plt.bar(r2, second_cosmic, color='green', width=bar_width, edgecolor='grey', label='Second Cosmic Velocity')
plt.bar(r3, third_cosmic, color='red', width=bar_width, edgecolor='grey', label='Third Cosmic Velocity')

plt.xlabel('Planet', fontsize=12)
plt.ylabel('Velocity (km/s)', fontsize=12)
plt.title('Comparison of Cosmic Velocities for Earth and Jupiter', fontsize=14)
plt.xticks([r + bar_width for r in range(len(planets))], planets)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

for i, v in enumerate(first_cosmic):
    plt.text(r1[i], v + 0.5, f'{v:.1f}', ha='center', va='bottom', fontsize=9)
for i, v in enumerate(second_cosmic):
    plt.text(r2[i], v + 0.5, f'{v:.1f}', ha='center', va='bottom', fontsize=9)
for i, v in enumerate(third_cosmic):
    plt.text(r3[i], v + 0.5, f'{v:.1f}', ha='center', va='bottom', fontsize=9)

plt.savefig(os.path.join(image_dir, 'cosmic_velocities_comparison.png'), dpi=300, bbox_inches='tight')

def create_trajectory_animation():
    with tempfile.TemporaryDirectory() as tmpdirname:
        fig, ax = plt.subplots(figsize=(10, 10))
        
        n_frames = 100
        frames_filenames = []
        
        planet = plt.scatter([], [], s=200, color='blue', label='Planet')
        orbital_trajectory = plt.Line2D([], [], color='green', lw=2, label='Orbital Trajectory (First Cosmic Velocity)')
        escape_trajectory = plt.Line2D([], [], color='red', lw=2, label='Escape Trajectory (Second Cosmic Velocity)')
        
        for i in range(n_frames):
            ax.clear()
            
            t = i * 0.1
            
            ax.scatter(0, 0, s=200, color='blue')
            
            theta = np.linspace(0, 2*np.pi, 100)
            orbit_radius = 1.0
            x_orbit = orbit_radius * np.cos(theta)
            y_orbit = orbit_radius * np.sin(theta)
            ax.plot(x_orbit, y_orbit, 'g--', alpha=0.5)
            
            angle = 2 * np.pi * i / n_frames
            x_orbital = orbit_radius * np.cos(angle)
            y_orbital = orbit_radius * np.sin(angle)
            
            ax.scatter(x_orbital, y_orbital, color='green', s=50, zorder=10)
            
            escape_radius = np.linspace(0, 3, 100)
            x_escape = escape_radius * np.cos(np.pi/4)
            y_escape = escape_radius * np.sin(np.pi/4)
            ax.plot(x_escape, y_escape, 'r--', alpha=0.5)
            
            escape_position = min(t, 3) 
            x_escape_current = escape_position * np.cos(np.pi/4)
            y_escape_current = escape_position * np.sin(np.pi/4)
            
            ax.scatter(x_escape_current, y_escape_current, color='red', s=50, zorder=10)
            
            ax.set_xlim(-3, 3)
            ax.set_ylim(-3, 3)
            ax.set_aspect('equal')
            ax.grid(True, linestyle='--', alpha=0.7)
            ax.set_xlabel('Distance (arbitrary units)', fontsize=12)
            ax.set_ylabel('Distance (arbitrary units)', fontsize=12)
            ax.set_title('Orbital vs. Escape Trajectories', fontsize=14)
            
            ax.legend(handles=[planet, orbital_trajectory, escape_trajectory], 
                     loc='upper right', bbox_to_anchor=(1.0, 1.0), framealpha=0.9)
            
            ax.text(0.02, 0.06, 'First Cosmic Velocity: Orbital motion (circular path)', 
                    transform=ax.transAxes, fontsize=10, verticalalignment='bottom',
                    bbox=dict(facecolor='white', alpha=0.9))
            ax.text(0.02, 0.01, 'Second Cosmic Velocity: Escape trajectory (hyperbolic path)', 
                    transform=ax.transAxes, fontsize=10, verticalalignment='bottom',
                    bbox=dict(facecolor='white', alpha=0.9))
            
            frame_filename = os.path.join(tmpdirname, f'frame_{i:03d}.png')
            plt.savefig(frame_filename, dpi=100, bbox_inches='tight')
            frames_filenames.append(frame_filename)
        
        with imageio.get_writer(os.path.join(image_dir, 'trajectory_comparison.gif'), mode='I', duration=0.1, loop=0) as writer:
            for frame_filename in frames_filenames:
                image = imageio.imread(frame_filename)
                writer.append_data(image)
        
        plt.savefig(os.path.join(image_dir, 'trajectory_comparison.png'), dpi=300, bbox_inches='tight')

def create_solar_system_escape_animation():
    with tempfile.TemporaryDirectory() as tmpdirname:
        fig = plt.figure(figsize=(12, 10))
        ax = fig.add_subplot(111, projection='3d')
        
        n_frames = 100
        frames_filenames = []
        
        sun_pos = np.array([0, 0, 0])
        
        earth_orbit_radius = 1.0
        theta = np.linspace(0, 2*np.pi, 100)
        earth_orbit_x = earth_orbit_radius * np.cos(theta)
        earth_orbit_y = earth_orbit_radius * np.sin(theta)
        earth_orbit_z = np.zeros_like(theta)
        
        spacecraft_start = np.array([earth_orbit_radius, 0, 0])
        spacecraft_direction = np.array([1, 1, 1])
        spacecraft_direction = spacecraft_direction / np.linalg.norm(spacecraft_direction)  # Normalize
        spacecraft_traj_length = 3.0
        spacecraft_traj = np.array([spacecraft_start + t * spacecraft_direction * spacecraft_traj_length 
                                   for t in np.linspace(0, 1, n_frames)])
        
        elev = 30
        azim = 45
        
        for i in range(n_frames):
            ax.clear()
            
            t = i / (n_frames - 1)
            
            ax.scatter(*sun_pos, color='yellow', s=300, label='Sun' if i == 0 else "")
            
            ax.plot(earth_orbit_x, earth_orbit_y, earth_orbit_z, 'b--', alpha=0.5)
            
            earth_angle = 2 * np.pi * i / n_frames
            earth_pos = np.array([earth_orbit_radius * np.cos(earth_angle), 
                                 earth_orbit_radius * np.sin(earth_angle), 
                                 0])
            ax.scatter(*earth_pos, color='blue', s=100, label='Earth' if i == 0 else "")
            
            spacecraft_pos = spacecraft_traj[i]
            ax.scatter(*spacecraft_pos, color='red', s=50, label='Spacecraft' if i == 0 else "")
            
            ax.plot(spacecraft_traj[:i+1, 0], spacecraft_traj[:i+1, 1], spacecraft_traj[:i+1, 2], 'r-')
            
            ax.set_xlim(-3, 3)
            ax.set_ylim(-3, 3)
            ax.set_zlim(-3, 3)
            
            ax.set_xlabel('X (arbitrary units)', fontsize=12, labelpad=10)
            ax.set_ylabel('Y (arbitrary units)', fontsize=12, labelpad=10)
            ax.set_zlabel('Z (arbitrary units)', fontsize=12, labelpad=10)
            
            ax.view_init(elev=elev, azim=azim)
            
            ax.set_title('Solar System Escape with Third Cosmic Velocity', fontsize=14)
            
            ax.text2D(0.05, 0.95, 'Third Cosmic Velocity: Escape from the Solar System', 
                     transform=ax.transAxes, fontsize=12,
                     bbox=dict(facecolor='white', alpha=0.9))
            
            if i == 0:
                ax.legend(loc='upper right', bbox_to_anchor=(1, 1), framealpha=0.9)
            
            frame_filename = os.path.join(tmpdirname, f'frame_{i:03d}.png')
            plt.savefig(frame_filename, dpi=100, bbox_inches='tight')
            frames_filenames.append(frame_filename)
        
        with imageio.get_writer(os.path.join(image_dir, 'solar_system_escape.gif'), mode='I', duration=0.1, loop=0) as writer:
            for frame_filename in frames_filenames:
                image = imageio.imread(frame_filename)
                writer.append_data(image)
        
        plt.savefig(os.path.join(image_dir, 'solar_system_escape.png'), dpi=300, bbox_inches='tight')

def plot_escape_velocity_vs_distance():
    bodies_to_plot = ['Earth', 'Mars', 'Jupiter']
    
    plt.figure(figsize=(10, 6))
    
    for body in bodies_to_plot:
        mass = celestial_bodies[body]['mass']
        radius = celestial_bodies[body]['radius']
        color = celestial_bodies[body]['color']
        
        distances = np.linspace(radius, radius * 5, 100)  
        escape_velocities = [calculate_second_cosmic_velocity(mass, r) / 1000 for r in distances]  
        
        plt.plot(distances / radius, escape_velocities, color=color, label=f'{body}')
    
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.xlabel('Distance from Center (Planet Radii)', fontsize=12)
    plt.ylabel('Escape Velocity (km/s)', fontsize=12)
    plt.title('Escape Velocity vs. Distance from Celestial Body Center', fontsize=14)
    plt.legend()
    plt.savefig(os.path.join(image_dir, 'escape_velocity_vs_distance.png'), dpi=300, bbox_inches='tight')

create_trajectory_animation()
create_solar_system_escape_animation()
plot_escape_velocity_vs_distance()

print(f"Images and animations saved to {image_dir}")

print("\nCosmic Velocities (km/s):")
print("-" * 80)
print(f"{'Body':<10} {'First Cosmic':<15} {'Second Cosmic':<15} {'Orbital (LEO)':<15}")
print("-" * 80)

for body, data in celestial_bodies.items():
    if body in ['Earth', 'Mars', 'Jupiter', 'Moon']:
        first = data['first_cosmic_velocity'] / 1000
        second = data['second_cosmic_velocity'] / 1000
        leo = data['orbital_velocity_leo'] / 1000
        print(f"{body:<10} {first:<15.2f} {second:<15.2f} {leo:<15.2f}")

print("\nThird Cosmic Velocity (Solar System Escape):")
print(f"From Earth's orbit: {earth_third_cosmic/1000:.2f} km/s")
print(f"From Jupiter's orbit: {jupiter_third_cosmic/1000:.2f} km/s")
