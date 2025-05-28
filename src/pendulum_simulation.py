import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from matplotlib.animation import FuncAnimation
import os
from scipy.stats import sem, t

# Get the correct path to the images directories
script_dir = os.path.dirname(os.path.abspath(__file__))
repo_root = os.path.dirname(script_dir)
mechanics_image_dir = os.path.join(repo_root, 'docs', '1 Physics', '1 Mechanics', 'pics')
measurements_image_dir = os.path.join(repo_root, 'docs', '1 Physics', '7 Measurements', 'pics')
os.makedirs(mechanics_image_dir, exist_ok=True)
os.makedirs(measurements_image_dir, exist_ok=True)

def pendulum_system(t, y, b, A, omega_d, omega_0_sq):
    theta, omega = y
    dtheta_dt = omega
    domega_dt = -omega_0_sq * np.sin(theta) - b * omega + A * np.cos(omega_d * t)
    return [dtheta_dt, domega_dt]

def linear_pendulum_system(t, y, b, A, omega_d, omega_0_sq):
    theta, omega = y
    dtheta_dt = omega
    domega_dt = -omega_0_sq * theta - b * omega + A * np.cos(omega_d * t)
    return [dtheta_dt, domega_dt]

def generate_main_plot():
    """Generate the main plot referenced in the markdown as problem2.png"""
    # Parameters for the main demonstration
    g = 9.81  
    L = 1.0  
    omega_0_sq = g / L  
    omega_0 = np.sqrt(omega_0_sq)
    
    b = 0.2  # damping coefficient
    A = 1.2  # driving force amplitude
    omega_d = 2.0  # driving frequency
    y0 = [0.1, 0]  # initial conditions: [theta(0), omega(0)]
    
    t_span = (0, 50)  # simulation time
    t_eval = np.linspace(0, 50, 1000)  # time steps
    
    # Solve the ODE
    sol = solve_ivp(
        lambda t, y: pendulum_system(t, y, b, A, omega_d, omega_0_sq),
        t_span, y0, t_eval=t_eval, method='RK45'
    )
    
    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(sol.t, sol.y[0], 'b-', linewidth=1.5, label='θ(t)')
    plt.xlabel('Time (s)')
    plt.ylabel('Angle (rad)')
    plt.title('Forced Damped Pendulum Motion')
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    # Add parameter information
    plt.text(0.02, 0.98, f'Parameters:\nb = {b}\nA = {A}\nω_d = {omega_d:.1f} rad/s\nω_0 = {omega_0:.2f} rad/s', 
             transform=plt.gca().transAxes, verticalalignment='top',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    
    plt.tight_layout()
    plt.savefig(os.path.join(mechanics_image_dir, 'problem2.png'), dpi=300, bbox_inches='tight')
    plt.close()

def run_comprehensive_analysis():
    """Run the comprehensive pendulum analysis"""
    g = 9.81  
    L = 1.0  
    omega_0_sq = g / L  
    omega_0 = np.sqrt(omega_0_sq)  

    t_span = (0, 50)  
    t_eval = np.linspace(*t_span, 5000)  

    y0 = [0.2, 0]  

    # 1. Effect of damping coefficients
    damping_coefficients = [0.1, 0.5, 1.0, 2.0]
    A = 0.5  
    omega_d = omega_0  

    plt.figure(figsize=(12, 8))

    for i, b in enumerate(damping_coefficients):
        sol = solve_ivp(
            lambda t, y: pendulum_system(t, y, b, A, omega_d, omega_0_sq),
            t_span, y0, t_eval=t_eval, method='RK45'
        )
        
        plt.subplot(2, 2, i+1)
        plt.plot(sol.t, sol.y[0], 'b-')
        plt.grid(True)
        plt.title(f'Damping Coefficient b = {b}')
        plt.xlabel('Time (s)')
        plt.ylabel('Angle (rad)')

    plt.tight_layout()
    plt.savefig(os.path.join(mechanics_image_dir, 'damping_effect.png'), dpi=300, bbox_inches='tight')
    plt.close()

    # 2. Effect of driving amplitudes
    driving_amplitudes = [0.1, 0.5, 1.0, 2.0]
    b = 0.5 

    plt.figure(figsize=(12, 8))

    for i, A in enumerate(driving_amplitudes):
        sol = solve_ivp(
            lambda t, y: pendulum_system(t, y, b, A, omega_d, omega_0_sq),
            t_span, y0, t_eval=t_eval, method='RK45'
        )
        
        plt.subplot(2, 2, i+1)
        plt.plot(sol.t, sol.y[0], 'r-')
        plt.grid(True)
        plt.title(f'Driving Amplitude A = {A}')
        plt.xlabel('Time (s)')
        plt.ylabel('Angle (rad)')

    plt.tight_layout()
    plt.savefig(os.path.join(mechanics_image_dir, 'amplitude_effect.png'), dpi=300, bbox_inches='tight')
    plt.close()

    # 3. Resonance curve analysis
    driving_frequencies = np.linspace(0.5 * omega_0, 1.5 * omega_0, 100)
    b = 0.2  
    A = 0.5  

    t_span_steady = (0, 100) 
    t_eval_steady = np.linspace(80, 100, 1000)  

    amplitudes = []

    for omega_d in driving_frequencies:
        sol = solve_ivp(
            lambda t, y: pendulum_system(t, y, b, A, omega_d, omega_0_sq),
            t_span_steady, y0, t_eval=t_eval_steady, method='RK45'
        )
        
        amplitude = (np.max(sol.y[0]) - np.min(sol.y[0])) / 2
        amplitudes.append(amplitude)

    plt.figure(figsize=(10, 6))
    plt.plot(driving_frequencies / omega_0, amplitudes, 'g-', linewidth=2)
    plt.grid(True)
    plt.axvline(x=1.0, color='r', linestyle='--', label='Natural Frequency')
    plt.xlabel('Driving Frequency / Natural Frequency')
    plt.ylabel('Amplitude (rad)')
    plt.title('Resonance Curve for Forced Damped Pendulum')
    plt.legend()
    plt.savefig(os.path.join(mechanics_image_dir, 'resonance_curve.png'), dpi=300, bbox_inches='tight')
    plt.close()

    # 4. Phase space analysis (potentially chaotic regime)
    b = 0.1  
    A = 1.2 
    omega_d = 2/3 * omega_0  

    t_span_long = (0, 200)
    t_eval_long = np.linspace(*t_span_long, 10000)

    sol_chaotic = solve_ivp(
        lambda t, y: pendulum_system(t, y, b, A, omega_d, omega_0_sq),
        t_span_long, y0, t_eval=t_eval_long, method='RK45'
    )

    plt.figure(figsize=(10, 8))
    plt.subplot(2, 1, 1)
    plt.plot(sol_chaotic.t, sol_chaotic.y[0], 'b-')
    plt.grid(True)
    plt.xlabel('Time (s)')
    plt.ylabel('Angle (rad)')
    plt.title('Angle vs Time (Potentially Chaotic Regime)')

    plt.subplot(2, 1, 2)
    plt.plot(sol_chaotic.y[0], sol_chaotic.y[1], 'r-')
    plt.grid(True)
    plt.xlabel('Angle (rad)')
    plt.ylabel('Angular Velocity (rad/s)')
    plt.title('Phase Space Trajectory')
    plt.tight_layout()
    plt.savefig(os.path.join(mechanics_image_dir, 'phase_space.png'), dpi=300, bbox_inches='tight')
    plt.close()

    # 5. Poincaré section
    driving_period = 2 * np.pi / omega_d
    n_periods = int(t_span_long[1] / driving_period)
    poincare_points = []

    for i in range(n_periods):
        t_target = i * driving_period
        idx = np.argmin(np.abs(sol_chaotic.t - t_target))
        if idx < len(sol_chaotic.t):
            poincare_points.append([sol_chaotic.y[0][idx], sol_chaotic.y[1][idx]])

    poincare_points = np.array(poincare_points)

    plt.figure(figsize=(8, 8))
    plt.scatter(poincare_points[:, 0], poincare_points[:, 1], s=5, c='blue')
    plt.grid(True)
    plt.xlabel('Angle (rad)')
    plt.ylabel('Angular Velocity (rad/s)')
    plt.title('Poincaré Section (Sampled at Driving Period)')
    plt.axis('equal')
    plt.savefig(os.path.join(mechanics_image_dir, 'poincare_section.png'), dpi=300, bbox_inches='tight')
    plt.close()

    # 6. Bifurcation diagram
    A_values = np.linspace(0.1, 1.5, 100)
    b = 0.1  
    omega_d = 2/3 * omega_0  

    t_span_bif = (0, 200)
    t_eval_bif = np.linspace(100, 200, 5000)  

    bifurcation_data = []

    for A_val in A_values:
        sol = solve_ivp(
            lambda t, y: pendulum_system(t, y, b, A_val, omega_d, omega_0_sq),
            t_span_bif, y0, t_eval=t_eval_bif, method='RK45'
        )
        
        driving_period = 2 * np.pi / omega_d
        t_mod = sol.t % driving_period
        indices = np.where(t_mod < driving_period/50)[0]  
        
        for idx in indices:
            bifurcation_data.append([A_val, sol.y[0][idx]])

    bifurcation_data = np.array(bifurcation_data)

    plt.figure(figsize=(10, 6))
    plt.scatter(bifurcation_data[:, 0], bifurcation_data[:, 1], s=0.5, c='black')
    plt.grid(True)
    plt.xlabel('Driving Amplitude (A)')
    plt.ylabel('Angle (rad)')
    plt.title('Bifurcation Diagram (Varying Driving Amplitude)')
    plt.savefig(os.path.join(mechanics_image_dir, 'bifurcation_diagram.png'), dpi=300, bbox_inches='tight')
    plt.close()

    # 7. Linear vs nonlinear comparison
    b = 0.2 
    A = 0.5 
    omega_d = omega_0  

    sol_linear = solve_ivp(
        lambda t, y: linear_pendulum_system(t, y, b, A, omega_d, omega_0_sq),
        t_span, y0, t_eval=t_eval, method='RK45'
    )

    sol_nonlinear = solve_ivp(
        lambda t, y: pendulum_system(t, y, b, A, omega_d, omega_0_sq),
        t_span, y0, t_eval=t_eval, method='RK45'
    )

    plt.figure(figsize=(12, 6))
    plt.plot(sol_linear.t, sol_linear.y[0], 'b-', label='Linear Approximation')
    plt.plot(sol_nonlinear.t, sol_nonlinear.y[0], 'r--', label='Nonlinear Solution')
    plt.grid(True)
    plt.xlabel('Time (s)')
    plt.ylabel('Angle (rad)')
    plt.title('Comparison of Linear and Nonlinear Solutions')
    plt.legend()
    plt.savefig(os.path.join(mechanics_image_dir, 'linear_vs_nonlinear.png'), dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"Comprehensive analysis plots saved to {mechanics_image_dir}")

# ------------------------------------------------------------------------
# Function to simulate a pendulum experiment for measuring gravitational acceleration
# ------------------------------------------------------------------------

def simulate_gravity_measurement():
    """
    Perform pendulum experiment simulation for measuring g and analyze uncertainties
    """
    # Constants and experiment parameters
    L = 1.000  # pendulum length in meters
    L_uncertainty = 0.0005  # half the ruler resolution of 1mm
    true_g = 9.81  # true gravitational acceleration in m/s²
    
    # Calculate the true period for this pendulum
    true_period = 2 * np.pi * np.sqrt(L / true_g)
    
    # Simulate 10 time measurements with realistic human error
    np.random.seed(42)  # For reproducibility
    num_trials = 10
    num_oscillations = 10
    
    # Simulate timing error (human reaction time, etc.)
    human_error_std = 0.05  # standard deviation of timing error in seconds
    
    # Time for 10 oscillations (true value plus random error)
    time_measurements = num_oscillations * true_period + np.random.normal(0, human_error_std, num_trials)
    
    # Round to 2 decimal places to simulate stopwatch precision
    time_measurements = np.round(time_measurements, 2)
    
    # Calculate statistics
    mean_time = np.mean(time_measurements)
    std_time = np.std(time_measurements, ddof=1)  # Sample standard deviation
    sem_time = std_time / np.sqrt(num_trials)  # Standard error of the mean
    
    # Calculate the period of a single oscillation and its uncertainty
    period = mean_time / num_oscillations
    period_uncertainty = sem_time / num_oscillations
    
    # Calculate g from the period using g = 4π²L/T²
    measured_g = 4 * np.pi**2 * L / period**2
    
    # Propagate uncertainties using the formula for relative uncertainty
    # Δg/g = √[(ΔL/L)² + (2ΔT/T)²]
    relative_uncertainty_g = np.sqrt((L_uncertainty/L)**2 + (2*period_uncertainty/period)**2)
    g_uncertainty = relative_uncertainty_g * measured_g
    
    # Calculate percentage contributions to the uncertainty
    length_contribution = ((L_uncertainty/L) / relative_uncertainty_g) * 100
    time_contribution = ((2*period_uncertainty/period) / relative_uncertainty_g) * 100
    
    # Create visualizations
    
    # 1. Time measurements plot
    plt.figure(figsize=(10, 6))
    trials = np.arange(1, num_trials + 1)
    plt.scatter(trials, time_measurements, s=60, color='blue', label='Measurements')
    plt.axhline(mean_time, color='red', linestyle='-', label=f'Mean: {mean_time:.3f} s')
    plt.axhline(mean_time + std_time, color='green', linestyle='--', label=f'± 1 std dev: {std_time:.3f} s')
    plt.axhline(mean_time - std_time, color='green', linestyle='--')
    
    plt.xlabel('Trial Number')
    plt.ylabel('Time for 10 Oscillations (s)')
    plt.title('Pendulum Time Measurements')
    plt.xticks(trials)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(measurements_image_dir, 'pendulum_time_measurements.png'), dpi=300)
    plt.close()
    
    # 2. Uncertainty contributions plot
    plt.figure(figsize=(8, 6))
    categories = ['Length Measurement', 'Time Measurement']
    contributions = [length_contribution, time_contribution]
    
    plt.bar(categories, contributions, color=['#ff9999', '#66b3ff'])
    for i, v in enumerate(contributions):
        plt.text(i, v + 1, f"{v:.1f}%", ha='center')
    
    plt.ylabel('Contribution to Total Uncertainty (%)')
    plt.title('Sources of Uncertainty in Gravitational Acceleration Measurement')
    plt.ylim(0, max(contributions) * 1.2)
    plt.tight_layout()
    plt.savefig(os.path.join(measurements_image_dir, 'pendulum_uncertainty_contributions.png'), dpi=300)
    plt.close()
    
    # 3. Measured vs true g comparison
    plt.figure(figsize=(8, 6))
    plt.errorbar(['Measured g'], [measured_g], yerr=[g_uncertainty], 
                 fmt='o', capsize=6, markersize=10, color='blue', ecolor='black')
    plt.scatter(['True g'], [true_g], marker='s', s=100, color='red')
    
    # Add horizontal lines
    plt.axhline(measured_g, color='blue', linestyle='--', alpha=0.5)
    plt.axhline(true_g, color='red', linestyle='--', alpha=0.5)
    
    # Add shading for error range
    plt.fill_between(['Measured g', 'True g'], 
                     [measured_g - g_uncertainty, measured_g - g_uncertainty],
                     [measured_g + g_uncertainty, measured_g + g_uncertainty], 
                     color='blue', alpha=0.2)
    
    # Add annotations
    diff = abs(measured_g - true_g)
    plt.annotate(f"Difference: {diff:.4f} m/s²", 
                xy=(0.5, (measured_g + true_g) / 2), 
                xytext=(1.1, (measured_g + true_g) / 2),
                arrowprops=dict(arrowstyle="->", color='black'))
    
    plt.ylabel('Gravitational Acceleration (m/s²)')
    plt.title('Measured vs True Gravitational Acceleration')
    plt.grid(True, alpha=0.3)
    
    # Set y limits to focus on the relevant range
    y_min = min(measured_g - g_uncertainty * 1.5, true_g - 0.1)
    y_max = max(measured_g + g_uncertainty * 1.5, true_g + 0.1)
    plt.ylim(y_min, y_max)
    
    plt.tight_layout()
    plt.savefig(os.path.join(measurements_image_dir, 'pendulum_g_comparison.png'), dpi=300)
    plt.close()
    
    # Print results
    print("\n" + "="*50)
    print("PENDULUM GRAVITY MEASUREMENT SIMULATION")
    print("="*50)
    print(f"Pendulum Length: {L:.3f} ± {L_uncertainty:.4f} m")
    print("\nTime Measurements for 10 Oscillations:")
    for i, t in enumerate(time_measurements, 1):
        print(f"Trial {i}: {t:.2f} s")
    
    print(f"\nMean Time for 10 oscillations: {mean_time:.4f} s")
    print(f"Standard Deviation: {std_time:.4f} s")
    print(f"Standard Error of Mean: {sem_time:.4f} s")
    
    print(f"\nPeriod: {period:.4f} ± {period_uncertainty:.4f} s")
    print(f"Measured g: {measured_g:.4f} ± {g_uncertainty:.4f} m/s²")
    print(f"True g: {true_g:.4f} m/s²")
    print(f"Relative Error: {(measured_g - true_g) / true_g * 100:.2f}%")
    
    print(f"\nLength Contribution to Uncertainty: {length_contribution:.1f}%")
    print(f"Timing Contribution to Uncertainty: {time_contribution:.1f}%")
    
    print(f"\nMeasurement images saved to {measurements_image_dir}")

if __name__ == "__main__":
    print("Generating forced damped pendulum visualizations...")
    
    # Generate the main plot referenced in Problem_2.md
    generate_main_plot()
    print("Generated problem2.png")
    
    # Generate comprehensive analysis plots
    run_comprehensive_analysis()
    print("Generated all comprehensive analysis plots")
    
    # Uncomment the following line if you want to run the gravity measurement simulation too
    # simulate_gravity_measurement()
