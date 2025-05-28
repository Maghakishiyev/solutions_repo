import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import os
import imageio.v2 as imageio
import tempfile

# Get the correct path to the images directory
script_dir = os.path.dirname(os.path.abspath(__file__))
repo_root = os.path.dirname(script_dir)
image_dir = os.path.join(repo_root, 'docs', '1 Physics', '2 Gravity', 'pics')
os.makedirs(image_dir, exist_ok=True)

# Physical constants
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
M_earth = 5.972e24  # Mass of Earth (kg)
M_sun = 1.989e30  # Mass of Sun (kg)
AU = 1.496e11  # Astronomical Unit (m)

def calculate_period(radius, central_mass):
    """Calculate orbital period using Kepler's Third Law"""
    return 2 * np.pi * np.sqrt(radius**3 / (G * central_mass))

def simulate_circular_orbit(radius, central_mass, num_points=1000):
    """Simulate a circular orbit and return position coordinates"""
    period = calculate_period(radius, central_mass)
    velocity = 2 * np.pi * radius / period
    
    theta = np.linspace(0, 2*np.pi, num_points)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    
    return x, y, period, velocity

def generate_main_plot():
    """Generate the main plot referenced in the markdown as problem1.png"""
    # Create the Kepler's Third Law verification plot
    orbit_radii = np.linspace(0.1, 10, 100) * AU  # 0.1 to 10 AU
    orbit_periods = []
    
    for radius in orbit_radii:
        period = calculate_period(radius, M_sun)
        orbit_periods.append(period / (60 * 60 * 24 * 365.25))  # Convert to years
    
    orbit_periods = np.array(orbit_periods)
    orbit_radii_au = orbit_radii / AU  # Convert to AU
    
    # Plot T^2 vs R^3 to verify linear relationship
    plt.figure(figsize=(10, 6))
    plt.plot(orbit_radii_au**3, orbit_periods**2, 'b-', linewidth=2, label="Kepler's Third Law")
    plt.xlabel('Orbital Radius Cubed (AU³)')
    plt.ylabel('Orbital Period Squared (years²)')
    plt.title('Verification of Kepler\'s Third Law: T² ∝ R³')
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    # Add theoretical annotation
    plt.text(0.05, 0.95, 'T² = (4π²/GM) × R³\nLinear relationship confirms Kepler\'s Law', 
             transform=plt.gca().transAxes, verticalalignment='top',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    
    plt.tight_layout()
    plt.savefig(os.path.join(image_dir, 'problem1.png'), dpi=300, bbox_inches='tight')
    plt.close()

def run_comprehensive_analysis():
    """Run comprehensive orbital mechanics analysis"""
    # Planet data for solar system analysis
    planet_data = {
        'Mercury': {'radius': 0.387 * AU, 'color': 'gray'},
        'Venus': {'radius': 0.723 * AU, 'color': 'orange'},
        'Earth': {'radius': 1.000 * AU, 'color': 'blue'},
        'Mars': {'radius': 1.524 * AU, 'color': 'red'},
        'Jupiter': {'radius': 5.203 * AU, 'color': 'brown'},
        'Saturn': {'radius': 9.537 * AU, 'color': 'gold'},
        'Uranus': {'radius': 19.191 * AU, 'color': 'lightblue'},
        'Neptune': {'radius': 30.069 * AU, 'color': 'darkblue'}
    }

    # 1. Solar system orbits visualization
    plt.figure(figsize=(14, 14))
    
    plt.scatter(0, 0, s=300, color='yellow', label='Sun', edgecolors='orange', linewidth=2)
    
    for planet, data in planet_data.items():
        x, y, period, _ = simulate_circular_orbit(data['radius'], M_sun)
        plt.plot(x/AU, y/AU, color=data['color'], linewidth=2, 
                label=f'{planet} (T = {period/86400/365.25:.2f} years)')
    
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.xlabel('Distance (AU)')
    plt.ylabel('Distance (AU)')
    plt.title('Orbits of Planets in the Solar System')
    plt.axis('equal')
    plt.legend(loc='upper right', bbox_to_anchor=(1.15, 1))
    plt.tight_layout()
    plt.savefig(os.path.join(image_dir, 'solar_system_orbits.png'), dpi=300, bbox_inches='tight')
    plt.close()

    # 2. Detailed Kepler's Third Law verification with planets
    radii = np.linspace(0.1, 40, 200) * AU
    periods = [calculate_period(r, M_sun) for r in radii]
    periods_years = np.array(periods) / (86400 * 365.25)  
    radii_au = np.array(radii) / AU

    periods_squared = periods_years**2
    radii_cubed = radii_au**3

    plt.figure(figsize=(12, 8))
    plt.plot(radii_cubed, periods_squared, 'b-', linewidth=2, alpha=0.7, label='Theoretical curve')

    planet_positions = {}
    for planet, data in planet_data.items():
        radius_au_cubed = (data['radius']/AU)**3
        period_years_squared = (calculate_period(data['radius'], M_sun)/86400/365.25)**2
        plt.scatter(radius_au_cubed, period_years_squared, color=data['color'], s=100, 
                   edgecolors='black', linewidth=1, zorder=10)
        planet_positions[planet] = (radius_au_cubed, period_years_squared)

    # Label planets with arrows
    label_offsets = {
        'Mercury': (20, 20),
        'Venus': (30, -40),
        'Earth': (-80, 30),
        'Mars': (40, 40),
        'Jupiter': (30, -50),
        'Saturn': (-120, -30),
        'Uranus': (40, 50),
        'Neptune': (-150, -50)
    }

    for planet, (x, y) in planet_positions.items():
        plt.annotate(planet, 
                    xy=(x, y),
                    xytext=label_offsets[planet], 
                    textcoords='offset points',
                    arrowprops=dict(arrowstyle='->', lw=2, color=planet_data[planet]['color']),
                    fontsize=12,
                    fontweight='bold',
                    bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8))

    plt.grid(True, alpha=0.3)
    plt.xlabel('Orbital Radius Cubed (AU³)', fontsize=14)
    plt.ylabel('Orbital Period Squared (years²)', fontsize=14)
    plt.title('Verification of Kepler\'s Third Law with Solar System Planets', fontsize=16)

    plt.text(0.05, 0.95, 'T² = (4π²/GM) × R³', transform=plt.gca().transAxes, 
            fontsize=14, verticalalignment='top', 
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))

    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(image_dir, 'keplers_third_law.png'), dpi=300, bbox_inches='tight')
    plt.close()

    # 3. Log-log plot of Kepler's Third Law
    plt.figure(figsize=(10, 8))
    plt.loglog(radii_au, periods_years, 'b-', linewidth=3, alpha=0.7, label='T ∝ R^(3/2)')

    for planet, data in planet_data.items():
        period_years = calculate_period(data['radius'], M_sun) / (86400 * 365.25)
        radius_au = data['radius'] / AU
        plt.scatter(radius_au, period_years, color=data['color'], s=100, 
                   edgecolors='black', linewidth=1, zorder=10)
        plt.annotate(planet, (radius_au, period_years), 
                    xytext=(10, 10), textcoords='offset points',
                    fontsize=11, fontweight='bold')

    plt.grid(True, which='both', linestyle='--', alpha=0.7)
    plt.xlabel('Orbital Radius (AU) - Log Scale', fontsize=14)
    plt.ylabel('Orbital Period (years) - Log Scale', fontsize=14)
    plt.title('Kepler\'s Third Law: Log-Log Plot\n(Slope = 3/2 confirms T ∝ R^(3/2))', fontsize=16)
    plt.legend(fontsize=12)
    plt.tight_layout()
    plt.savefig(os.path.join(image_dir, 'keplers_law_loglog.png'), dpi=300, bbox_inches='tight')
    plt.close()

    # 4. Circular orbit dynamics demonstration
    plt.figure(figsize=(10, 10))
    
    # Central body
    plt.scatter(0, 0, s=400, color='gold', label='Central Body', 
               edgecolors='orange', linewidth=3, zorder=10)
    
    # Orbit path
    orbit_radius = 1.0
    theta = np.linspace(0, 2*np.pi, 200)
    x_orbit = orbit_radius * np.cos(theta)
    y_orbit = orbit_radius * np.sin(theta)
    plt.plot(x_orbit, y_orbit, 'k--', alpha=0.5, linewidth=2, label='Orbital path')
    
    # Show forces and velocities at different positions
    angles = [0, np.pi/3, np.pi, 4*np.pi/3]
    colors = ['red', 'green', 'purple', 'orange']
    
    for i, angle in enumerate(angles):
        x = orbit_radius * np.cos(angle)
        y = orbit_radius * np.sin(angle)
        
        # Velocity vector (tangent to orbit)
        vx = -np.sin(angle) * 0.4
        vy = np.cos(angle) * 0.4
        
        # Acceleration vector (toward center)
        ax_val = -np.cos(angle) * 0.3
        ay_val = -np.sin(angle) * 0.3
        
        # Orbiting body
        plt.scatter(x, y, color=colors[i], s=150, zorder=10, edgecolors='black')
        
        # Position vector
        plt.arrow(0, 0, x, y, color=colors[i], width=0.02, 
                 length_includes_head=True, alpha=0.7, 
                 label='Position vector' if i == 0 else '')
        
        # Velocity vector
        plt.arrow(x, y, vx, vy, color='blue', width=0.02, 
                 length_includes_head=True, alpha=0.8,
                 label='Velocity vector' if i == 0 else '')
        
        # Acceleration vector
        plt.arrow(x, y, ax_val, ay_val, color='red', width=0.02, 
                 length_includes_head=True, alpha=0.8,
                 label='Centripetal acceleration' if i == 0 else '')

    plt.grid(True, linestyle='--', alpha=0.7)
    plt.xlim(-1.8, 1.8)
    plt.ylim(-1.8, 1.8)
    plt.axis('equal')
    plt.xlabel('x (normalized units)', fontsize=12)
    plt.ylabel('y (normalized units)', fontsize=12)
    plt.title('Circular Orbit Dynamics\nVectors at Different Orbital Positions', fontsize=14)
    plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1))
    plt.tight_layout()
    plt.savefig(os.path.join(image_dir, 'orbit_dynamics.png'), dpi=300, bbox_inches='tight')
    plt.close()

    # 5. Effect of central mass on orbital characteristics
    masses = [0.5*M_sun, 1.0*M_sun, 2.0*M_sun, 5.0*M_sun]
    radii_range = np.linspace(0.5, 5, 100) * AU
    
    plt.figure(figsize=(12, 8))
    
    for i, mass in enumerate(masses):
        periods = [calculate_period(r, mass) for r in radii_range]
        periods_years = np.array(periods) / (86400 * 365.25)
        plt.plot(radii_range/AU, periods_years, linewidth=3, 
                label=f'Mass = {mass/M_sun:.1f} M☉')
    
    plt.grid(True, alpha=0.3)
    plt.xlabel('Orbital Radius (AU)', fontsize=14)
    plt.ylabel('Orbital Period (years)', fontsize=14)
    plt.title('Effect of Central Mass on Orbital Period', fontsize=16)
    plt.legend(fontsize=12)
    plt.tight_layout()
    plt.savefig(os.path.join(image_dir, 'different_masses.png'), dpi=300, bbox_inches='tight')
    plt.close()

    # 6. Earth-Moon system barycenter
    M_moon = 7.342e22  
    earth_moon_distance = 3.844e8  # meters
    
    # Calculate barycenter position
    barycenter_distance_from_earth = earth_moon_distance * M_moon / (M_earth + M_moon)
    
    plt.figure(figsize=(12, 8))
    
    # Create visualization of Earth-Moon system
    earth_orbit_radius = barycenter_distance_from_earth
    moon_orbit_radius = earth_moon_distance - barycenter_distance_from_earth
    
    # Generate orbital paths
    theta = np.linspace(0, 2*np.pi, 100)
    earth_x = earth_orbit_radius * np.cos(theta)
    earth_y = earth_orbit_radius * np.sin(theta)
    
    moon_x = moon_orbit_radius * np.cos(theta + np.pi)
    moon_y = moon_orbit_radius * np.sin(theta + np.pi)
    
    plt.plot(earth_x/1000, earth_y/1000, 'b-', linewidth=3, label='Earth orbit around barycenter')
    plt.plot(moon_x/1000, moon_y/1000, 'gray', linewidth=3, label='Moon orbit around barycenter')
    
    # Show current positions
    plt.scatter(earth_x[0]/1000, earth_y[0]/1000, c='blue', s=200, 
               label='Earth', edgecolors='darkblue', linewidth=2)
    plt.scatter(moon_x[0]/1000, moon_y[0]/1000, c='gray', s=100, 
               label='Moon', edgecolors='black', linewidth=2)
    plt.scatter(0, 0, c='red', s=50, label='Barycenter', marker='x', linewidth=3)
    
    # Show connecting line
    plt.plot([earth_x[0]/1000, moon_x[0]/1000], [earth_y[0]/1000, moon_y[0]/1000], 
             'k--', alpha=0.5, linewidth=2)
    
    plt.grid(True, alpha=0.3)
    plt.axis('equal')
    plt.xlabel('Distance (km)', fontsize=14)
    plt.ylabel('Distance (km)', fontsize=14)
    plt.title('Earth-Moon System: Orbits Around Common Barycenter', fontsize=16)
    plt.legend(fontsize=12)
    
    # Add informative text
    plt.text(0.02, 0.98, f'Barycenter distance from Earth center: {barycenter_distance_from_earth/1000:.0f} km\n'
                        f'Earth radius: {6371:.0f} km\n'
                        f'Barycenter is {barycenter_distance_from_earth/6371000:.1f} Earth radii from center',
             transform=plt.gca().transAxes, verticalalignment='top',
             bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))
    
    plt.tight_layout()
    plt.savefig(os.path.join(image_dir, 'earth_moon_barycenter.png'), dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"All orbital mechanics visualizations saved to {image_dir}")

if __name__ == "__main__":
    print("Generating orbital mechanics visualizations...")
    
    # Generate the main plot referenced in Problem_1.md
    generate_main_plot()
    print("Generated problem1.png")
    
    # Generate comprehensive analysis plots
    run_comprehensive_analysis()
    print("Generated all comprehensive orbital mechanics plots")
    
    print("Orbital mechanics visualization generation complete!")