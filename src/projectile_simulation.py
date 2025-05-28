import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import os

# Get the correct path to the images directory
script_dir = os.path.dirname(os.path.abspath(__file__))
repo_root = os.path.dirname(script_dir)
image_dir = os.path.join(repo_root, 'docs', '1 Physics', '1 Mechanics', 'pics')
os.makedirs(image_dir, exist_ok=True)

def calculate_trajectory(v0, theta_deg, g=9.8, h0=0, time_step=0.01):
    theta = np.radians(theta_deg)
    
    v0x = v0 * np.cos(theta)
    v0y = v0 * np.sin(theta)
    
    discriminant = v0y**2 + 2*g*h0
    if discriminant < 0: 
        return [], [], 0
    
    t_flight = (v0y + np.sqrt(discriminant)) / g
    
    t = np.arange(0, t_flight + time_step, time_step)
    
    x = v0x * t
    y = h0 + v0y * t - 0.5 * g * t**2
    
    return x, y, t_flight

def calculate_range(v0, theta_deg, g=9.8, h0=0):
    """Calculate range using the analytical formula for projectile motion"""
    theta = np.radians(theta_deg)
    
    # For general case with initial height h0
    # Range = (v0*cos(theta)/g) * (v0*sin(theta) + sqrt((v0*sin(theta))^2 + 2*g*h0))
    v0x = v0 * np.cos(theta)
    v0y = v0 * np.sin(theta)
    
    discriminant = v0y**2 + 2*g*h0
    if discriminant < 0:
        return 0
    
    range_val = (v0x/g) * (v0y + np.sqrt(discriminant))
    return range_val

def theoretical_range(v0, theta_deg, g=9.8):
    """Theoretical range formula for h0=0: R = v0^2 * sin(2*theta) / g"""
    theta = np.radians(theta_deg)
    return (v0**2 * np.sin(2*theta)) / g

def generate_main_plot():
    """Generate the main plot referenced in the markdown as problem1.png"""
    v0 = 20  # initial velocity in m/s
    theta_values = np.linspace(0, 90, 100)  # range of angles
    g = 9.81  # gravity (using standard value)
    
    # Calculate theoretical ranges (h0=0 case)
    ranges = [theoretical_range(v0, theta, g) for theta in theta_values]
    
    plt.figure(figsize=(10, 6))
    plt.plot(theta_values, ranges, 'b-', linewidth=2, label=f'v₀ = {v0} m/s')
    
    # Mark the maximum at 45 degrees
    max_range = theoretical_range(v0, 45, g)
    plt.plot(45, max_range, 'ro', markersize=8)
    plt.annotate(f'Maximum: {max_range:.1f} m at 45°', 
                 xy=(45, max_range), xytext=(50, max_range-2),
                 arrowprops=dict(facecolor='red', shrink=0.05))
    
    plt.xlabel('Launch Angle (degrees)')
    plt.ylabel('Range (m)')
    plt.title('Projectile Range vs. Launch Angle')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xlim(0, 90)
    plt.ylim(0, max(ranges) * 1.1)
    
    # Save as problem1.png (referenced in markdown)
    plt.savefig(os.path.join(image_dir, 'problem1.png'), dpi=300, bbox_inches='tight')
    plt.close()

def generate_additional_plots():
    """Generate additional analysis plots"""
    v0 = 20  
    theta_values = np.arange(5, 86, 5)  
    g = 9.8 
    h0 = 0  

    ranges = [calculate_range(v0, theta, g, h0) for theta in theta_values]

    max_range_idx = np.argmax(ranges)
    max_range = ranges[max_range_idx]
    optimal_angle = theta_values[max_range_idx]

    # Plot 1: Range vs angle with discrete points
    plt.figure(figsize=(10, 6))
    plt.plot(theta_values, ranges, 'b-', linewidth=2)
    plt.plot(optimal_angle, max_range, 'ro', markersize=8)
    plt.annotate(f'Maximum Range: {max_range:.2f} m at {optimal_angle}°', 
                 xy=(optimal_angle, max_range), xytext=(optimal_angle+5, max_range-5),
                 arrowprops=dict(facecolor='black', shrink=0.05, width=1.5))
    plt.grid(True)
    plt.xlabel('Launch Angle (degrees)')
    plt.ylabel('Range (m)')
    plt.title('Projectile Range vs Launch Angle')
    plt.savefig(os.path.join(image_dir, 'range_vs_angle.png'), dpi=300, bbox_inches='tight')
    plt.close()

    # Plot 2: Trajectories for different angles
    plt.figure(figsize=(12, 6))
    selected_angles = [15, 30, 45, 60, 75]
    colors = ['r', 'g', 'b', 'c', 'm']

    for angle, color in zip(selected_angles, colors):
        x, y, _ = calculate_trajectory(v0, angle, g, h0)
        plt.plot(x, y, color=color, linewidth=2, label=f'{angle}°')

    plt.grid(True)
    plt.xlabel('Horizontal Distance (m)')
    plt.ylabel('Height (m)')
    plt.title('Projectile Trajectories for Different Launch Angles')
    plt.legend()
    plt.ylim(bottom=0)
    plt.savefig(os.path.join(image_dir, 'trajectories.png'), dpi=300, bbox_inches='tight')
    plt.close()

    # Plot 3: Effect of initial velocity
    velocities = np.linspace(10, 50, 5)
    plt.figure(figsize=(10, 6))

    for v in velocities:
        ranges = [calculate_range(v, theta, g, h0) for theta in theta_values]
        plt.plot(theta_values, ranges, linewidth=2, label=f'v₀ = {v} m/s')

    plt.grid(True)
    plt.xlabel('Launch Angle (degrees)')
    plt.ylabel('Range (m)')
    plt.title('Range vs Launch Angle for Different Initial Velocities')
    plt.legend()
    plt.savefig(os.path.join(image_dir, 'range_vs_velocity.png'), dpi=300, bbox_inches='tight')
    plt.close()

    # Plot 4: Effect of gravity on different celestial bodies
    gravities = {
        'Earth': 9.8,
        'Moon': 1.62,
        'Mars': 3.72,
        'Jupiter': 24.79
    }

    plt.figure(figsize=(10, 6))

    for planet, g_value in gravities.items():
        ranges = [calculate_range(v0, theta, g_value, h0) for theta in theta_values]
        plt.plot(theta_values, ranges, linewidth=2, label=f'{planet} (g = {g_value} m/s²)')

    plt.grid(True)
    plt.xlabel('Launch Angle (degrees)')
    plt.ylabel('Range (m)')
    plt.title('Range vs Launch Angle on Different Celestial Bodies')
    plt.legend()
    plt.savefig(os.path.join(image_dir, 'range_vs_gravity.png'), dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    print("Generating projectile motion visualizations...")
    
    # Generate the main plot referenced in Problem_1.md
    generate_main_plot()
    print(f"Generated problem1.png")
    
    # Generate additional analysis plots
    generate_additional_plots()
    print(f"Generated additional analysis plots")
    
    print(f"All images saved to {image_dir}")
    print("Visualization generation complete!")
