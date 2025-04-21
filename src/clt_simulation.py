import numpy as np
import matplotlib.pyplot as plt
import os
import scipy.stats as stats

def plot_sampling_distribution(data, sample_sizes, distribution_name, save_path, n_simulations=10000):
    """
    Plots the sampling distribution of the mean for different sample sizes.
    
    Args:
        data: The population data
        sample_sizes: List of sample sizes to test
        distribution_name: Name of the distribution for plot titles
        save_path: Path to save the figure
        n_simulations: Number of times to draw a sample and calculate the mean
    """
    # Calculate population parameters for reference
    pop_mean = np.mean(data)
    pop_std = np.std(data, ddof=1)
    
    # Create figure with subplots
    fig, axes = plt.subplots(2, len(sample_sizes)//2, figsize=(15, 10))
    axes = axes.flatten()
    
    fig.suptitle(f'Sampling Distribution of the Mean for {distribution_name} Distribution', fontsize=16)
    
    # Add a small subplot for the original distribution
    orig_dist_ax = fig.add_axes([0.15, 0.02, 0.7, 0.1])  # [left, bottom, width, height]
    
    # Plot original distribution
    orig_dist_ax.hist(data[:min(10000, len(data))], bins=50, alpha=0.7, density=True, color='gray')
    orig_dist_ax.set_title(f'Original {distribution_name} Distribution', fontsize=12)
    orig_dist_ax.set_xlabel('Value')
    orig_dist_ax.set_ylabel('Density')
    orig_dist_ax.grid(alpha=0.3)
    
    # For each sample size, simulate sampling distribution
    for i, n in enumerate(sample_sizes):
        sample_means = []
        for _ in range(n_simulations):
            # Draw n samples with replacement
            samples = np.random.choice(data, size=n, replace=True)
            sample_means.append(np.mean(samples))
        
        # Calculate theoretical parameters
        se = pop_std / np.sqrt(n)  # Standard error
        
        # Plot histogram of sample means
        axes[i].hist(sample_means, bins=50, density=True, alpha=0.7, color='skyblue')
        
        # Plot normal distribution with same mean and standard error
        x = np.linspace(min(sample_means), max(sample_means), 1000)
        axes[i].plot(x, stats.norm.pdf(x, pop_mean, se), 'r-', linewidth=2, 
                    label=f'Normal PDF\nμ={pop_mean:.2f}, σ={se:.2f}')
        
        # Add annotations
        axes[i].axvline(pop_mean, color='green', linestyle='--', alpha=0.7, 
                      label=f'Population mean: {pop_mean:.2f}')
        
        # Calculate summary statistics
        mean_of_means = np.mean(sample_means)
        std_of_means = np.std(sample_means, ddof=1)
        
        # Add textbox with statistics
        props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
        textstr = f'n = {n}\nMean of means: {mean_of_means:.4f}\nStd of means: {std_of_means:.4f}\nSE (theory): {se:.4f}'
        axes[i].text(0.05, 0.95, textstr, transform=axes[i].transAxes, fontsize=10,
                verticalalignment='top', bbox=props)
        
        axes[i].set_title(f'Sample Size N = {n}')
        axes[i].set_xlabel('Sample Mean')
        axes[i].set_ylabel('Density')
        axes[i].legend(fontsize=8)
        axes[i].grid(alpha=0.3)
    
    plt.tight_layout()
    plt.subplots_adjust(top=0.9, bottom=0.15)  # Make room for original distribution
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    # Save figure
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close(fig)

# Plot the original distributions separately
def plot_original_distributions(distributions, save_path):
    """
    Plots the original distributions side by side for comparison.
    
    Args:
        distributions: Dictionary of {name: data}
        save_path: Path to save the figure
    """
    fig, axes = plt.subplots(1, len(distributions), figsize=(15, 5))
    
    for i, (name, data) in enumerate(distributions.items()):
        axes[i].hist(data[:min(10000, len(data))], bins=50, alpha=0.7, density=True)
        axes[i].set_title(f'{name} Distribution')
        axes[i].set_xlabel('Value')
        axes[i].set_ylabel('Density')
        
        # Add mean and std annotations
        mean = np.mean(data)
        std = np.std(data, ddof=1)
        
        props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
        textstr = f'Mean: {mean:.2f}\nStd: {std:.2f}'
        axes[i].text(0.05, 0.95, textstr, transform=axes[i].transAxes, fontsize=10,
                    verticalalignment='top', bbox=props)
    
    plt.tight_layout()
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    # Save figure
    plt.savefig(save_path, dpi=300)
    plt.close(fig)

# --- Main execution ---
if __name__ == "__main__":
    # Define sample sizes to test
    sample_sizes = [5, 10, 30, 50]
    
    # Set random seed for reproducibility
    np.random.seed(42)
    
    # Population size
    population_size = 100000
    
    # Define directory to save plots
    plot_dir = os.path.join('docs', '1 Physics', '6 Statistics', 'pics')
    os.makedirs(plot_dir, exist_ok=True)
    
    # 1. Generate population data for different distributions
    
    # Uniform distribution (0, 1)
    uniform_data = np.random.uniform(0, 1, population_size)
    
    # Exponential distribution (lambda=1.5)
    exponential_data = np.random.exponential(scale=1/1.5, size=population_size)
    
    # Binomial distribution (n=10, p=0.3)
    binomial_n = 10
    binomial_p = 0.3
    binomial_data = np.random.binomial(binomial_n, binomial_p, population_size)
    
    # Store all distributions in a dictionary
    distributions = {
        "Uniform": uniform_data,
        "Exponential": exponential_data,
        "Binomial": binomial_data
    }
    
    # Plot original distributions side by side
    plot_original_distributions(distributions, os.path.join(plot_dir, 'original_distributions.png'))
    
    # 2. For each distribution, plot sampling distributions for different sample sizes
    plot_sampling_distribution(uniform_data, sample_sizes, 'Uniform', 
                              os.path.join(plot_dir, 'uniform_clt.png'))
    
    plot_sampling_distribution(exponential_data, sample_sizes, 'Exponential', 
                              os.path.join(plot_dir, 'exponential_clt.png'))
    
    plot_sampling_distribution(binomial_data, sample_sizes, 'Binomial', 
                              os.path.join(plot_dir, 'binomial_clt.png'))
    
    # 3. Bonus: Create a more comprehensive visualization showing convergence
    # Define more granular sample sizes for detailed convergence plot
    detailed_sample_sizes = [2, 5, 10, 20, 30, 50, 100]
    
    # Plot convergence of standard error for all distributions
    fig, ax = plt.subplots(figsize=(10, 6))
    
    for name, data in distributions.items():
        pop_std = np.std(data, ddof=1)
        
        # For each sample size, calculate the empirical standard error
        empirical_ses = []
        theoretical_ses = []
        
        for n in detailed_sample_sizes:
            sample_means = []
            for _ in range(2000):  # Fewer simulations for speed
                samples = np.random.choice(data, size=n, replace=True)
                sample_means.append(np.mean(samples))
            
            # Calculate empirical standard error (std dev of sampling distribution)
            empirical_se = np.std(sample_means, ddof=1)
            empirical_ses.append(empirical_se)
            
            # Calculate theoretical standard error
            theoretical_se = pop_std / np.sqrt(n)
            theoretical_ses.append(theoretical_se)
        
        # Plot empirical standard errors
        ax.plot(detailed_sample_sizes, empirical_ses, 'o-', label=f'{name} (Empirical)')
        
        # Plot theoretical standard errors
        ax.plot(detailed_sample_sizes, theoretical_ses, '--', alpha=0.7, 
                label=f'{name} (Theoretical: σ/√n)')
    
    # Add reference line showing 1/√n relationship
    reference_x = np.array(detailed_sample_sizes)
    reference_y = 0.3 / np.sqrt(reference_x)  # Scaled for visibility
    ax.plot(reference_x, reference_y, 'k--', alpha=0.5, label='1/√n relationship')
    
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlabel('Sample Size (n)')
    ax.set_ylabel('Standard Error of the Mean')
    ax.set_title('Convergence of Standard Error with Increasing Sample Size')
    ax.legend()
    ax.grid(True, which="both", ls="-", alpha=0.2)
    
    plt.tight_layout()
    plt.savefig(os.path.join(plot_dir, 'standard_error_convergence.png'), dpi=300)
    plt.close(fig)
    
    print("CLT simulations complete. Plots saved in {}".format(plot_dir))