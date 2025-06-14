#!/usr/bin/env python3
"""
Educational Chaos Theory Visualization Tools
============================================

Interactive and educational tools for understanding chaos theory:
1. Butterfly effect demonstration with precise calculations
2. Feigenbaum sequence and universality
3. Chaos game (fractal generation)
4. Return maps and first return maps
5. Recurrence plots
6. Information theory and chaos
7. Synchronization of chaotic systems

Author: Physics Class Project - Educational Tools
Date: 2025
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
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

def butterfly_effect_quantitative():
    """Quantitative demonstration of butterfly effect"""
    print("Generating quantitative butterfly effect...")
    
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    
    # Logistic map parameters
    r = 3.9
    initial_separations = [1e-3, 1e-6, 1e-9, 1e-12]
    colors = ['red', 'blue', 'green', 'purple']
    
    for i, (delta0, color) in enumerate(zip(initial_separations, colors)):
        ax = axes[i//2, i%2]
        
        # Two trajectories with tiny difference
        x1, x2 = 0.5, 0.5 + delta0
        separations = [delta0]
        iterations = [0]
        
        # Theoretical Lyapunov exponent for r=3.9
        lyap_theoretical = np.log(3.9) - np.log(4)  # Approximate
        
        for n in range(1, 40):
            x1 = r * x1 * (1 - x1)
            x2 = r * x2 * (1 - x2)
            separation = abs(x2 - x1)
            
            if separation > 1e-15:  # Avoid numerical issues
                separations.append(separation)
                iterations.append(n)
            else:
                break
        
        # Plot actual separation
        ax.semilogy(iterations, separations, 'o-', color=color, linewidth=2, 
                   markersize=4, label=f'Actual (δ₀={delta0:.0e})')
        
        # Plot theoretical exponential growth
        if len(iterations) > 5:
            # Estimate Lyapunov exponent from data
            log_seps = np.log(separations)
            coeffs = np.polyfit(iterations[:len(log_seps)], log_seps, 1)
            lyap_estimated = coeffs[0]
            
            # Plot theoretical curve
            theoretical = delta0 * np.exp(lyap_estimated * np.array(iterations))
            ax.semilogy(iterations, theoretical, '--', color=color, alpha=0.7,
                       label=f'Theory (λ≈{lyap_estimated:.3f})')
        
        ax.set_xlabel('Iteration', fontsize=12)
        ax.set_ylabel('Separation |δ|', fontsize=12)
        ax.set_title(f'Initial Separation: {delta0:.0e}', fontsize=14)
        ax.grid(True, alpha=0.3)
        ax.legend()
        
        # Add doubling time
        if len(separations) > 1:
            # Find when separation doubles
            double_idx = None
            for j in range(1, len(separations)):
                if separations[j] >= 2 * separations[0]:
                    double_idx = j
                    break
            
            if double_idx:
                ax.axvline(x=iterations[double_idx], color='black', linestyle=':', alpha=0.7)
                ax.text(0.6, 0.9, f'Doubling time: {iterations[double_idx]} steps', 
                       transform=ax.transAxes, fontsize=10,
                       bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    plt.suptitle('Butterfly Effect: Quantitative Analysis', fontsize=16)
    plt.tight_layout()
    plt.savefig(os.path.join(image_dir, 'butterfly_effect_quantitative.png'), dpi=300, bbox_inches='tight')
    plt.close()

def feigenbaum_sequence():
    """Demonstrate Feigenbaum sequence and universality"""
    print("Generating Feigenbaum sequence...")
    
    def find_bifurcation_points():
        """Find period-doubling bifurcation points"""
        bifurcations = []
        
        # Known approximate values for logistic map
        r_values = [3.0, 3.449, 3.5441, 3.5644, 3.5688, 3.5697]
        
        # More precise calculation
        for i, r_start in enumerate(r_values[:-1]):
            r_end = r_values[i+1] if i+1 < len(r_values) else 3.57
            
            # Fine search for bifurcation point
            r_test = np.linspace(r_start, r_end, 1000)
            period = 2**i
            
            for r in r_test:
                # Test if system has desired period
                x = 0.5
                # Skip transients
                for _ in range(1000):
                    x = r * x * (1 - x)
                
                # Check period
                trajectory = []
                for _ in range(2 * period):
                    x = r * x * (1 - x)
                    trajectory.append(x)
                
                # Check if it's periodic with expected period
                if len(trajectory) >= 2 * period:
                    first_half = trajectory[:period]
                    second_half = trajectory[period:2*period]
                    
                    if np.allclose(first_half, second_half, rtol=1e-6):
                        bifurcations.append(r)
                        break
            
            if len(bifurcations) <= i:
                # Use approximate value if not found
                bifurcations.append(r_values[i+1] if i+1 < len(r_values) else 3.57)
        
        return bifurcations
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 12))
    
    # Use known values for demonstration
    bifurcations = [3.0, 3.449, 3.5441, 3.5644, 3.5688, 3.5697]
    
    # Calculate Feigenbaum constants
    deltas = []
    for i in range(len(bifurcations) - 1):
        delta = bifurcations[i+1] - bifurcations[i]
        deltas.append(delta)
    
    # Calculate ratios
    ratios = []
    for i in range(len(deltas) - 1):
        ratio = deltas[i] / deltas[i+1]
        ratios.append(ratio)
    
    # Plot bifurcation points
    periods = [2**i for i in range(len(bifurcations))]
    ax1.semilogx(periods, bifurcations, 'bo-', markersize=8, linewidth=2)
    ax1.set_xlabel('Period', fontsize=12)
    ax1.set_ylabel('Bifurcation Parameter r', fontsize=12)
    ax1.set_title('Period-Doubling Bifurcation Sequence', fontsize=14)
    ax1.grid(True, alpha=0.3)
    
    # Add annotations
    for i, (period, r) in enumerate(zip(periods, bifurcations)):
        ax1.annotate(f'r₍{i+1}₎ = {r:.4f}', 
                    xy=(period, r), xytext=(10, 10), 
                    textcoords='offset points', fontsize=10,
                    bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.7))
    
    # Plot Feigenbaum ratios
    ratio_indices = range(1, len(ratios) + 1)
    ax2.plot(ratio_indices, ratios, 'rs-', markersize=8, linewidth=2, label='Calculated ratios')
    
    # Theoretical Feigenbaum constant
    feigenbaum_const = 4.669201609
    ax2.axhline(y=feigenbaum_const, color='black', linestyle='--', linewidth=2, 
               label=f'Feigenbaum constant δ = {feigenbaum_const:.6f}')
    
    ax2.set_xlabel('Ratio Index', fontsize=12)
    ax2.set_ylabel('δₙ = (rₙ - rₙ₋₁)/(rₙ₊₁ - rₙ)', fontsize=12)
    ax2.set_title('Convergence to Feigenbaum Constant', fontsize=14)
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    ax2.set_ylim(3, 6)
    
    # Add text with ratio values
    ratio_text = "Ratios:\n"
    for i, ratio in enumerate(ratios):
        ratio_text += f"δ₍{i+1}₎ = {ratio:.3f}\n"
    
    ax2.text(0.02, 0.98, ratio_text, transform=ax2.transAxes, 
            verticalalignment='top', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.9))
    
    plt.tight_layout()
    plt.savefig(os.path.join(image_dir, 'feigenbaum_sequence.png'), dpi=300, bbox_inches='tight')
    plt.close()

def chaos_game_fractals():
    """Generate fractals using the chaos game"""
    print("Generating chaos game fractals...")
    
    def sierpinski_triangle():
        """Generate Sierpinski triangle using chaos game"""
        # Triangle vertices
        vertices = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3)/2]])
        
        # Starting point
        point = np.array([0.5, 0.25])
        points = [point.copy()]
        
        # Chaos game iterations
        for _ in range(10000):
            # Choose random vertex
            vertex_idx = np.random.randint(0, 3)
            vertex = vertices[vertex_idx]
            
            # Move halfway to chosen vertex
            point = (point + vertex) / 2
            points.append(point.copy())
        
        return np.array(points)
    
    def dragon_curve_game():
        """Generate dragon curve using chaos game"""
        # Complex plane approach
        points = []
        z = 0 + 0j
        
        for _ in range(15000):
            if np.random.random() < 0.5:
                # Transformation 1: z -> (1+i)*z/2
                z = (1 + 1j) * z / 2
            else:
                # Transformation 2: z -> 1 + (i-1)*z/2
                z = 1 + (1j - 1) * z / 2
            
            points.append([z.real, z.imag])
        
        return np.array(points)
    
    def barnsley_fern():
        """Generate Barnsley fern using chaos game"""
        points = []
        x, y = 0, 0
        
        for _ in range(50000):
            r = np.random.random()
            
            if r < 0.01:
                # Stem
                x_new = 0
                y_new = 0.16 * y
            elif r < 0.86:
                # Successively smaller leaflets
                x_new = 0.85 * x + 0.04 * y
                y_new = -0.04 * x + 0.85 * y + 1.6
            elif r < 0.93:
                # Left leaflet
                x_new = 0.2 * x - 0.26 * y
                y_new = 0.23 * x + 0.22 * y + 1.6
            else:
                # Right leaflet
                x_new = -0.15 * x + 0.28 * y
                y_new = 0.26 * x + 0.24 * y + 0.44
            
            x, y = x_new, y_new
            points.append([x, y])
        
        return np.array(points)
    
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    
    # Sierpinski triangle
    sierpinski_points = sierpinski_triangle()
    axes[0].scatter(sierpinski_points[:, 0], sierpinski_points[:, 1], 
                   s=0.1, c='blue', alpha=0.6)
    axes[0].set_aspect('equal')
    axes[0].set_title('Sierpinski Triangle\n(Chaos Game)', fontsize=14)
    axes[0].set_xlabel('x')
    axes[0].set_ylabel('y')
    
    # Dragon curve
    dragon_points = dragon_curve_game()
    axes[1].scatter(dragon_points[:, 0], dragon_points[:, 1], 
                   s=0.1, c='red', alpha=0.6)
    axes[1].set_aspect('equal')
    axes[1].set_title('Dragon Curve\n(Chaos Game)', fontsize=14)
    axes[1].set_xlabel('x')
    axes[1].set_ylabel('y')
    
    # Barnsley fern
    fern_points = barnsley_fern()
    axes[2].scatter(fern_points[:, 0], fern_points[:, 1], 
                   s=0.05, c='green', alpha=0.8)
    axes[2].set_aspect('equal')
    axes[2].set_title('Barnsley Fern\n(Chaos Game)', fontsize=14)
    axes[2].set_xlabel('x')
    axes[2].set_ylabel('y')
    
    plt.suptitle('Fractal Generation Using Chaos Game', fontsize=16)
    plt.tight_layout()
    plt.savefig(os.path.join(image_dir, 'chaos_game_fractals.png'), dpi=300, bbox_inches='tight')
    plt.close()

def return_maps():
    """Generate return maps for different systems"""
    print("Generating return maps...")
    
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    
    # Logistic map return map
    r_values = [3.2, 3.5, 3.8, 4.0]
    titles = ['Period-2 Cycle', 'Period-4 Cycle', 'Chaotic', 'Fully Chaotic']
    
    for i, (r, title) in enumerate(zip(r_values, titles)):
        ax = axes[i//2, i%2]
        
        # Generate time series
        x = 0.5
        trajectory = []
        
        # Skip transients
        for _ in range(500):
            x = r * x * (1 - x)
        
        # Collect trajectory
        for _ in range(1000):
            x = r * x * (1 - x)
            trajectory.append(x)
        
        # Create return map (x_n vs x_n+1)
        x_n = trajectory[:-1]
        x_n1 = trajectory[1:]
        
        ax.scatter(x_n, x_n1, s=1, alpha=0.6, c='blue')
        
        # Add diagonal and function curve for reference
        x_range = np.linspace(0, 1, 100)
        ax.plot(x_range, x_range, 'k--', alpha=0.5, label='y = x')
        ax.plot(x_range, r * x_range * (1 - x_range), 'r-', alpha=0.7, label=f'y = {r}x(1-x)')
        
        ax.set_xlabel('xₙ', fontsize=12)
        ax.set_ylabel('xₙ₊₁', fontsize=12)
        ax.set_title(f'{title} (r = {r})', fontsize=14)
        ax.grid(True, alpha=0.3)
        ax.legend()
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
    
    plt.suptitle('Return Maps: xₙ₊₁ vs xₙ', fontsize=16)
    plt.tight_layout()
    plt.savefig(os.path.join(image_dir, 'return_maps.png'), dpi=300, bbox_inches='tight')
    plt.close()

def recurrence_plots():
    """Generate recurrence plots for chaotic systems"""
    print("Generating recurrence plots...")
    
    def recurrence_matrix(trajectory, threshold):
        """Calculate recurrence matrix"""
        n = len(trajectory)
        R = np.zeros((n, n))
        
        for i in range(n):
            for j in range(n):
                if abs(trajectory[i] - trajectory[j]) < threshold:
                    R[i, j] = 1
        
        return R
    
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    
    # Different systems
    systems = [
        ('Periodic (r=3.2)', 3.2),
        ('Chaotic (r=3.8)', 3.8),
        ('Sine wave', None),
        ('Random noise', None)
    ]
    
    for i, (name, r) in enumerate(systems):
        ax = axes[i//2, i%2]
        
        if r is not None:
            # Logistic map
            x = 0.5
            trajectory = []
            for _ in range(200):
                x = r * x * (1 - x)
                trajectory.append(x)
        elif 'Sine' in name:
            # Sine wave
            t = np.linspace(0, 4*np.pi, 200)
            trajectory = np.sin(t)
        else:
            # Random noise
            trajectory = np.random.randn(200)
        
        # Calculate recurrence matrix
        threshold = 0.1 * np.std(trajectory)
        R = recurrence_matrix(trajectory, threshold)
        
        # Plot recurrence plot
        ax.imshow(R, cmap='binary', origin='lower')
        ax.set_xlabel('Time i', fontsize=12)
        ax.set_ylabel('Time j', fontsize=12)
        ax.set_title(f'Recurrence Plot: {name}', fontsize=14)
    
    plt.suptitle('Recurrence Plots: Pattern Recognition in Time Series', fontsize=16)
    plt.tight_layout()
    plt.savefig(os.path.join(image_dir, 'recurrence_plots.png'), dpi=300, bbox_inches='tight')
    plt.close()

def chaos_synchronization():
    """Demonstrate synchronization of chaotic systems"""
    print("Generating chaos synchronization...")
    
    def lorenz_system(state, t, sigma=10.0, rho=28.0, beta=8.0/3.0):
        """Lorenz system equations"""
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
    
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    
    # Two Lorenz systems with different initial conditions
    state1 = np.array([1.0, 1.0, 1.0])
    state2 = np.array([1.1, 1.1, 1.1])  # Slightly different
    
    dt = 0.01
    n_steps = 5000
    coupling_start = 2500  # Start coupling halfway through
    coupling_strength = 2.0
    
    t_series = []
    x1_series = []
    x2_series = []
    sync_error = []
    
    for i in range(n_steps):
        t = i * dt
        t_series.append(t)
        x1_series.append(state1[0])
        x2_series.append(state2[0])
        sync_error.append(abs(state1[0] - state2[0]))
        
        # Evolution without coupling
        if i < coupling_start:
            state1 = runge_kutta_4th(lorenz_system, state1, t, dt)
            state2 = runge_kutta_4th(lorenz_system, state2, t, dt)
        else:
            # Evolution with coupling
            # Couple through x-variable
            dx1_coupled = lorenz_system(state1, t) + coupling_strength * (state2[0] - state1[0]) * np.array([1, 0, 0])
            dx2_coupled = lorenz_system(state2, t) + coupling_strength * (state1[0] - state2[0]) * np.array([1, 0, 0])
            
            state1 += dx1_coupled * dt
            state2 += dx2_coupled * dt
    
    # Plot time series
    axes[0,0].plot(t_series, x1_series, 'b-', linewidth=1, label='System 1', alpha=0.8)
    axes[0,0].plot(t_series, x2_series, 'r-', linewidth=1, label='System 2', alpha=0.8)
    axes[0,0].axvline(x=coupling_start*dt, color='green', linestyle='--', 
                     label='Coupling starts')
    axes[0,0].set_xlabel('Time', fontsize=12)
    axes[0,0].set_ylabel('x variable', fontsize=12)
    axes[0,0].set_title('Chaotic System Time Series', fontsize=14)
    axes[0,0].legend()
    axes[0,0].grid(True, alpha=0.3)
    
    # Plot synchronization error
    axes[0,1].semilogy(t_series, sync_error, 'purple', linewidth=2)
    axes[0,1].axvline(x=coupling_start*dt, color='green', linestyle='--', 
                     label='Coupling starts')
    axes[0,1].set_xlabel('Time', fontsize=12)
    axes[0,1].set_ylabel('Synchronization Error', fontsize=12)
    axes[0,1].set_title('Exponential Synchronization', fontsize=14)
    axes[0,1].legend()
    axes[0,1].grid(True, alpha=0.3)
    
    # Phase space before coupling
    mid_point = coupling_start // 2
    axes[1,0].plot(x1_series[:mid_point], x2_series[:mid_point], 'ko', 
                  markersize=1, alpha=0.6)
    axes[1,0].set_xlabel('System 1 (x)', fontsize=12)
    axes[1,0].set_ylabel('System 2 (x)', fontsize=12)
    axes[1,0].set_title('Before Coupling', fontsize=14)
    axes[1,0].grid(True, alpha=0.3)
    
    # Phase space after coupling
    axes[1,1].plot(x1_series[coupling_start:], x2_series[coupling_start:], 'ro', 
                  markersize=1, alpha=0.6)
    # Add synchronization line
    min_val = min(min(x1_series[coupling_start:]), min(x2_series[coupling_start:]))
    max_val = max(max(x1_series[coupling_start:]), max(x2_series[coupling_start:]))
    axes[1,1].plot([min_val, max_val], [min_val, max_val], 'k--', 
                  label='Perfect sync')
    axes[1,1].set_xlabel('System 1 (x)', fontsize=12)
    axes[1,1].set_ylabel('System 2 (x)', fontsize=12)
    axes[1,1].set_title('After Coupling', fontsize=14)
    axes[1,1].legend()
    axes[1,1].grid(True, alpha=0.3)
    
    plt.suptitle('Synchronization of Chaotic Lorenz Systems', fontsize=16)
    plt.tight_layout()
    plt.savefig(os.path.join(image_dir, 'chaos_synchronization.png'), dpi=300, bbox_inches='tight')
    plt.close()

def run_educational_tools():
    """Run all educational visualization tools"""
    print("=" * 70)
    print("CHAOS THEORY EDUCATIONAL TOOLS")
    print("=" * 70)
    
    try:
        butterfly_effect_quantitative()
        feigenbaum_sequence()
        chaos_game_fractals()
        return_maps()
        recurrence_plots()
        chaos_synchronization()
        
        print("\n" + "=" * 70)
        print("ALL EDUCATIONAL TOOLS GENERATED SUCCESSFULLY!")
        print("=" * 70)
        print(f"Images saved to: {image_dir}")
        print("\nEducational tool files:")
        print("- butterfly_effect_quantitative.png")
        print("- feigenbaum_sequence.png")
        print("- chaos_game_fractals.png")
        print("- return_maps.png")
        print("- recurrence_plots.png")
        print("- chaos_synchronization.png")
        
    except Exception as e:
        print(f"Error during educational tools generation: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    run_educational_tools()