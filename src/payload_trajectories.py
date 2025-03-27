import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import os
import imageio
import tempfile
from scipy.integrate import solve_ivp

image_dir = os.path.join('docs', '1 Physics', '2 Gravity', 'pics')
os.makedirs(image_dir, exist_ok=True)

G = 6.67430e-11  
M_EARTH = 5.972e24  
R_EARTH = 6.371e6  

def gravitational_acceleration(r, M=M_EARTH):
    return G * M / r**2

def payload_dynamics(t, state, mu=G*M_EARTH):
    x, y, vx, vy = state
    
    r = np.sqrt(x**2 + y**2)
    
    if r <= R_EARTH:
        return [0, 0, 0, 0] 
    
    a = mu / r**3
    
    return [vx, vy, -a * x, -a * y]

def simulate_trajectory(initial_position, initial_velocity, t_span, t_eval=None):
    initial_state = [initial_position[0], initial_position[1], 
                    initial_velocity[0], initial_velocity[1]]
    
    solution = solve_ivp(
        payload_dynamics,
        t_span,
        initial_state,
        method='RK45',
        t_eval=t_eval,
        rtol=1e-8,
        atol=1e-8
    )
    
    return solution

def calculate_orbital_parameters(position, velocity, mu=G*M_EARTH):
    r = np.sqrt(position[0]**2 + position[1]**2)
    v = np.sqrt(velocity[0]**2 + velocity[1]**2)
    
    energy = 0.5 * v**2 - mu / r
    
    if energy == 0:  
        a = float('inf')
    else:
        a = -mu / (2 * energy)
    
    pos_3d = np.array([position[0], position[1], 0])
    vel_3d = np.array([velocity[0], velocity[1], 0])
    h_vec = np.cross(pos_3d, vel_3d)
    h = np.abs(h_vec[2]) 
    e = np.sqrt(1 + 2 * energy * h**2 / mu**2)
    
    if e < 1e-10:  
        orbit_type = "Circular"
    elif e < 1.0:
        orbit_type = "Elliptical"
    elif abs(e - 1.0) < 1e-10:  
        orbit_type = "Parabolic"
    else:
        orbit_type = "Hyperbolic"
    
    if e < 1.0: 
        periapsis = a * (1 - e)
        apoapsis = a * (1 + e)
    elif e == 1.0: 
        periapsis = h**2 / (2 * mu)
        apoapsis = float('inf')
    else:  
        periapsis = a * (1 - e)  
        apoapsis = float('inf')
    
    return {
        "semi_major_axis": a,
        "eccentricity": e,
        "specific_energy": energy,
        "angular_momentum": h,
        "orbit_type": orbit_type,
        "periapsis": periapsis,
        "apoapsis": apoapsis
    }

def plot_trajectory(solution, title="Payload Trajectory", save_path=None):
    fig, ax = plt.subplots(figsize=(10, 10))
    
    x = solution.y[0]
    y = solution.y[1]
    
    ax.plot(x / R_EARTH, y / R_EARTH, 'b-', label='Payload Trajectory')
    
    earth_circle = plt.Circle((0, 0), 1, color='blue', alpha=0.3, label='Earth')
    ax.add_patch(earth_circle)
    
    ax.set_aspect('equal')
    
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.set_xlabel('x (Earth radii)', fontsize=12)
    ax.set_ylabel('y (Earth radii)', fontsize=12)
    ax.set_title(title, fontsize=14)
    
    ax.legend(loc='upper right')
    
    max_dist = max(np.max(np.abs(x)), np.max(np.abs(y))) / R_EARTH
    ax.set_xlim(-max_dist * 1.1, max_dist * 1.1)
    ax.set_ylim(-max_dist * 1.1, max_dist * 1.1)
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    return fig, ax

def create_trajectory_animation(solution, title="Payload Trajectory Animation", save_path=None):
    with tempfile.TemporaryDirectory() as tmpdirname:
        x = solution.y[0]
        y = solution.y[1]
        
        x_norm = x / R_EARTH
        y_norm = y / R_EARTH
        
        max_dist = max(np.max(np.abs(x_norm)), np.max(np.abs(y_norm)))
        
        n_frames = min(100, len(x)) 
        indices = np.linspace(0, len(x) - 1, n_frames, dtype=int)
        
        frames_filenames = []
        
        for i, idx in enumerate(indices):
            fig, ax = plt.subplots(figsize=(10, 10))
            
            ax.set_xlim(-max_dist * 1.1, max_dist * 1.1)
            ax.set_ylim(-max_dist * 1.1, max_dist * 1.1)
            
            earth_circle = plt.Circle((0, 0), 1, color='blue', alpha=0.3, label='Earth')
            ax.add_patch(earth_circle)
            
            ax.set_aspect('equal')
            
            ax.grid(True, linestyle='--', alpha=0.7)
            ax.set_xlabel('x (Earth radii)', fontsize=12)
            ax.set_ylabel('y (Earth radii)', fontsize=12)
            ax.set_title(title, fontsize=14)
            
            ax.plot(x_norm[:idx+1], y_norm[:idx+1], 'b-', label='Trajectory')
            
            ax.scatter(x_norm[idx], y_norm[idx], color='red', s=50, label='Payload')
            
            ax.legend(loc='upper right')
            
            frame_filename = os.path.join(tmpdirname, f'frame_{i:03d}.png')
            plt.savefig(frame_filename, dpi=100, bbox_inches='tight')
            frames_filenames.append(frame_filename)
            
            plt.close(fig)
        
        if save_path:
            with imageio.get_writer(save_path, mode='I', duration=0.1, loop=0) as writer:
                for frame_filename in frames_filenames:
                    image = imageio.imread(frame_filename)
                    writer.append_data(image)

def plot_multiple_trajectories(initial_conditions, t_span, title="Multiple Payload Trajectories", save_path=None):
    fig, ax = plt.subplots(figsize=(12, 12))
    
    earth_circle = plt.Circle((0, 0), 1, color='blue', alpha=0.3, label='Earth')
    ax.add_patch(earth_circle)
    
    ax.set_aspect('equal')
    
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.set_xlabel('x (Earth radii)', fontsize=12)
    ax.set_ylabel('y (Earth radii)', fontsize=12)
    ax.set_title(title, fontsize=14)
    
    max_dist = 1.0  
    
    for i, condition in enumerate(initial_conditions):
        initial_position = condition['position']
        initial_velocity = condition['velocity']
        label = condition.get('label', f'Trajectory {i+1}')
        color = condition.get('color', None)
        
        solution = simulate_trajectory(initial_position, initial_velocity, t_span)
        
        x = solution.y[0] / R_EARTH
        y = solution.y[1] / R_EARTH
        
        max_dist = max(max_dist, np.max(np.abs(x)), np.max(np.abs(y)))
        
        params = calculate_orbital_parameters(
            [solution.y[0][0], solution.y[1][0]],
            [solution.y[2][0], solution.y[3][0]]
        )
        
        ax.plot(x, y, label=f"{label} ({params['orbit_type']})", color=color)
        
        ax.scatter(x[0], y[0], color=color if color else 'black', s=50)
    
    ax.set_xlim(-max_dist * 1.1, max_dist * 1.1)
    ax.set_ylim(-max_dist * 1.1, max_dist * 1.1)
    
    ax.legend(loc='upper right')
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    return fig, ax

def generate_example_trajectories():
   
    altitude = 300e3  
    initial_position = [R_EARTH + altitude, 0] 
    
    circular_velocity = np.sqrt(G * M_EARTH / (R_EARTH + altitude))
    
    circular_initial_velocity = [0, circular_velocity]  
    circular_solution = simulate_trajectory(
        initial_position,
        circular_initial_velocity,
        [0, 3 * 3600]  
    )
    
    circular_params = calculate_orbital_parameters(
        [circular_solution.y[0][0], circular_solution.y[1][0]],
        [circular_solution.y[2][0], circular_solution.y[3][0]]
    )
    print("Circular Orbit Parameters:")
    for key, value in circular_params.items():
        print(f"  {key}: {value}")
    
    plot_trajectory(
        circular_solution,
        title="Circular Orbit Trajectory (300 km altitude)",
        save_path=os.path.join(image_dir, 'circular_orbit.png')
    )
    
    create_trajectory_animation(
        circular_solution,
        title="Circular Orbit Animation",
        save_path=os.path.join(image_dir, 'circular_orbit.gif')
    )
    
    elliptical_initial_velocity = [0, 0.9 * circular_velocity]  
    elliptical_solution = simulate_trajectory(
        initial_position,
        elliptical_initial_velocity,
        [0, 3 * 3600]  
    )
    
    elliptical_params = calculate_orbital_parameters(
        [elliptical_solution.y[0][0], elliptical_solution.y[1][0]],
        [elliptical_solution.y[2][0], elliptical_solution.y[3][0]]
    )
    print("\nElliptical Orbit Parameters:")
    for key, value in elliptical_params.items():
        print(f"  {key}: {value}")
    
    plot_trajectory(
        elliptical_solution,
        title="Elliptical Orbit Trajectory (90% of circular velocity)",
        save_path=os.path.join(image_dir, 'elliptical_orbit.png')
    )
    
    escape_velocity = np.sqrt(2 * G * M_EARTH / (R_EARTH + altitude))
    parabolic_initial_velocity = [0, escape_velocity]  
    parabolic_solution = simulate_trajectory(
        initial_position,
        parabolic_initial_velocity,
        [0, 6 * 3600]  
    )
    
    parabolic_params = calculate_orbital_parameters(
        [parabolic_solution.y[0][0], parabolic_solution.y[1][0]],
        [parabolic_solution.y[2][0], parabolic_solution.y[3][0]]
    )
    print("\nParabolic Trajectory Parameters:")
    for key, value in parabolic_params.items():
        print(f"  {key}: {value}")
    
    plot_trajectory(
        parabolic_solution,
        title="Parabolic Trajectory (Escape Velocity)",
        save_path=os.path.join(image_dir, 'parabolic_trajectory.png')
    )
    
    hyperbolic_initial_velocity = [0, 1.2 * escape_velocity] 
    hyperbolic_solution = simulate_trajectory(
        initial_position,
        hyperbolic_initial_velocity,
        [0, 6 * 3600]  
    )
    
    hyperbolic_params = calculate_orbital_parameters(
        [hyperbolic_solution.y[0][0], hyperbolic_solution.y[1][0]],
        [hyperbolic_solution.y[2][0], hyperbolic_solution.y[3][0]]
    )
    print("\nHyperbolic Trajectory Parameters:")
    for key, value in hyperbolic_params.items():
        print(f"  {key}: {value}")
    
    plot_trajectory(
        hyperbolic_solution,
        title="Hyperbolic Trajectory (120% of Escape Velocity)",
        save_path=os.path.join(image_dir, 'hyperbolic_trajectory.png')
    )
    
    reentry_initial_velocity = [0, 0.7 * circular_velocity]  
    reentry_solution = simulate_trajectory(
        initial_position,
        reentry_initial_velocity,
        [0, 1 * 3600] 
    )
    
    reentry_params = calculate_orbital_parameters(
        [reentry_solution.y[0][0], reentry_solution.y[1][0]],
        [reentry_solution.y[2][0], reentry_solution.y[3][0]]
    )
    print("\nReentry Trajectory Parameters:")
    for key, value in reentry_params.items():
        print(f"  {key}: {value}")
    
    plot_trajectory(
        reentry_solution,
        title="Reentry Trajectory (70% of circular velocity)",
        save_path=os.path.join(image_dir, 'reentry_trajectory.png')
    )
    
    initial_conditions = [
        {
            'position': initial_position,
            'velocity': [0, 0.7 * circular_velocity],
            'label': 'Reentry (70%)',
            'color': 'red'
        },
        {
            'position': initial_position,
            'velocity': [0, 0.9 * circular_velocity],
            'label': 'Elliptical (90%)',
            'color': 'green'
        },
        {
            'position': initial_position,
            'velocity': circular_initial_velocity,
            'label': 'Circular (100%)',
            'color': 'blue'
        },
        {
            'position': initial_position,
            'velocity': [0, escape_velocity],
            'label': 'Parabolic (Escape)',
            'color': 'purple'
        },
        {
            'position': initial_position,
            'velocity': [0, 1.2 * escape_velocity],
            'label': 'Hyperbolic (120%)',
            'color': 'orange'
        }
    ]
    
    plot_multiple_trajectories(
        initial_conditions,
        [0, 6 * 3600],  
        title="Comparison of Different Payload Trajectories",
        save_path=os.path.join(image_dir, 'trajectory_comparison.png')
    )
    
    angles = [0, 45, 90, 135, 180, 225, 270, 315]
    angle_conditions = []
    
    for angle in angles:
        angle_rad = np.radians(angle)
        
        vx = circular_velocity * np.cos(angle_rad)
        vy = circular_velocity * np.sin(angle_rad)
        
        angle_conditions.append({
            'position': initial_position,
            'velocity': [vx, vy],
            'label': f'{angle}°',
            'color': None  
        })
    
    plot_multiple_trajectories(
        angle_conditions,
        [0, 3 * 3600],  
        title="Payload Trajectories with Different Release Angles (Circular Velocity)",
        save_path=os.path.join(image_dir, 'angle_trajectories.png')
    )
    
    speeds = [0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0]
    speed_conditions = []
    
    for speed_factor in speeds:
        speed_conditions.append({
            'position': initial_position,
            'velocity': [0, speed_factor * circular_velocity],
            'label': f'{speed_factor:.2f}×V_circ',
            'color': None  
        })
    
    plot_multiple_trajectories(
        speed_conditions,
        [0, 6 * 3600],  
        title="Payload Trajectories with Different Initial Speeds",
        save_path=os.path.join(image_dir, 'speed_trajectories.png')
    )

if __name__ == "__main__":
    generate_example_trajectories()
    
    print("\nAll simulations and visualizations completed.")
    print(f"Images saved to {image_dir}")
