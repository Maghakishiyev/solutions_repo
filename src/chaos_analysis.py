#!/usr/bin/env python3
"""
Deterministic Chaos Analysis and Visualization
==============================================

This script generates comprehensive visualizations for chaos theory concepts including:
1. Logistic map bifurcation diagram
2. Lorenz attractor visualization  
3. Sensitivity to initial conditions demonstration
4. Lyapunov exponent calculation
5. Period-doubling cascade
6. Julia set fractals
7. Chaotic time series analysis

Author: Physics Class Project
Date: 2025
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
from matplotlib.colors import LinearSegmentedColormap
import os
import warnings
warnings.filterwarnings('ignore')

# Set up paths for saving figures
script_dir = os.path.dirname(os.path.abspath(__file__))
repo_root = os.path.dirname(script_dir)
image_dir = os.path.join(repo_root, 'docs', '1 Physics', '8 Deterministic Chaos', 'pics')
os.makedirs(image_dir, exist_ok=True)

plt.style.use('default')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12
plt.rcParams['lines.linewidth'] = 2

def logistic_map(r, x):
    """Logistic map function: x_n+1 = r * x_n * (1 - x_n)"""
    return r * x * (1 - x)

def logistic_map_derivative(r, x):
    """Derivative of logistic map: r * (1 - 2*x)"""
    return r * (1 - 2*x)

def iterate_logistic(r, x0, n_iterations=1000, n_transient=100):
    """Iterate the logistic map and return the time series"""
    x = x0
    trajectory = []
    
    # Skip transient behavior
    for _ in range(n_transient):
        x = logistic_map(r, x)
    
    # Collect trajectory
    for _ in range(n_iterations):
        x = logistic_map(r, x)
        trajectory.append(x)
    
    return np.array(trajectory)

def calculate_lyapunov_logistic(r, x0=0.5, n_iterations=10000):
    """Calculate Lyapunov exponent for logistic map"""
    x = x0
    lyap_sum = 0.0
    
    for _ in range(n_iterations):
        x = logistic_map(r, x)
        # Avoid log(0) by adding small epsilon
        derivative = abs(logistic_map_derivative(r, x))
        if derivative > 1e-15:
            lyap_sum += np.log(derivative)
    
    return lyap_sum / n_iterations

def lorenz_system(state, t, sigma=10.0, rho=28.0, beta=8.0/3.0):
    """Lorenz system differential equations"""
    x, y, z = state
    dx_dt = sigma * (y - x)
    dy_dt = x * (rho - z) - y
    dz_dt = x * y - beta * z
    return np.array([dx_dt, dy_dt, dz_dt])

def runge_kutta_4th(func, state, t, dt, *args):
    """4th order Runge-Kutta integration"""
    k1 = func(state, t, *args)
    k2 = func(state + 0.5*dt*k1, t + 0.5*dt, *args)
    k3 = func(state + 0.5*dt*k2, t + 0.5*dt, *args)
    k4 = func(state + dt*k3, t + dt, *args)
    return state + (dt/6.0) * (k1 + 2*k2 + 2*k3 + k4)

def generate_lorenz_attractor(initial_state=[1.0, 1.0, 1.0], dt=0.01, num_steps=10000):
    """Generate Lorenz attractor trajectory"""
    trajectory = np.zeros((num_steps, 3))
    state = np.array(initial_state)
    
    for i in range(num_steps):
        trajectory[i] = state
        state = runge_kutta_4th(lorenz_system, state, i*dt, dt)
    
    return trajectory

def julia_set(c, width=800, height=600, max_iter=100, x_range=(-2, 2), y_range=(-1.5, 1.5)):
    """Generate Julia set fractal"""
    x = np.linspace(x_range[0], x_range[1], width)
    y = np.linspace(y_range[0], y_range[1], height)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j*Y
    
    iterations = np.zeros(Z.shape, dtype=int)
    
    for i in range(max_iter):
        mask = np.abs(Z) <= 2
        Z[mask] = Z[mask]**2 + c
        iterations[mask] = i
    
    return iterations

def generate_bifurcation_diagram():
    """Generate bifurcation diagram for logistic map"""
    print("Generating bifurcation diagram...")
    
    r_min, r_max = 2.5, 4.0
    r_values = np.linspace(r_min, r_max, 2000)
    x0 = 0.5
    
    # Store results
    r_plot = []
    x_plot = []
    
    for r in r_values:
        # Skip transient behavior
        x = x0
        for _ in range(1000):
            x = logistic_map(r, x)
        
        # Collect attractor points
        for _ in range(100):
            x = logistic_map(r, x)
            r_plot.append(r)
            x_plot.append(x)
    
    plt.figure(figsize=(14, 10))
    plt.plot(r_plot, x_plot, ',k', alpha=0.5, markersize=0.1)
    plt.xlabel('Growth Parameter r', fontsize=14)
    plt.ylabel('Population x', fontsize=14)
    plt.title('Bifurcation Diagram of the Logistic Map\n$x_{n+1} = r x_n (1 - x_n)$', fontsize=16)
    plt.grid(True, alpha=0.3)
    
    # Add annotations for key bifurcation points
    plt.axvline(x=3.0, color='red', linestyle='--', alpha=0.7, label='First bifurcation (r=3)')
    plt.axvline(x=3.449, color='blue', linestyle='--', alpha=0.7, label='Second bifurcation (r≈3.449)')
    plt.axvline(x=3.569, color='green', linestyle='--', alpha=0.7, label='Chaos onset (r≈3.569)')
    
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(image_dir, 'bifurcation_diagram.png'), dpi=300, bbox_inches='tight')
    plt.close()

def generate_lorenz_visualization():
    """Generate Lorenz attractor visualization"""
    print("Generating Lorenz attractor...")
    
    # Generate trajectory
    trajectory = generate_lorenz_attractor(dt=0.01, num_steps=15000)
    x, y, z = trajectory[:, 0], trajectory[:, 1], trajectory[:, 2]
    
    # Create figure with subplots
    fig = plt.figure(figsize=(16, 12))
    
    # 3D plot
    ax1 = fig.add_subplot(221, projection='3d')
    ax1.plot(x, y, z, linewidth=0.8, alpha=0.8, color='blue')
    ax1.set_xlabel('X', fontsize=12)
    ax1.set_ylabel('Y', fontsize=12)
    ax1.set_zlabel('Z', fontsize=12)
    ax1.set_title('Lorenz Attractor - 3D View', fontsize=14)
    ax1.grid(True, alpha=0.3)
    
    # X-Y projection
    ax2 = fig.add_subplot(222)
    ax2.plot(x, y, linewidth=0.5, alpha=0.7, color='red')
    ax2.set_xlabel('X', fontsize=12)
    ax2.set_ylabel('Y', fontsize=12)
    ax2.set_title('X-Y Projection', fontsize=14)
    ax2.grid(True, alpha=0.3)
    
    # X-Z projection
    ax3 = fig.add_subplot(223)
    ax3.plot(x, z, linewidth=0.5, alpha=0.7, color='green')
    ax3.set_xlabel('X', fontsize=12)
    ax3.set_ylabel('Z', fontsize=12)
    ax3.set_title('X-Z Projection', fontsize=14)
    ax3.grid(True, alpha=0.3)
    
    # Time series
    ax4 = fig.add_subplot(224)
    t = np.arange(len(x)) * 0.01
    ax4.plot(t[:2000], x[:2000], linewidth=1, color='purple', label='X(t)')
    ax4.set_xlabel('Time', fontsize=12)
    ax4.set_ylabel('X', fontsize=12)
    ax4.set_title('Time Series (X component)', fontsize=14)
    ax4.grid(True, alpha=0.3)
    ax4.legend()
    
    plt.suptitle('Lorenz Attractor: $\\dot{x} = \\sigma(y-x)$, $\\dot{y} = x(\\rho-z)-y$, $\\dot{z} = xy-\\beta z$', 
                 fontsize=16)
    plt.tight_layout()
    plt.savefig(os.path.join(image_dir, 'lorenz_attractor.png'), dpi=300, bbox_inches='tight')
    plt.close()

def generate_sensitivity_demonstration():
    """Demonstrate sensitivity to initial conditions"""
    print("Generating sensitivity demonstration...")
    
    r = 3.8  # Chaotic regime
    x0_1 = 0.5
    x0_2 = 0.5 + 1e-6  # Tiny difference
    
    n_steps = 50
    trajectory_1 = [x0_1]
    trajectory_2 = [x0_2]
    
    x1, x2 = x0_1, x0_2
    for _ in range(n_steps):
        x1 = logistic_map(r, x1)
        x2 = logistic_map(r, x2)
        trajectory_1.append(x1)
        trajectory_2.append(x2)
    
    trajectory_1 = np.array(trajectory_1)
    trajectory_2 = np.array(trajectory_2)
    difference = np.abs(trajectory_1 - trajectory_2)
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    
    # Plot trajectories
    iterations = np.arange(len(trajectory_1))
    ax1.plot(iterations, trajectory_1, 'b-', linewidth=2, label=f'$x_0 = {x0_1}$')
    ax1.plot(iterations, trajectory_2, 'r--', linewidth=2, label=f'$x_0 = {x0_2}$')
    ax1.set_xlabel('Iteration n', fontsize=12)
    ax1.set_ylabel('Population $x_n$', fontsize=12)
    ax1.set_title('Sensitivity to Initial Conditions in Logistic Map (r = 3.8)', fontsize=14)
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    
    # Plot difference on log scale
    ax2.semilogy(iterations, difference, 'g-', linewidth=2, label='|Difference|')
    ax2.set_xlabel('Iteration n', fontsize=12)
    ax2.set_ylabel('|$x_n^{(1)} - x_n^{(2)}$|', fontsize=12)
    ax2.set_title('Exponential Divergence (Log Scale)', fontsize=14)
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    
    # Add exponential fit
    try:
        # Fit exponential growth to divergence
        nonzero_idx = difference > 1e-15
        if np.sum(nonzero_idx) > 10:
            fit_x = iterations[nonzero_idx]
            fit_y = np.log(difference[nonzero_idx])
            coeffs = np.polyfit(fit_x, fit_y, 1)
            lyap_est = coeffs[0]
            
            # Plot exponential fit
            fit_line = np.exp(coeffs[1] + coeffs[0] * iterations)
            ax2.semilogy(iterations, fit_line, 'k--', alpha=0.7, 
                        label=f'Exponential fit (λ ≈ {lyap_est:.3f})')
            ax2.legend()
    except:
        pass
    
    plt.tight_layout()
    plt.savefig(os.path.join(image_dir, 'sensitivity_demonstration.png'), dpi=300, bbox_inches='tight')
    plt.close()

def generate_lyapunov_spectrum():
    """Generate Lyapunov exponent spectrum"""
    print("Generating Lyapunov spectrum...")
    
    r_values = np.linspace(2.5, 4.0, 300)
    lyapunov_values = []
    
    for r in r_values:
        lyap = calculate_lyapunov_logistic(r)
        lyapunov_values.append(lyap)
    
    plt.figure(figsize=(12, 8))
    plt.plot(r_values, lyapunov_values, 'b-', linewidth=1.5)
    plt.axhline(y=0, color='red', linestyle='--', alpha=0.7, label='λ = 0 (Chaos threshold)')
    plt.xlabel('Growth Parameter r', fontsize=14)
    plt.ylabel('Lyapunov Exponent λ', fontsize=14)
    plt.title('Lyapunov Exponent for Logistic Map', fontsize=16)
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    # Highlight chaotic regions
    chaotic_mask = np.array(lyapunov_values) > 0
    plt.fill_between(r_values, -2, 2, where=chaotic_mask, alpha=0.2, color='red', label='Chaotic regions')
    
    plt.ylim(-2, 1)
    plt.tight_layout()
    plt.savefig(os.path.join(image_dir, 'lyapunov_spectrum.png'), dpi=300, bbox_inches='tight')
    plt.close()

def generate_period_doubling():
    """Generate period-doubling cascade visualization"""
    print("Generating period-doubling cascade...")
    
    # Focus on period-doubling region
    r_values = [2.8, 3.2, 3.45, 3.52, 3.55]
    r_labels = ['r=2.8 (Fixed point)', 'r=3.2 (Period-2)', 'r=3.45 (Period-4)', 
                'r=3.52 (Period-8)', 'r=3.55 (Near chaos)']
    
    fig, axes = plt.subplots(2, 3, figsize=(16, 10))
    axes = axes.flatten()
    
    for i, (r, label) in enumerate(zip(r_values, r_labels)):
        if i < len(axes):
            trajectory = iterate_logistic(r, 0.5, n_iterations=100, n_transient=500)
            
            axes[i].plot(trajectory, 'o-', markersize=4, linewidth=1, alpha=0.8)
            axes[i].set_title(label, fontsize=12)
            axes[i].set_xlabel('Iteration', fontsize=10)
            axes[i].set_ylabel('Population x', fontsize=10)
            axes[i].grid(True, alpha=0.3)
            axes[i].set_ylim(0, 1)
    
    # Remove empty subplot
    if len(r_values) < len(axes):
        fig.delaxes(axes[-1])
    
    plt.suptitle('Period-Doubling Route to Chaos', fontsize=16)
    plt.tight_layout()
    plt.savefig(os.path.join(image_dir, 'period_doubling.png'), dpi=300, bbox_inches='tight')
    plt.close()

def generate_julia_set_visualization():
    """Generate Julia set fractal"""
    print("Generating Julia set fractal...")
    
    # Classic Julia set parameters
    c_values = [-0.7269 + 0.1889j, -0.8 + 0.156j, -0.4 + 0.6j]
    c_labels = ['c = -0.73 + 0.19i', 'c = -0.8 + 0.16i', 'c = -0.4 + 0.6i']
    
    fig, axes = plt.subplots(1, 3, figsize=(16, 6))
    
    for i, (c, label) in enumerate(zip(c_values, c_labels)):
        julia = julia_set(c, width=600, height=600, max_iter=80)
        
        im = axes[i].imshow(julia, extent=[-2, 2, -2, 2], cmap='hot', origin='lower')
        axes[i].set_title(label, fontsize=12)
        axes[i].set_xlabel('Real', fontsize=10)
        axes[i].set_ylabel('Imaginary', fontsize=10)
    
    plt.suptitle('Julia Sets: Fractals from Chaotic Dynamics\n$z_{n+1} = z_n^2 + c$', fontsize=16)
    plt.tight_layout()
    plt.savefig(os.path.join(image_dir, 'julia_sets.png'), dpi=300, bbox_inches='tight')
    plt.close()

def generate_phase_space_comparison():
    """Compare regular vs chaotic motion in phase space"""
    print("Generating phase space comparison...")
    
    # Regular motion (limit cycle) vs chaotic motion
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Limit cycle (driven damped oscillator)
    t = np.linspace(0, 20*np.pi, 2000)
    # Simple limit cycle example
    x1 = np.cos(t) * np.exp(-0.1*t) + 0.5*np.cos(1.5*t)
    y1 = np.sin(t) * np.exp(-0.1*t) + 0.5*np.sin(1.5*t)
    
    ax1.plot(x1, y1, 'b-', linewidth=1, alpha=0.8)
    ax1.set_xlabel('Position', fontsize=12)
    ax1.set_ylabel('Velocity', fontsize=12)
    ax1.set_title('Regular Motion (Limit Cycle)', fontsize=14)
    ax1.grid(True, alpha=0.3)
    ax1.set_aspect('equal')
    
    # Chaotic motion (simplified Lorenz projection)
    lorenz_traj = generate_lorenz_attractor(dt=0.01, num_steps=5000)
    ax2.plot(lorenz_traj[:, 0], lorenz_traj[:, 1], 'r-', linewidth=0.5, alpha=0.7)
    ax2.set_xlabel('X', fontsize=12)
    ax2.set_ylabel('Y', fontsize=12)
    ax2.set_title('Chaotic Motion (Strange Attractor)', fontsize=14)
    ax2.grid(True, alpha=0.3)
    
    plt.suptitle('Phase Space: Regular vs Chaotic Dynamics', fontsize=16)
    plt.tight_layout()
    plt.savefig(os.path.join(image_dir, 'phase_space_comparison.png'), dpi=300, bbox_inches='tight')
    plt.close()

def generate_chaos_applications():
    """Generate visualization of chaos applications"""
    print("Generating chaos applications diagram...")
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 12))
    
    # Weather chaos demonstration
    ax1 = axes[0, 0]
    t = np.linspace(0, 10, 1000)
    weather1 = np.sin(t) + 0.5*np.sin(3*t) + 0.2*np.random.randn(1000)
    weather2 = np.sin(t + 0.01) + 0.5*np.sin(3*t + 0.01) + 0.2*np.random.randn(1000)
    
    ax1.plot(t, weather1, 'b-', label='Measurement 1', linewidth=1)
    ax1.plot(t, weather2, 'r--', label='Measurement 2 (+0.01)', linewidth=1)
    ax1.set_xlabel('Time (days)', fontsize=10)
    ax1.set_ylabel('Temperature', fontsize=10)
    ax1.set_title('Weather: Butterfly Effect', fontsize=12)
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Population dynamics
    ax2 = axes[0, 1]
    r_pop = 3.7
    pop = iterate_logistic(r_pop, 0.3, n_iterations=100, n_transient=0)
    ax2.plot(pop, 'g-', linewidth=2)
    ax2.set_xlabel('Generation', fontsize=10)
    ax2.set_ylabel('Population', fontsize=10)
    ax2.set_title('Population Dynamics (Chaotic)', fontsize=12)
    ax2.grid(True, alpha=0.3)
    
    # Chua's circuit (simulated)
    ax3 = axes[1, 0]
    t_circuit = np.linspace(0, 50, 2000)
    # Simplified chaotic circuit behavior
    circuit_x = np.sin(t_circuit) + 0.3*np.sin(7*t_circuit) + 0.1*np.sin(23*t_circuit)
    ax3.plot(t_circuit, circuit_x, 'm-', linewidth=1)
    ax3.set_xlabel('Time', fontsize=10)
    ax3.set_ylabel('Voltage', fontsize=10)
    ax3.set_title("Chua's Circuit (Electronic Chaos)", fontsize=12)
    ax3.grid(True, alpha=0.3)
    
    # Economic chaos (simulated)
    ax4 = axes[1, 1]
    # Simplified chaotic economic model
    econ_data = []
    x = 0.5
    for i in range(200):
        x = 3.9 * x * (1 - x) + 0.1*np.sin(i*0.1)  # Modified logistic with external forcing
        econ_data.append(x)
    
    ax4.plot(econ_data, 'orange', linewidth=2)
    ax4.set_xlabel('Time Period', fontsize=10)
    ax4.set_ylabel('Market Index', fontsize=10)
    ax4.set_title('Economic Markets (Chaotic Behavior)', fontsize=12)
    ax4.grid(True, alpha=0.3)
    
    plt.suptitle('Applications of Chaos Theory', fontsize=16)
    plt.tight_layout()
    plt.savefig(os.path.join(image_dir, 'chaos_applications.png'), dpi=300, bbox_inches='tight')
    plt.close()

def run_comprehensive_analysis():
    """Run all chaos theory visualizations"""
    print("=" * 60)
    print("DETERMINISTIC CHAOS - COMPREHENSIVE ANALYSIS")
    print("=" * 60)
    
    try:
        # Generate all visualizations
        generate_bifurcation_diagram()
        generate_lorenz_visualization()
        generate_sensitivity_demonstration()
        generate_lyapunov_spectrum()
        generate_period_doubling()
        generate_julia_set_visualization()
        generate_phase_space_comparison()
        generate_chaos_applications()
        
        print("\n" + "=" * 60)
        print("ALL VISUALIZATIONS GENERATED SUCCESSFULLY!")
        print("=" * 60)
        print(f"Images saved to: {image_dir}")
        print("\nGenerated files:")
        print("- bifurcation_diagram.png")
        print("- lorenz_attractor.png")
        print("- sensitivity_demonstration.png")
        print("- lyapunov_spectrum.png")
        print("- period_doubling.png")
        print("- julia_sets.png")
        print("- phase_space_comparison.png")
        print("- chaos_applications.png")
        
    except Exception as e:
        print(f"Error during analysis: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    run_comprehensive_analysis()