#!/usr/bin/env python3
"""
Enhanced Deterministic Chaos Visualizations
===========================================

Additional educational visualizations for chaos theory concepts:
1. Interactive chaos vs randomness comparison
2. Fractal dimension calculation demonstration
3. Poincaré sections for different systems
4. Route to chaos animation
5. Real-world chaos examples with data
6. Chaos control demonstration
7. Basin of attraction visualization
8. Multifractal analysis

Author: Physics Class Project - Enhanced Version
Date: 2025
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
from matplotlib.patches import Circle
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

def chaos_vs_randomness_comparison():
    """Create detailed comparison of chaos vs randomness"""
    print("Generating chaos vs randomness comparison...")
    
    fig, axes = plt.subplots(3, 2, figsize=(16, 12))
    
    # Time series comparison
    n_points = 1000
    t = np.arange(n_points)
    
    # Chaotic time series (logistic map)
    x_chaos = 0.5
    chaos_series = []
    for i in range(n_points):
        x_chaos = 3.9 * x_chaos * (1 - x_chaos)
        chaos_series.append(x_chaos)
    
    # Random time series
    random_series = np.random.randn(n_points)
    random_series = 0.5 + 0.2 * random_series  # Scale to similar range
    
    # Plot time series
    axes[0,0].plot(t[:200], chaos_series[:200], 'b-', linewidth=1, label='Chaotic (Logistic)')
    axes[0,0].set_title('Chaotic Time Series', fontsize=14)
    axes[0,0].set_ylabel('Value')
    axes[0,0].grid(True, alpha=0.3)
    
    axes[0,1].plot(t[:200], random_series[:200], 'r-', linewidth=1, label='Random')
    axes[0,1].set_title('Random Time Series', fontsize=14)
    axes[0,1].grid(True, alpha=0.3)
    
    # Autocorrelation comparison
    chaos_autocorr = np.correlate(chaos_series, chaos_series, mode='full')
    chaos_autocorr = chaos_autocorr[chaos_autocorr.size // 2:]
    chaos_autocorr = chaos_autocorr / chaos_autocorr[0]
    
    random_autocorr = np.correlate(random_series, random_series, mode='full')
    random_autocorr = random_autocorr[random_autocorr.size // 2:]
    random_autocorr = random_autocorr / random_autocorr[0]
    
    lags = np.arange(min(100, len(chaos_autocorr)))
    axes[1,0].plot(lags, chaos_autocorr[:len(lags)], 'b-', linewidth=2)
    axes[1,0].set_title('Autocorrelation: Chaos', fontsize=14)
    axes[1,0].set_ylabel('Correlation')
    axes[1,0].grid(True, alpha=0.3)
    
    axes[1,1].plot(lags, random_autocorr[:len(lags)], 'r-', linewidth=2)
    axes[1,1].set_title('Autocorrelation: Random', fontsize=14)
    axes[1,1].grid(True, alpha=0.3)
    
    # Power spectrum comparison
    chaos_fft = np.abs(np.fft.fft(chaos_series))**2
    random_fft = np.abs(np.fft.fft(random_series))**2
    freqs = np.fft.fftfreq(len(chaos_series))
    
    # Plot only positive frequencies
    pos_mask = freqs > 0
    axes[2,0].loglog(freqs[pos_mask], chaos_fft[pos_mask], 'b-', linewidth=1)
    axes[2,0].set_title('Power Spectrum: Chaos', fontsize=14)
    axes[2,0].set_xlabel('Frequency')
    axes[2,0].set_ylabel('Power')
    axes[2,0].grid(True, alpha=0.3)
    
    axes[2,1].loglog(freqs[pos_mask], random_fft[pos_mask], 'r-', linewidth=1)
    axes[2,1].set_title('Power Spectrum: Random', fontsize=14)
    axes[2,1].set_xlabel('Frequency')
    axes[2,1].grid(True, alpha=0.3)
    
    plt.suptitle('Chaos vs Randomness: Detailed Comparison', fontsize=16)
    plt.tight_layout()
    plt.savefig(os.path.join(image_dir, 'chaos_vs_randomness_detailed.png'), dpi=300, bbox_inches='tight')
    plt.close()

def fractal_dimension_demo():
    """Demonstrate fractal dimension calculation"""
    print("Generating fractal dimension demonstration...")
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # Koch snowflake construction
    def koch_snowflake(order, scale=1):
        """Generate Koch snowflake coordinates"""
        def koch_curve(start, end, order):
            if order == 0:
                return [start, end]
            else:
                # Divide line into three parts
                dx = (end[0] - start[0]) / 3
                dy = (end[1] - start[1]) / 3
                
                p1 = start
                p2 = [start[0] + dx, start[1] + dy]
                p4 = [start[0] + 2*dx, start[1] + 2*dy]
                p5 = end
                
                # Third point (top of triangle)
                p3 = [p2[0] + dx/2 - dy*np.sqrt(3)/2, 
                      p2[1] + dy/2 + dx*np.sqrt(3)/2]
                
                # Recursively generate each segment
                curve = []
                curve.extend(koch_curve(p1, p2, order-1)[:-1])
                curve.extend(koch_curve(p2, p3, order-1)[:-1])
                curve.extend(koch_curve(p3, p4, order-1)[:-1])
                curve.extend(koch_curve(p4, p5, order-1))
                
                return curve
        
        # Initial triangle
        points = [[0, 0], [scale, 0], [scale/2, scale*np.sqrt(3)/2], [0, 0]]
        
        if order == 0:
            return points
        
        # Apply Koch curve to each side
        curve = []
        for i in range(3):
            side_curve = koch_curve(points[i], points[i+1], order)
            curve.extend(side_curve[:-1])
        curve.append(curve[0])  # Close the curve
        
        return curve
    
    # Plot Koch snowflakes of different orders
    orders = [0, 1, 2, 3]
    for i, order in enumerate(orders):
        ax = axes[i//2, i%2]
        snowflake = koch_snowflake(order)
        x_coords = [p[0] for p in snowflake]
        y_coords = [p[1] for p in snowflake]
        
        ax.plot(x_coords, y_coords, 'b-', linewidth=2)
        ax.set_aspect('equal')
        ax.set_title(f'Koch Snowflake: Order {order}', fontsize=12)
        ax.grid(True, alpha=0.3)
        
        # Calculate and display perimeter
        perimeter = 0
        for j in range(len(snowflake)-1):
            dx = snowflake[j+1][0] - snowflake[j][0]
            dy = snowflake[j+1][1] - snowflake[j][1]
            perimeter += np.sqrt(dx**2 + dy**2)
        
        ax.text(0.02, 0.98, f'Perimeter: {perimeter:.2f}', 
                transform=ax.transAxes, verticalalignment='top',
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    plt.suptitle('Fractal Dimension: Koch Snowflake Evolution', fontsize=16)
    plt.tight_layout()
    plt.savefig(os.path.join(image_dir, 'fractal_dimension_demo.png'), dpi=300, bbox_inches='tight')
    plt.close()

def poincare_sections():
    """Generate Poincaré sections for different systems"""
    print("Generating Poincaré sections...")
    
    def duffing_oscillator(state, t, alpha=1.0, beta=-1.0, delta=0.3, gamma=0.5, omega=1.0):
        """Duffing oscillator equations"""
        x, y = state
        dx_dt = y
        dy_dt = -delta*y - alpha*x - beta*x**3 + gamma*np.cos(omega*t)
        return np.array([dx_dt, dy_dt])
    
    def runge_kutta_4th(func, state, t, dt, *args):
        """4th order Runge-Kutta integration"""
        k1 = func(state, t, *args)
        k2 = func(state + 0.5*dt*k1, t + 0.5*dt, *args)
        k3 = func(state + 0.5*dt*k2, t + 0.5*dt, *args)
        k4 = func(state + dt*k3, t + dt, *args)
        return state + (dt/6.0) * (k1 + 2*k2 + 2*k3 + k4)
    
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    
    # Different parameter sets for Duffing oscillator
    params = [
        (1.0, -1.0, 0.3, 0.5, 1.0, 'Regular'),
        (1.0, -1.0, 0.3, 1.14, 1.0, 'Period-2'),
        (1.0, -1.0, 0.3, 1.4, 1.0, 'Chaotic')
    ]
    
    for i, (alpha, beta, delta, gamma, omega, label) in enumerate(params):
        # Initial condition
        state = np.array([0.1, 0.1])
        dt = 0.01
        t = 0
        
        # Collect Poincaré section points (when t = 2πn/ω)
        poincare_x = []
        poincare_y = []
        
        # Run for many periods
        period = 2 * np.pi / omega
        n_periods = 200
        steps_per_period = int(period / dt)
        
        # Skip transients
        for _ in range(100 * steps_per_period):
            state = runge_kutta_4th(duffing_oscillator, state, t, dt, alpha, beta, delta, gamma, omega)
            t += dt
        
        # Collect Poincaré points
        for period_num in range(n_periods):
            for _ in range(steps_per_period):
                state = runge_kutta_4th(duffing_oscillator, state, t, dt, alpha, beta, delta, gamma, omega)
                t += dt
            
            # Store point at end of period
            poincare_x.append(state[0])
            poincare_y.append(state[1])
        
        axes[i].plot(poincare_x, poincare_y, 'bo', markersize=1, alpha=0.7)
        axes[i].set_xlabel('Position x', fontsize=12)
        axes[i].set_ylabel('Velocity y', fontsize=12)
        axes[i].set_title(f'Poincaré Section: {label}', fontsize=14)
        axes[i].grid(True, alpha=0.3)
    
    plt.suptitle('Poincaré Sections: Duffing Oscillator', fontsize=16)
    plt.tight_layout()
    plt.savefig(os.path.join(image_dir, 'poincare_sections.png'), dpi=300, bbox_inches='tight')
    plt.close()

def basin_of_attraction():
    """Visualize basin of attraction for a chaotic system"""
    print("Generating basin of attraction...")
    
    def newton_fractal(f, df, roots, x_range, y_range, resolution=400, max_iter=50, tolerance=1e-6):
        """Generate Newton fractal for complex function"""
        x = np.linspace(x_range[0], x_range[1], resolution)
        y = np.linspace(y_range[0], y_range[1], resolution)
        X, Y = np.meshgrid(x, y)
        Z = X + 1j*Y
        
        # Initialize result array
        result = np.zeros(Z.shape, dtype=int)
        
        for i in range(max_iter):
            # Newton's method iteration
            mask = np.abs(f(Z)) > tolerance
            if not np.any(mask):
                break
            
            dZ = df(Z[mask])
            # Avoid division by zero
            dZ[np.abs(dZ) < 1e-15] = 1e-15
            Z[mask] = Z[mask] - f(Z[mask]) / dZ
            
            # Check which root each point is converging to
            for j, root in enumerate(roots):
                root_mask = mask & (np.abs(Z - root) < tolerance)
                result[root_mask] = j + 1
        
        return result
    
    # Define polynomial and its derivative: z^3 - 1 = 0
    def f(z):
        return z**3 - 1
    
    def df(z):
        return 3*z**2
    
    # Roots of z^3 - 1 = 0
    roots = [1, -0.5 + 0.5j*np.sqrt(3), -0.5 - 0.5j*np.sqrt(3)]
    
    # Generate fractal
    fractal = newton_fractal(f, df, roots, (-2, 2), (-2, 2), resolution=600)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
    
    # Plot basin of attraction
    im1 = ax1.imshow(fractal, extent=[-2, 2, -2, 2], cmap='viridis', origin='lower')
    ax1.set_xlabel('Real', fontsize=12)
    ax1.set_ylabel('Imaginary', fontsize=12)
    ax1.set_title('Basin of Attraction: Newton\'s Method for $z^3 - 1 = 0$', fontsize=14)
    
    # Mark the roots
    for i, root in enumerate(roots):
        ax1.plot(root.real, root.imag, 'ro', markersize=10, 
                label=f'Root {i+1}: {root:.2f}')
    ax1.legend()
    
    # Zoom in on fractal boundary
    fractal_zoom = newton_fractal(f, df, roots, (-0.5, 0.5), (-0.5, 0.5), resolution=600)
    im2 = ax2.imshow(fractal_zoom, extent=[-0.5, 0.5, -0.5, 0.5], cmap='viridis', origin='lower')
    ax2.set_xlabel('Real', fontsize=12)
    ax2.set_ylabel('Imaginary', fontsize=12)
    ax2.set_title('Fractal Boundary (Zoomed)', fontsize=14)
    
    plt.tight_layout()
    plt.savefig(os.path.join(image_dir, 'basin_of_attraction.png'), dpi=300, bbox_inches='tight')
    plt.close()

def chaos_control_demo():
    """Demonstrate chaos control techniques"""
    print("Generating chaos control demonstration...")
    
    def controlled_logistic(x, r, control_strength=0, target=0.5):
        """Logistic map with feedback control"""
        uncontrolled = r * x * (1 - x)
        control_term = control_strength * (target - x)
        return uncontrolled + control_term
    
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    
    # Parameters
    r = 3.8  # Chaotic regime
    n_steps = 200
    
    # Different control scenarios
    scenarios = [
        (0, 0.5, 'No Control (Chaotic)'),
        (0.1, 0.5, 'Weak Control'),
        (0.3, 0.5, 'Moderate Control'),
        (0.5, 0.5, 'Strong Control')
    ]
    
    for i, (control_strength, target, title) in enumerate(scenarios):
        ax = axes[i//2, i%2]
        
        # Simulate controlled system
        x = 0.3  # Initial condition
        trajectory = [x]
        
        for _ in range(n_steps):
            x = controlled_logistic(x, r, control_strength, target)
            trajectory.append(x)
        
        # Plot trajectory
        ax.plot(trajectory, 'b-', linewidth=1, alpha=0.8)
        ax.axhline(y=target, color='red', linestyle='--', alpha=0.7, 
                  label=f'Target = {target}')
        ax.set_xlabel('Time Step', fontsize=12)
        ax.set_ylabel('Population x', fontsize=12)
        ax.set_title(title, fontsize=14)
        ax.grid(True, alpha=0.3)
        ax.legend()
        ax.set_ylim(0, 1)
        
        # Add text showing final variance
        final_variance = np.var(trajectory[-50:])  # Last 50 points
        ax.text(0.02, 0.98, f'Final Variance: {final_variance:.4f}', 
                transform=ax.transAxes, verticalalignment='top',
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    plt.suptitle('Chaos Control: Stabilizing Chaotic Systems', fontsize=16)
    plt.tight_layout()
    plt.savefig(os.path.join(image_dir, 'chaos_control_demo.png'), dpi=300, bbox_inches='tight')
    plt.close()

def route_to_chaos_detailed():
    """Detailed visualization of different routes to chaos"""
    print("Generating detailed route to chaos...")
    
    fig, axes = plt.subplots(3, 3, figsize=(18, 15))
    
    # Period-doubling route (logistic map)
    r_values = [2.9, 3.1, 3.45, 3.54, 3.56, 3.57, 3.6, 3.8, 4.0]
    
    for i, r in enumerate(r_values):
        ax = axes[i//3, i%3]
        
        # Generate trajectory
        x = 0.5
        trajectory = []
        
        # Skip transients
        for _ in range(500):
            x = r * x * (1 - x)
        
        # Collect trajectory
        for _ in range(100):
            x = r * x * (1 - x)
            trajectory.append(x)
        
        # Plot trajectory
        ax.plot(range(len(trajectory)), trajectory, 'b-', linewidth=1)
        ax.set_title(f'r = {r}', fontsize=12)
        ax.set_ylabel('x', fontsize=10)
        ax.grid(True, alpha=0.3)
        ax.set_ylim(0, 1)
        
        # Add period information
        if r <= 3.0:
            period_text = "Fixed point"
        elif r <= 3.45:
            period_text = "Period-2"
        elif r <= 3.54:
            period_text = "Period-4"
        elif r <= 3.56:
            period_text = "Period-8"
        elif r <= 3.57:
            period_text = "Higher periods"
        else:
            period_text = "Chaos"
        
        ax.text(0.02, 0.98, period_text, transform=ax.transAxes, 
                verticalalignment='top', fontsize=10,
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    # Add overall xlabel to bottom row
    for ax in axes[2, :]:
        ax.set_xlabel('Time Step', fontsize=10)
    
    plt.suptitle('Period-Doubling Route to Chaos (Logistic Map)', fontsize=16)
    plt.tight_layout()
    plt.savefig(os.path.join(image_dir, 'route_to_chaos_detailed.png'), dpi=300, bbox_inches='tight')
    plt.close()

def real_world_chaos_data():
    """Simulate real-world chaotic data examples"""
    print("Generating real-world chaos examples...")
    
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    
    # 1. Simulated ECG with chaotic arrhythmia
    t_ecg = np.linspace(0, 10, 1000)
    # Normal ECG component
    ecg_normal = 0.5 * np.sin(2*np.pi*1.2*t_ecg)
    # Add chaotic component (simplified)
    x_chaos = 0.5
    chaos_component = []
    for i in range(len(t_ecg)):
        x_chaos = 3.7 * x_chaos * (1 - x_chaos)
        chaos_component.append(x_chaos)
    
    ecg_chaotic = ecg_normal + 0.3 * np.array(chaos_component)
    
    axes[0,0].plot(t_ecg, ecg_chaotic, 'r-', linewidth=1)
    axes[0,0].set_xlabel('Time (s)', fontsize=12)
    axes[0,0].set_ylabel('Amplitude', fontsize=12)
    axes[0,0].set_title('Chaotic Heart Rhythm (Simulated)', fontsize=14)
    axes[0,0].grid(True, alpha=0.3)
    
    # 2. Simulated stock market chaos
    n_days = 252  # Trading days in a year
    returns = []
    price = 100  # Starting price
    
    # Use chaotic map for returns
    x = 0.6
    for i in range(n_days):
        x = 3.9 * x * (1 - x)
        # Transform to realistic return
        daily_return = 0.02 * (x - 0.5)  # ±1% daily returns
        returns.append(daily_return)
        price *= (1 + daily_return)
    
    axes[0,1].plot(range(n_days), returns, 'b-', linewidth=1)
    axes[0,1].set_xlabel('Trading Day', fontsize=12)
    axes[0,1].set_ylabel('Daily Return', fontsize=12)
    axes[0,1].set_title('Chaotic Stock Returns (Simulated)', fontsize=14)
    axes[0,1].grid(True, alpha=0.3)
    
    # 3. Simulated population oscillations
    # Predator-prey with chaotic dynamics
    def predator_prey_chaotic(state, dt, a=1.0, b=0.1, c=1.5, d=0.075):
        x, y = state
        dx = a*x - b*x*y
        dy = -c*y + d*x*y
        # Add nonlinear terms for chaos
        dx += -0.1*x**2
        dy += 0.05*y**2
        return np.array([dx, dy]) * dt
    
    # Simulate population dynamics
    state = np.array([10.0, 5.0])  # Initial populations
    dt = 0.01
    t_pop = []
    prey_pop = []
    pred_pop = []
    
    for i in range(5000):
        t_pop.append(i * dt)
        prey_pop.append(state[0])
        pred_pop.append(state[1])
        state += predator_prey_chaotic(state, dt)
        
        # Prevent negative populations
        state = np.abs(state)
    
    axes[1,0].plot(t_pop, prey_pop, 'g-', linewidth=1, label='Prey')
    axes[1,0].plot(t_pop, pred_pop, 'r-', linewidth=1, label='Predator')
    axes[1,0].set_xlabel('Time', fontsize=12)
    axes[1,0].set_ylabel('Population', fontsize=12)
    axes[1,0].set_title('Chaotic Predator-Prey Dynamics', fontsize=14)
    axes[1,0].legend()
    axes[1,0].grid(True, alpha=0.3)
    
    # 4. Simulated laser intensity chaos
    t_laser = np.linspace(0, 100, 2000)
    # Use Rössler system for laser chaos
    def rossler_system(state, t, a=0.2, b=0.2, c=5.7):
        x, y, z = state
        dx_dt = -y - z
        dy_dt = x + a*y
        dz_dt = b + z*(x - c)
        return np.array([dx_dt, dy_dt, dz_dt])
    
    # Simple integration for demonstration
    state = np.array([1.0, 1.0, 1.0])
    dt = 0.05
    laser_intensity = []
    
    for i in range(len(t_laser)):
        laser_intensity.append(state[0]**2 + state[1]**2)  # Intensity proxy
        if i < len(t_laser) - 1:
            state += rossler_system(state, t_laser[i], 0.2, 0.2, 5.7) * dt
    
    axes[1,1].plot(t_laser, laser_intensity, 'm-', linewidth=1)
    axes[1,1].set_xlabel('Time', fontsize=12)
    axes[1,1].set_ylabel('Intensity', fontsize=12)
    axes[1,1].set_title('Chaotic Laser Intensity', fontsize=14)
    axes[1,1].grid(True, alpha=0.3)
    
    plt.suptitle('Real-World Applications of Chaos Theory', fontsize=16)
    plt.tight_layout()
    plt.savefig(os.path.join(image_dir, 'real_world_chaos_data.png'), dpi=300, bbox_inches='tight')
    plt.close()

def run_enhanced_analysis():
    """Run all enhanced visualizations"""
    print("=" * 70)
    print("ENHANCED DETERMINISTIC CHAOS VISUALIZATIONS")
    print("=" * 70)
    
    try:
        # Generate enhanced visualizations
        chaos_vs_randomness_comparison()
        fractal_dimension_demo()
        poincare_sections()
        basin_of_attraction()
        chaos_control_demo()
        route_to_chaos_detailed()
        real_world_chaos_data()
        
        print("\n" + "=" * 70)
        print("ALL ENHANCED VISUALIZATIONS GENERATED SUCCESSFULLY!")
        print("=" * 70)
        print(f"Images saved to: {image_dir}")
        print("\nNew visualization files:")
        print("- chaos_vs_randomness_detailed.png")
        print("- fractal_dimension_demo.png")
        print("- poincare_sections.png")
        print("- basin_of_attraction.png")
        print("- chaos_control_demo.png")
        print("- route_to_chaos_detailed.png")
        print("- real_world_chaos_data.png")
        
    except Exception as e:
        print(f"Error during enhanced analysis: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    run_enhanced_analysis()