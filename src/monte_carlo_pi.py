import numpy as np
import matplotlib.pyplot as plt
import os
import time
from matplotlib.patches import Circle, Rectangle
from matplotlib.lines import Line2D

def create_directory():
    """Create necessary directory for saving plots."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    plot_dir = os.path.join(repo_root, 'docs', '1 Physics', '6 Statistics', 'pics')
    os.makedirs(plot_dir, exist_ok=True)
    return plot_dir

def circle_monte_carlo(num_points, visualize=False, plot_dir=None, seed=None):
    """
    Estimate π using the circle Monte Carlo method.
    
    Args:
        num_points: Number of random points to generate
        visualize: If True, create visualization of points
        plot_dir: Directory to save visualization plot
        seed: Random seed for reproducibility
        
    Returns:
        Estimated value of π, number of points inside circle
    """
    if seed is not None:
        np.random.seed(seed)
    
    # Generate random points in square from -1 to 1
    x = np.random.uniform(-1, 1, num_points)
    y = np.random.uniform(-1, 1, num_points)
    
    # Calculate distances from origin
    distances = x**2 + y**2
    
    # Count points inside unit circle
    inside_circle = distances <= 1
    count_inside = np.sum(inside_circle)
    
    # Estimate π
    pi_estimate = 4 * count_inside / num_points
    
    # Create visualization if requested
    if visualize and plot_dir:
        fig, ax = plt.subplots(figsize=(10, 10))
        
        # Plot circle and square
        square = Rectangle((-1, -1), 2, 2, fill=False, edgecolor='black', lw=2)
        circle = Circle((0, 0), 1, fill=False, edgecolor='black', lw=2)
        ax.add_patch(square)
        ax.add_patch(circle)
        
        # Plot points
        ax.scatter(x[inside_circle], y[inside_circle], color='blue', s=5, alpha=0.6, label='Inside Circle')
        ax.scatter(x[~inside_circle], y[~inside_circle], color='red', s=5, alpha=0.6, label='Outside Circle')
        
        # Add annotations
        ax.set_aspect('equal')
        ax.set_xlim(-1.1, 1.1)
        ax.set_ylim(-1.1, 1.1)
        ax.set_title(f'Monte Carlo Estimation of π\nPoints: {num_points}, Estimate: {pi_estimate:.6f}')
        ax.legend()
        
        # Save figure
        plt.savefig(os.path.join(plot_dir, 'circle_monte_carlo.png'), dpi=300, bbox_inches='tight')
        plt.close(fig)
    
    return pi_estimate, count_inside

def buffons_needle(num_throws, needle_length=1, line_distance=2, visualize=False, plot_dir=None, seed=None):
    """
    Estimate π using Buffon's Needle method.
    
    Args:
        num_throws: Number of needles to randomly throw
        needle_length: Length of needle
        line_distance: Distance between parallel lines
        visualize: If True, create visualization of needles
        plot_dir: Directory to save visualization plot
        seed: Random seed for reproducibility
        
    Returns:
        Estimated value of π, number of needles crossing lines
    """
    if seed is not None:
        np.random.seed(seed)
    
    # Generate random needle positions and angles
    # y: distance from needle center to nearest line
    # theta: angle of needle with horizontal
    y = np.random.uniform(0, line_distance/2, num_throws)  # Only need to simulate up to half the distance between lines
    theta = np.random.uniform(0, np.pi, num_throws)
    
    # For Buffon's needle, a crossing occurs when:
    # distance from nearest line <= (L/2) * sin(θ)
    half_length = needle_length / 2
    crosses = y <= half_length * np.sin(theta)
    num_crosses = np.sum(crosses)
    
    # Estimate π using the formula: π ≈ (2L*n)/(D*c)
    # where L = needle length, D = line distance, n = throws, c = crossings
    if num_crosses > 0:  # Avoid division by zero
        pi_estimate = (2 * needle_length * num_throws) / (line_distance * num_crosses)
    else:
        pi_estimate = np.nan
    
    # Create visualization if requested
    if visualize and plot_dir:
        # Only visualize a subset for clarity
        max_display = min(300, num_throws)
        
        fig, ax = plt.subplots(figsize=(12, 8))
        
        # Draw parallel lines
        num_lines = 5
        for i in range(num_lines + 1):
            ax.axhline(y=i * line_distance, color='black', linestyle='-', alpha=0.7)
        
        # Draw needles (as line segments)
        for i in range(max_display):
            # Position of needle center (x is arbitrary since we're looking at y-position only)
            center_x = np.random.uniform(1, num_lines * line_distance - 1)
            # For visualization, we need to map y back to the full space
            center_y = np.random.uniform(0, line_distance * num_lines)
            
            # Ensure we know if this needle crosses a line in the visualization
            nearest_line = line_distance * round(center_y / line_distance)
            dist_to_line = abs(center_y - nearest_line)
            crosses_line = dist_to_line <= half_length * np.sin(theta[i])
            
            # Calculate needle endpoints
            dx = half_length * np.cos(theta[i])
            dy = half_length * np.sin(theta[i])
            
            x1, y1 = center_x - dx, center_y - dy
            x2, y2 = center_x + dx, center_y + dy
            
            # Draw needle
            if crosses_line:
                ax.plot([x1, x2], [y1, y2], 'r-', lw=1.5, alpha=0.7)
            else:
                ax.plot([x1, x2], [y1, y2], 'b-', lw=1.5, alpha=0.7)
        
        # Labels and legend
        ax.set_title(f"Buffon's Needle Method\nNeedles: {num_throws}, Crossings: {num_crosses}, π ≈ {pi_estimate:.6f}")
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        
        # Custom legend
        red_line = Line2D([0], [0], color='red', lw=2, label='Crossing')
        blue_line = Line2D([0], [0], color='blue', lw=2, label='Not Crossing')
        ax.legend(handles=[red_line, blue_line])
        
        # Set limits with some padding
        ax.set_xlim(0, num_lines * line_distance)
        ax.set_ylim(0, num_lines * line_distance)
        
        # Save figure
        plt.savefig(os.path.join(plot_dir, 'buffons_needle.png'), dpi=300, bbox_inches='tight')
        plt.close(fig)
    
    return pi_estimate, num_crosses

def convergence_analysis(method_func, sample_sizes, iterations=3, **kwargs):
    """
    Analyze convergence of π estimates as sample size increases.
    
    Args:
        method_func: Function implementing estimation method
        sample_sizes: List of sample sizes to test
        iterations: Number of trials to run for each sample size
        **kwargs: Additional parameters for method_func
        
    Returns:
        Array of sample sizes, array of π estimates, array of errors, array of execution times
    """
    estimates = np.zeros(len(sample_sizes))
    abs_errors = np.zeros(len(sample_sizes))
    exec_times = np.zeros(len(sample_sizes))
    
    for i, n in enumerate(sample_sizes):
        start_time = time.time()
        
        # Run multiple iterations and average
        pi_values = []
        for j in range(iterations):
            # Use different seeds for each iteration
            seed = 42 + j
            pi_est, _ = method_func(n, seed=seed, **kwargs)
            if not np.isnan(pi_est):  # Skip NaN values (might occur in Buffon's method)
                pi_values.append(pi_est)
        
        # Calculate average and error
        if pi_values:
            estimates[i] = np.mean(pi_values)
            abs_errors[i] = np.abs(estimates[i] - np.pi)
        else:
            estimates[i] = np.nan
            abs_errors[i] = np.nan
        
        exec_times[i] = time.time() - start_time
    
    return sample_sizes, estimates, abs_errors, exec_times

def plot_convergence(sample_sizes, estimates, errors, method_name, plot_dir):
    """
    Plot convergence of π estimates as sample size increases.
    
    Args:
        sample_sizes: Array of sample sizes
        estimates: Array of π estimates
        errors: Array of absolute errors
        method_name: Name of the method for plot title
        plot_dir: Directory to save plots
    """
    # Create convergence plot
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12), sharex=True)
    
    # Plot estimates
    ax1.semilogx(sample_sizes, estimates, 'o-', lw=2, label=f'{method_name} Estimate')
    ax1.axhline(y=np.pi, color='r', linestyle='--', alpha=0.7, label='True π')
    
    ax1.set_ylabel('Estimated π')
    ax1.set_title(f'Convergence of {method_name} Method')
    ax1.legend()
    ax1.grid(True, which="both", ls="-", alpha=0.2)
    
    # Plot errors on log-log scale
    ax2.loglog(sample_sizes, errors, 'o-', lw=2, label='Absolute Error')
    
    # Add reference line with 1/√N slope (expected convergence rate)
    if not np.any(np.isnan(errors)):
        ref_point = errors[0]  # Use first error as reference
        ref_n = sample_sizes[0]
        reference_y = ref_point * np.sqrt(ref_n) / np.sqrt(sample_sizes)
        ax2.loglog(sample_sizes, reference_y, 'k--', alpha=0.5, label='1/√N Reference')
    
    ax2.set_xlabel('Number of Samples (N)')
    ax2.set_ylabel('Absolute Error')
    ax2.legend()
    ax2.grid(True, which="both", ls="-", alpha=0.2)
    
    plt.tight_layout()
    plt.savefig(os.path.join(plot_dir, f'{method_name.lower().replace(" ", "_")}_convergence.png'), dpi=300)
    plt.close(fig)

def compare_methods(circle_data, buffon_data, plot_dir):
    """
    Create comparison plot of both methods.
    
    Args:
        circle_data: (sample_sizes, estimates, errors, times) for circle method
        buffon_data: (sample_sizes, estimates, errors, times) for Buffon's method
        plot_dir: Directory to save plots
    """
    circle_sizes, circle_estimates, circle_errors, circle_times = circle_data
    buffon_sizes, buffon_estimates, buffon_errors, buffon_times = buffon_data
    
    # Create comparison plot
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True)
    
    # Plot errors
    ax1.loglog(circle_sizes, circle_errors, 'o-', lw=2, label='Circle Method')
    ax1.loglog(buffon_sizes, buffon_errors, 's-', lw=2, label="Buffon's Needle Method")
    
    # Add reference line with 1/√N slope
    if not np.any(np.isnan(circle_errors)) and not np.any(np.isnan(buffon_errors)):
        ref_point = min(circle_errors[0], buffon_errors[0]) * 2  # Use higher of first errors as reference, scaled up
        ref_n = circle_sizes[0]
        reference_y = ref_point * np.sqrt(ref_n) / np.sqrt(circle_sizes)
        ax1.loglog(circle_sizes, reference_y, 'k--', alpha=0.5, label='1/√N Reference')
    
    ax1.set_ylabel('Absolute Error')
    ax1.set_title('Comparison of Monte Carlo Methods for π Estimation')
    ax1.legend()
    ax1.grid(True, which="both", ls="-", alpha=0.2)
    
    # Plot execution times
    ax2.loglog(circle_sizes, circle_times, 'o-', lw=2, label='Circle Method')
    ax2.loglog(buffon_sizes, buffon_times, 's-', lw=2, label="Buffon's Needle Method")
    
    ax2.set_xlabel('Number of Samples (N)')
    ax2.set_ylabel('Execution Time (seconds)')
    ax2.legend()
    ax2.grid(True, which="both", ls="-", alpha=0.2)
    
    plt.tight_layout()
    plt.savefig(os.path.join(plot_dir, 'methods_comparison.png'), dpi=300)
    plt.close(fig)

def main():
    # Set up
    np.random.seed(42)  # For reproducibility
    plot_dir = create_directory()
    
    # Sample sizes for analysis
    sample_sizes = [100, 1000, 10000, 100000, 1000000]
    
    print("Monte Carlo π Estimation")
    print("=" * 50)
    print("\nRunning Circle Monte Carlo Method...")
    
    # Circle Monte Carlo visualization
    circle_monte_carlo(10000, visualize=True, plot_dir=plot_dir)
    
    # Circle Monte Carlo convergence analysis
    circle_data = convergence_analysis(circle_monte_carlo, sample_sizes)
    plot_convergence(circle_data[0], circle_data[1], circle_data[2], "Circle Monte Carlo", plot_dir)
    
    print("\nCircle Monte Carlo Results:")
    print("Sample Size\tπ Estimate\tAbsolute Error\tExecution Time")
    for i, n in enumerate(circle_data[0]):
        print(f"{n:,}\t\t{circle_data[1][i]:.6f}\t{circle_data[2][i]:.6f}\t{circle_data[3][i]:.4f}s")
    
    print("\nRunning Buffon's Needle Method...")
    
    # Buffon's Needle visualization
    buffons_needle(300, visualize=True, plot_dir=plot_dir)
    
    # Buffon's Needle convergence analysis
    buffon_data = convergence_analysis(buffons_needle, sample_sizes)
    plot_convergence(buffon_data[0], buffon_data[1], buffon_data[2], "Buffon's Needle", plot_dir)
    
    print("\nBuffon's Needle Results:")
    print("Sample Size\tπ Estimate\tAbsolute Error\tExecution Time")
    for i, n in enumerate(buffon_data[0]):
        print(f"{n:,}\t\t{buffon_data[1][i]:.6f}\t{buffon_data[2][i]:.6f}\t{buffon_data[3][i]:.4f}s")
    
    # Compare methods
    compare_methods(circle_data, buffon_data, plot_dir)
    
    print("\nComparison completed. All plots saved to", plot_dir)

if __name__ == "__main__":
    main()