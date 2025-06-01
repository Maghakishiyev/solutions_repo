import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
repo_root = os.path.dirname(script_dir)
image_dir = os.path.join(repo_root, 'docs', '1 Physics', '4 Electromagnetism', 'pics')
os.makedirs(image_dir, exist_ok=True)

def lorentz_force(q, E, v, B):
    return q * (E + np.cross(v, B))

def acceleration(q, m, E, v, B):
    F = lorentz_force(q, E, v, B)
    return F / m

def runge_kutta_step(q, m, E, v, r, B, dt):
    a1 = acceleration(q, m, E, v, B)
    k1_v = a1 * dt
    k1_r = v * dt
    
    a2 = acceleration(q, m, E, v + 0.5 * k1_v, B)
    k2_v = a2 * dt
    k2_r = (v + 0.5 * k1_v) * dt
    
    a3 = acceleration(q, m, E, v + 0.5 * k2_v, B)
    k3_v = a3 * dt
    k3_r = (v + 0.5 * k2_v) * dt
    
    a4 = acceleration(q, m, E, v + k3_v, B)
    k4_v = a4 * dt
    k4_r = (v + k3_v) * dt
    
    v_new = v + (k1_v + 2*k2_v + 2*k3_v + k4_v) / 6
    r_new = r + (k1_r + 2*k2_r + 2*k3_r + k4_r) / 6
    
    return r_new, v_new

def simulate_particle_motion(q, m, E, B, v0, r0, dt, steps):
    positions = np.zeros((steps, 3))
    velocities = np.zeros((steps, 3))
    
    positions[0] = r0
    velocities[0] = v0
    
    for i in range(1, steps):
        positions[i], velocities[i] = runge_kutta_step(
            q, m, E, velocities[i-1], positions[i-1], B, dt
        )
    
    return positions, velocities

def calculate_larmor_radius(q, m, v_perp, B_mag):
    return m * v_perp / (abs(q) * B_mag)

def calculate_cyclotron_frequency(q, m, B_mag):
    return abs(q) * B_mag / m

def calculate_drift_velocity(q, E, B):
    B_squared = np.sum(B**2)
    return np.cross(E, B) / B_squared

def plot_trajectory_2d(positions, title, save_path=None, E=None, B=None):
    plt.figure(figsize=(10, 8))
    plt.plot(positions[:, 0], positions[:, 1], 'b-', label='Trajectory')
    plt.plot(positions[0, 0], positions[0, 1], 'go', label='Start')
    plt.plot(positions[-1, 0], positions[-1, 1], 'ro', label='End')
    
    x_min, x_max = positions[:, 0].min(), positions[:, 0].max()
    y_min, y_max = positions[:, 1].min(), positions[:, 1].max()
    x_range = x_max - x_min
    y_range = y_max - y_min
    
    if E is not None and np.any(E):
        corner_x = x_max + 0.05 * x_range
        corner_y = y_max - 0.05 * y_range
        E_scale = 0.15 * max(x_range, y_range)
        
        plt.arrow(corner_x, corner_y, E_scale * E[0], E_scale * E[1], 
                 color='r', width=0.005 * E_scale, head_width=0.03 * E_scale, 
                 head_length=0.05 * E_scale, label='E field')
    
    if B is not None and np.any(B):
        corner_x = x_min - 0.05 * x_range
        corner_y = y_max - 0.05 * y_range
        
        if B[2] > 0:  
            plt.scatter(corner_x, corner_y, color='g', marker='o', s=300, label='B field (out)')
            plt.scatter(corner_x, corner_y, color='g', marker='.', s=100)
        elif B[2] < 0:  
            plt.scatter(corner_x, corner_y, color='g', marker='o', s=300, label='B field (in)')
            plt.scatter(corner_x, corner_y, color='g', marker='x', s=100)
        else:  
            B_scale = 0.15 * max(x_range, y_range)
            plt.arrow(corner_x, corner_y, B_scale * B[0], B_scale * B[1], 
                     color='g', width=0.005 * B_scale, head_width=0.03 * B_scale, 
                     head_length=0.05 * B_scale, label='B field')
    
    plt.title(title)
    plt.xlabel('X (m)')
    plt.ylabel('Y (m)')
    plt.grid(True)
    
    plt.legend(loc='upper left', fontsize='small')
    
    plt.xlim(x_min - 0.2 * x_range, x_max + 0.2 * x_range)
    plt.ylim(y_min - 0.2 * y_range, y_max + 0.2 * y_range)
    
    plt.ticklabel_format(style='sci', scilimits=(-2, 2), axis='both')
    
    plt.axis('equal')
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Saved 2D plot to {save_path}")
        plt.close()
    else:
        plt.show()

def plot_trajectory_3d(positions, title, save_path=None, E=None, B=None):
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    ax.plot(positions[:, 0], positions[:, 1], positions[:, 2], 'b-', label='Trajectory')
    ax.scatter(positions[0, 0], positions[0, 1], positions[0, 2], color='g', s=100, label='Start')
    ax.scatter(positions[-1, 0], positions[-1, 1], positions[-1, 2], color='r', s=100, label='End')
    
    max_range = np.array([positions[:, 0].max() - positions[:, 0].min(),
                          positions[:, 1].max() - positions[:, 1].min(),
                          positions[:, 2].max() - positions[:, 2].min()]).max() / 2.0
    
    mid_x = (positions[:, 0].max() + positions[:, 0].min()) * 0.5
    mid_y = (positions[:, 1].max() + positions[:, 1].min()) * 0.5
    mid_z = (positions[:, 2].max() + positions[:, 2].min()) * 0.5
    
    x_min, x_max = mid_x - max_range, mid_x + max_range
    y_min, y_max = mid_y - max_range, mid_y + max_range
    z_min, z_max = mid_z - max_range, mid_z + max_range
    
    if E is not None and np.any(E):
        corner_x = x_max - 0.1 * (x_max - x_min)
        corner_y = y_max - 0.1 * (y_max - y_min)
        corner_z = z_max - 0.1 * (z_max - z_min)
        
        E_scale = 0.15 * max_range
        ax.quiver(corner_x, corner_y, corner_z, 
                 E_scale * E[0], E_scale * E[1], E_scale * E[2], 
                 color='r', arrow_length_ratio=0.3, label='E field')
    
    if B is not None and np.any(B):
        corner_x = x_min + 0.1 * (x_max - x_min)
        corner_y = y_max - 0.1 * (y_max - y_min)
        corner_z = z_max - 0.1 * (z_max - z_min)
        
        B_scale = 0.15 * max_range
        ax.quiver(corner_x, corner_y, corner_z, 
                 B_scale * B[0], B_scale * B[1], B_scale * B[2], 
                 color='g', arrow_length_ratio=0.3, label='B field')
    
    ax.set_title(title)
    ax.set_xlabel('X (m)')
    ax.set_ylabel('Y (m)')
    ax.set_zlabel('Z (m)')
    
    ax.legend(loc='upper left', fontsize='small')
    
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_zlim(z_min, z_max)
    
    ax.ticklabel_format(style='sci', scilimits=(-2, 2), axis='both')
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Saved 3D plot to {save_path}")
        plt.close()
    else:
        plt.show()

def create_animation(positions, title, save_path=None, E=None, B=None):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    line, = ax.plot([], [], [], 'b-', label='Trajectory')
    point, = ax.plot([], [], [], 'ro', markersize=8)
    
    max_range = np.array([positions[:, 0].max() - positions[:, 0].min(),
                          positions[:, 1].max() - positions[:, 1].min(),
                          positions[:, 2].max() - positions[:, 2].min()]).max() / 2.0
    
    mid_x = (positions[:, 0].max() + positions[:, 0].min()) * 0.5
    mid_y = (positions[:, 1].max() + positions[:, 1].min()) * 0.5
    mid_z = (positions[:, 2].max() + positions[:, 2].min()) * 0.5
    
    x_min, x_max = mid_x - max_range, mid_x + max_range
    y_min, y_max = mid_y - max_range, mid_y + max_range
    z_min, z_max = mid_z - max_range, mid_z + max_range
    
    if E is not None and np.any(E):
        corner_x = x_max - 0.1 * (x_max - x_min)
        corner_y = y_max - 0.1 * (y_max - y_min)
        corner_z = z_max - 0.1 * (z_max - z_min)
        
        E_scale = 0.15 * max_range
        ax.quiver(corner_x, corner_y, corner_z, 
                 E_scale * E[0], E_scale * E[1], E_scale * E[2], 
                 color='r', arrow_length_ratio=0.3, label='E field')
    
    if B is not None and np.any(B):
        corner_x = x_min + 0.1 * (x_max - x_min)
        corner_y = y_max - 0.1 * (y_max - y_min)
        corner_z = z_max - 0.1 * (z_max - z_min)
        
        B_scale = 0.15 * max_range
        ax.quiver(corner_x, corner_y, corner_z, 
                 B_scale * B[0], B_scale * B[1], B_scale * B[2], 
                 color='g', arrow_length_ratio=0.3, label='B field')
    
    ax.set_xlabel('X (m)')
    ax.set_ylabel('Y (m)')
    ax.set_zlabel('Z (m)')
    ax.set_title(title)
    
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_zlim(z_min, z_max)
    
    ax.legend(loc='upper left', fontsize='small')
    
    def init():
        line.set_data([], [])
        line.set_3d_properties([])
        point.set_data([], [])
        point.set_3d_properties([])
        return line, point
    
    def animate(i):
        window_size = 50
        start_idx = max(0, i - window_size)
        
        x = positions[start_idx:i+1, 0]
        y = positions[start_idx:i+1, 1]
        z = positions[start_idx:i+1, 2]
        
        line.set_data(x, y)
        line.set_3d_properties(z)
        
        point.set_data([positions[i, 0]], [positions[i, 1]])
        point.set_3d_properties([positions[i, 2]])
        
        return line, point
    
    frames = min(len(positions), 200)  
    step = len(positions) // frames if len(positions) > frames else 1
    ani = FuncAnimation(fig, animate, frames=range(0, len(positions), step),
                        init_func=init, blit=True, interval=50)
    
    if save_path:
        ani.save(save_path, writer='pillow', fps=20)
        print(f"Saved animation to {save_path}")
        plt.close()
    else:
        plt.show()

def magnetic_bottle(q=1.602e-19, m=9.109e-31, B0=1.0, z_max=1.0, v0=1e6, v_parallel_ratio=0.3, steps=2000, dt=1e-11, save_plots=True):
    def B_field(r):
        z = r[2]
        B_z = B0 * (1 + (z / z_max)**2)
        B_r = -B0 * z * r[0] / (z_max**2)
        B_theta = -B0 * z * r[1] / (z_max**2)
        return np.array([B_r, B_theta, B_z])
    
    E = np.array([0.0, 0.0, 0.0])  
    B_center = np.array([0.0, 0.0, B0])  
    v_parallel = v0 * v_parallel_ratio
    v_perp = v0 * np.sqrt(1 - v_parallel_ratio**2)
    v0_vec = np.array([v_perp, 0.0, v_parallel])  
    r0 = np.array([0.0, 0.0, 0.0]) 
    
    mu = 0.5 * m * v_perp**2 / B0
    
    def simulate_with_nonuniform_B(q, m, E, v0, r0, dt, steps):
        positions = np.zeros((steps, 3))
        velocities = np.zeros((steps, 3))
        
        positions[0] = r0
        velocities[0] = v0
        
        for i in range(1, steps):
            B = B_field(positions[i-1])
            
            positions[i], velocities[i] = runge_kutta_step(q, m, E, velocities[i-1], positions[i-1], B, dt)
            
            if np.any(np.isnan(positions[i])) or np.any(np.isinf(positions[i])):
                print(f"Warning: NaN or Inf values detected at step {i}. Truncating simulation.")
                return positions[:i], velocities[:i]
        
        return positions, velocities
    
    positions, velocities = simulate_with_nonuniform_B(q, m, E, v0_vec, r0, dt, steps)
    
    z_max_reached = np.max(np.abs(positions[:, 2]))
    
    observations = {
        'magnetic_moment': f"Magnetic moment: {mu:.3e} J/T (conserved)",
        'pitch_angle': f"Pitch angle: {np.arctan2(v_perp, v_parallel)*180/np.pi:.1f}°",
        'turning_point': f"Maximum z reached: {z_max_reached:.3e} m"
    }
    
    if save_plots:
        title = f"Charged Particle in Magnetic Bottle"
        plot_path_3d = os.path.join(image_dir, 'magnetic_bottle_trajectory.png')
        
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        ax.plot(positions[:, 0], positions[:, 1], positions[:, 2], 'g-', label='Trajectory')
        ax.plot([positions[0, 0]], [positions[0, 1]], [positions[0, 2]], 'go', label='Start')
        ax.plot([positions[-1, 0]], [positions[-1, 1]], [positions[-1, 2]], 'ro', label='End')
        
        ax.set_zlim(-0.006, 0.006)
        
        z_range = np.linspace(-0.006, 0.006, 2) 
        ax.plot([0, 0], [0, 0], z_range, 'b-', linewidth=2, label='B field')
        
        ax.text(0, 0, z_range[-1]*1.1, 'B', color='blue', fontsize=14, ha='center')
        
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title(title)
        ax.legend()
        
        plt.savefig(plot_path_3d)
        print(f"Saved 3D plot to {plot_path_3d}")
    
    return positions, velocities

def create_magnetic_bottle_animation():
    q = 1.602e-19  
    m = 9.109e-31 
    B0 = 1.0
    z_max = 1.0  
    v0 = 1e6
    v_parallel_ratio = 0.5  
    v_perp_ratio = 0.866   
    steps = 500  
    dt = 1e-11
    
    E = np.array([0.0, 0.0, 0.0]) 
    B_center = np.array([0.0, 0.0, B0])  
    
    v_parallel = v0 * v_parallel_ratio
    v_perp = v0 * v_perp_ratio
    v0_vec = np.array([v_perp, 0.0, v_parallel])  
    r0 = np.array([0.0, 0.0, -0.5])
    
    def B_field(r):
        z = r[2]
        B_z = B0 * (1 + (z / z_max)**2)
        B_r = -B0 * z * r[0] / (z_max**2)
        B_theta = -B0 * z * r[1] / (z_max**2)
        return np.array([B_r, B_theta, B_z])
    
    def simulate_with_nonuniform_B(q, m, E, v0, r0, dt, steps):
        positions = np.zeros((steps, 3))
        velocities = np.zeros((steps, 3))
        
        positions[0] = r0
        velocities[0] = v0
        
        for i in range(1, steps):
            B = B_field(positions[i-1])
            
            positions[i], velocities[i] = runge_kutta_step(q, m, E, velocities[i-1], positions[i-1], B, dt)
            
            if np.any(np.isnan(positions[i])) or np.any(np.isinf(positions[i])):
                print(f"Warning: NaN or Inf values detected at step {i}. Truncating simulation.")
                return positions[:i], velocities[:i]
        
        return positions, velocities
    
    positions, velocities = simulate_with_nonuniform_B(q, m, E, v0_vec, r0, dt, steps)
    
    title = f"Charged Particle in Magnetic Bottle"
    static_image_path = os.path.join(image_dir, 'magnetic_bottle_static.png')
    
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    max_range = 0.6
    ax.set_xlim(-max_range, max_range)
    ax.set_ylim(-max_range, max_range)
    ax.set_zlim(-max_range, max_range)
    
    z_values = np.linspace(-max_range, max_range, 2)
    ax.plot([0, 0], [0, 0], z_values, 'b-', linewidth=2, label='B field')
    
    ax.text(0, 0, z_values[-1]*1.1, 'B', color='blue', fontsize=14)
    
    ax.plot(positions[:, 0], positions[:, 1], positions[:, 2], '-', color='royalblue', label='Trajectory')
    
    mid_idx = len(positions) // 2
    ax.plot([positions[mid_idx, 0]], [positions[mid_idx, 1]], [positions[mid_idx, 2]], 'ro', markersize=10, label='Particle')
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(title)
    ax.legend()
    
    plt.savefig(static_image_path)
    print(f"Saved static image to {static_image_path}")
    plt.close(fig)

def run_comprehensive_simulations():
    """Run all Lorentz force simulations and generate visualizations."""
    
    # Physical constants
    q_electron = -1.602e-19  # Electron charge (C)
    m_electron = 9.109e-31   # Electron mass (kg)
    q_proton = 1.602e-19     # Proton charge (C)
    m_proton = 1.673e-27     # Proton mass (kg)
    
    print("Running comprehensive Lorentz force simulations...")
    
    # Simulation parameters
    dt = 1e-12  # Time step (s)
    steps = 2000  # Number of steps
    
    # Scenario 1: Uniform Magnetic Field Only
    print("\n1. Uniform Magnetic Field Scenario")
    B_uniform = np.array([0.0, 0.0, 0.1])  # 0.1 T in z-direction
    E_zero = np.array([0.0, 0.0, 0.0])
    v0_perp = np.array([1e6, 0.0, 0.0])  # 1 MeV perpendicular velocity
    r0 = np.array([0.0, 0.0, 0.0])
    
    positions, velocities = simulate_particle_motion(
        q_electron, m_electron, E_zero, B_uniform, v0_perp, r0, dt, steps
    )
    
    # Calculate theoretical parameters
    v_perp = np.linalg.norm(v0_perp)
    larmor_radius = calculate_larmor_radius(q_electron, m_electron, v_perp, np.linalg.norm(B_uniform))
    cyclotron_freq = calculate_cyclotron_frequency(q_electron, m_electron, np.linalg.norm(B_uniform))
    
    print(f"  Theoretical Larmor radius: {larmor_radius:.2e} m")
    print(f"  Cyclotron frequency: {cyclotron_freq:.2e} rad/s")
    
    plot_trajectory_2d(positions, "Uniform Magnetic Field - Circular Motion", 
                      save_path=os.path.join(image_dir, 'uniform_magnetic_field.png'),
                      E=E_zero, B=B_uniform)
    
    plot_trajectory_3d(positions, "Uniform Magnetic Field - 3D View", 
                      save_path=os.path.join(image_dir, 'uniform_magnetic_field_3d.png'),
                      E=E_zero, B=B_uniform)
    
    # Scenario 2: Combined Electric and Magnetic Fields (ExB Drift)
    print("\n2. Combined Electric and Magnetic Fields (ExB Drift)")
    E_combined = np.array([1000.0, 0.0, 0.0])  # 1 kV/m in x-direction
    B_combined = np.array([0.0, 0.0, 0.1])     # 0.1 T in z-direction
    v0_small = np.array([1e5, 0.0, 0.0])       # Smaller initial velocity
    
    positions_drift, velocities_drift = simulate_particle_motion(
        q_electron, m_electron, E_combined, B_combined, v0_small, r0, dt, steps*2
    )
    
    # Calculate drift velocity
    drift_velocity = calculate_drift_velocity(q_electron, E_combined, B_combined)
    print(f"  Theoretical ExB drift velocity: {drift_velocity} m/s")
    print(f"  Drift speed: {np.linalg.norm(drift_velocity):.2e} m/s")
    
    plot_trajectory_2d(positions_drift, "ExB Drift Motion", 
                      save_path=os.path.join(image_dir, 'combined_fields.png'),
                      E=E_combined, B=B_combined)
    
    plot_trajectory_3d(positions_drift, "ExB Drift Motion - 3D View", 
                      save_path=os.path.join(image_dir, 'combined_fields_3d.png'),
                      E=E_combined, B=B_combined)
    
    # Scenario 3: Crossed Fields (Velocity Selector)
    print("\n3. Crossed Electric and Magnetic Fields (Velocity Selector)")
    E_crossed = np.array([0.0, 2000.0, 0.0])  # 2 kV/m in y-direction
    B_crossed = np.array([0.0, 0.0, 0.1])     # 0.1 T in z-direction
    
    # Test different initial velocities
    v_select = np.linalg.norm(E_crossed) / np.linalg.norm(B_crossed)  # Selection velocity
    print(f"  Selection velocity: {v_select:.2e} m/s")
    
    velocities_test = [
        np.array([v_select * 0.8, 0.0, 0.0]),  # Below selection velocity
        np.array([v_select, 0.0, 0.0]),        # At selection velocity
        np.array([v_select * 1.2, 0.0, 0.0])   # Above selection velocity
    ]
    
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    labels = ['80% v_select', '100% v_select', '120% v_select']
    
    for i, v0_test in enumerate(velocities_test):
        positions_test, _ = simulate_particle_motion(
            q_electron, m_electron, E_crossed, B_crossed, v0_test, r0, dt, steps
        )
        
        axes[i].plot(positions_test[:, 0], positions_test[:, 1], 'b-', label='Trajectory')
        axes[i].plot(positions_test[0, 0], positions_test[0, 1], 'go', label='Start')
        axes[i].plot(positions_test[-1, 0], positions_test[-1, 1], 'ro', label='End')
        axes[i].set_title(f'Velocity Selector - {labels[i]}')
        axes[i].set_xlabel('X (m)')
        axes[i].set_ylabel('Y (m)')
        axes[i].grid(True)
        axes[i].legend()
        axes[i].axis('equal')
    
    plt.tight_layout()
    plt.savefig(os.path.join(image_dir, 'velocity_selector.png'), dpi=300, bbox_inches='tight')
    plt.close()
    
    # Scenario 4: Parameter Exploration - Mass Effect
    print("\n4. Parameter Exploration - Mass Effect")
    masses = [m_electron, m_proton]  # Electron and proton
    charges = [q_electron, q_proton]
    particles = ['Electron', 'Proton']
    
    fig, ax = plt.subplots(figsize=(12, 10))
    
    for i, (mass, charge, particle) in enumerate(zip(masses, charges, particles)):
        positions_mass, _ = simulate_particle_motion(
            charge, mass, E_zero, B_uniform, v0_perp, r0, dt, steps
        )
        
        ax.plot(positions_mass[:, 0], positions_mass[:, 1], 
               label=f'{particle} (m={mass:.2e} kg)', linewidth=2)
        ax.plot(positions_mass[0, 0], positions_mass[0, 1], 'o', markersize=8)
    
    ax.set_title('Mass Effect on Cyclotron Motion')
    ax.set_xlabel('X (m)')
    ax.set_ylabel('Y (m)')
    ax.grid(True)
    ax.legend()
    ax.axis('equal')
    plt.savefig(os.path.join(image_dir, 'mass_effect.png'), dpi=300, bbox_inches='tight')
    plt.close()
    
    # Scenario 5: Parameter Exploration - Magnetic Field Strength
    print("\n5. Parameter Exploration - Magnetic Field Strength")
    B_strengths = [0.05, 0.1, 0.2]  # Different magnetic field strengths
    
    fig, ax = plt.subplots(figsize=(12, 10))
    
    for B_strength in B_strengths:
        B_var = np.array([0.0, 0.0, B_strength])
        positions_B, _ = simulate_particle_motion(
            q_electron, m_electron, E_zero, B_var, v0_perp, r0, dt, steps
        )
        
        ax.plot(positions_B[:, 0], positions_B[:, 1], 
               label=f'B = {B_strength} T', linewidth=2)
        ax.plot(positions_B[0, 0], positions_B[0, 1], 'o', markersize=8)
    
    ax.set_title('Magnetic Field Strength Effect on Cyclotron Motion')
    ax.set_xlabel('X (m)')
    ax.set_ylabel('Y (m)')
    ax.grid(True)
    ax.legend()
    ax.axis('equal')
    plt.savefig(os.path.join(image_dir, 'field_strength_effect.png'), dpi=300, bbox_inches='tight')
    plt.close()
    
    # Scenario 6: Helical Motion
    print("\n6. Helical Motion in Magnetic Field")
    v0_helical = np.array([5e5, 0.0, 5e5])  # Velocity with both perpendicular and parallel components
    
    positions_helical, _ = simulate_particle_motion(
        q_electron, m_electron, E_zero, B_uniform, v0_helical, r0, dt, steps*2
    )
    
    plot_trajectory_3d(positions_helical, "Helical Motion in Magnetic Field", 
                      save_path=os.path.join(image_dir, 'helical_motion.png'),
                      E=E_zero, B=B_uniform)
    
    # Scenario 7: Magnetic Bottle
    print("\n7. Magnetic Bottle Confinement")
    magnetic_bottle()
    create_magnetic_bottle_animation()
    
    # Create combined parameter exploration plot
    print("\n8. Creating Combined Parameter Exploration Plot")
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
    
    # Mass effect subplot
    for i, (mass, charge, particle) in enumerate(zip(masses, charges, particles)):
        positions_mass, _ = simulate_particle_motion(
            charge, mass, E_zero, B_uniform, v0_perp, r0, dt, steps
        )
        ax1.plot(positions_mass[:, 0], positions_mass[:, 1], 
               label=f'{particle}', linewidth=2)
        ax1.plot(positions_mass[0, 0], positions_mass[0, 1], 'o', markersize=6)
    ax1.set_title('Mass Effect on Cyclotron Motion')
    ax1.set_xlabel('X (m)')
    ax1.set_ylabel('Y (m)')
    ax1.grid(True)
    ax1.legend()
    ax1.axis('equal')
    
    # Field strength effect subplot
    for B_strength in B_strengths:
        B_var = np.array([0.0, 0.0, B_strength])
        positions_B, _ = simulate_particle_motion(
            q_electron, m_electron, E_zero, B_var, v0_perp, r0, dt, steps
        )
        ax2.plot(positions_B[:, 0], positions_B[:, 1], 
               label=f'B = {B_strength} T', linewidth=2)
        ax2.plot(positions_B[0, 0], positions_B[0, 1], 'o', markersize=6)
    ax2.set_title('Magnetic Field Strength Effect')
    ax2.set_xlabel('X (m)')
    ax2.set_ylabel('Y (m)')
    ax2.grid(True)
    ax2.legend()
    ax2.axis('equal')
    
    # Velocity selector subplot (middle panel)
    v0_test = np.array([v_select, 0.0, 0.0])  # At selection velocity
    positions_test, _ = simulate_particle_motion(
        q_electron, m_electron, E_crossed, B_crossed, v0_test, r0, dt, steps
    )
    ax3.plot(positions_test[:, 0], positions_test[:, 1], 'b-', label='v = v_select')
    ax3.plot(positions_test[0, 0], positions_test[0, 1], 'go', label='Start')
    ax3.plot(positions_test[-1, 0], positions_test[-1, 1], 'ro', label='End')
    ax3.set_title('Velocity Selector at Selection Velocity')
    ax3.set_xlabel('X (m)')
    ax3.set_ylabel('Y (m)')
    ax3.grid(True)
    ax3.legend()
    ax3.axis('equal')
    
    # Helical motion projection
    ax4.plot(positions_helical[:, 0], positions_helical[:, 1], 'purple', linewidth=2, label='XY projection')
    ax4.plot(positions_helical[0, 0], positions_helical[0, 1], 'go', markersize=6, label='Start')
    ax4.plot(positions_helical[-1, 0], positions_helical[-1, 1], 'ro', markersize=6, label='End')
    ax4.set_title('Helical Motion (XY Projection)')
    ax4.set_xlabel('X (m)')
    ax4.set_ylabel('Y (m)')
    ax4.grid(True)
    ax4.legend()
    ax4.axis('equal')
    
    plt.tight_layout()
    plt.savefig(os.path.join(image_dir, 'parameter_exploration.png'), dpi=300, bbox_inches='tight')
    plt.close()
    print("  Saved parameter exploration plot")
    
    print("\nAll simulations completed successfully!")
    print(f"Visualizations saved to: {image_dir}")
    
    # List all generated files
    print("\nGenerated visualization files:")
    expected_files = [
        'uniform_magnetic_field.png',
        'uniform_magnetic_field_3d.png', 
        'combined_fields.png',
        'combined_fields_3d.png',
        'velocity_selector.png',
        'mass_effect.png',
        'field_strength_effect.png',
        'helical_motion.png',
        'magnetic_bottle_trajectory.png',
        'magnetic_bottle_static.png',
        'parameter_exploration.png'
    ]
    
    for filename in expected_files:
        filepath = os.path.join(image_dir, filename)
        if os.path.exists(filepath):
            print(f"  ✓ {filename}")
        else:
            print(f"  ✗ {filename} - NOT FOUND")

if __name__ == "__main__":
    run_comprehensive_simulations()
