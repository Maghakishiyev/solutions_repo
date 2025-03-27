import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm 

population_size = 100000  
n_samples = 10000       
sample_sizes = [5, 10, 30, 50, 100]

low_uni, high_uni = 0, 10
pop_uniform = np.random.uniform(low_uni, high_uni, population_size)
mean_pop_uniform = np.mean(pop_uniform)
var_pop_uniform = np.var(pop_uniform)

scale_exp = 2.0
pop_exponential = np.random.exponential(scale=scale_exp, size=population_size)
mean_pop_exponential = np.mean(pop_exponential)
var_pop_exponential = np.var(pop_exponential)

n_trials_binom, p_binom = 10, 0.3
pop_binomial = np.random.binomial(n_trials_binom, p_binom, population_size)
mean_pop_binomial = np.mean(pop_binomial)
var_pop_binomial = np.var(pop_binomial)

populations = {
    "Uniform(0, 10)": {
        "data": pop_uniform,
        "mean": mean_pop_uniform,
        "var": var_pop_uniform,
        "color": "blue"
    },
    "Exponential(scale=2)": {
        "data": pop_exponential,
        "mean": mean_pop_exponential,
        "var": var_pop_exponential,
        "color": "green"
    },
    "Binomial(n=10, p=0.3)": {
        "data": pop_binomial,
        "mean": mean_pop_binomial,
        "var": var_pop_binomial,
        "color": "red"
    }
}

sns.set_theme()

for dist_name, pop_info in populations.items():
    print(f"--- Simulating for {dist_name} Distribution ---")
    population_data = pop_info["data"]
    pop_mean = pop_info["mean"]
    pop_var = pop_info["var"]
    color = pop_info["color"]

    fig, axes = plt.subplots(1, len(sample_sizes), figsize=(5 * len(sample_sizes), 5), sharey=True)
    fig.suptitle(f'Sampling Distribution of the Mean ({dist_name})', fontsize=16)

    for i, n in enumerate(sample_sizes):
        sample_means = []
        for _ in range(n_samples):
            sample = np.random.choice(population_data, size=n, replace=True)
            sample_means.append(np.mean(sample))

        ax = axes[i]
        sns.histplot(sample_means, bins=30, kde=True, ax=ax, color=color, stat="density")

        clt_mean = pop_mean
        clt_std_dev = np.sqrt(pop_var / n)

        x_norm = np.linspace(clt_mean - 4*clt_std_dev, clt_mean + 4*clt_std_dev, 100)
        y_norm = norm.pdf(x_norm, clt_mean, clt_std_dev)
        ax.plot(x_norm, y_norm, 'k--', linewidth=2, label='Theoretical Normal (CLT)')

        ax.set_title(f'n = {n}')
        ax.set_xlabel('Sample Mean')
        if i == 0:
            ax.set_ylabel('Density')
        ax.legend()

    plt.tight_layout(rect=[0, 0.03, 1, 0.95]) 
    plot_filename = f"clt_simulation_{dist_name.split('(')[0]}.png"
    plt.savefig(plot_filename)
    print(f"Saved plot: {plot_filename}")

print("Simulations complete. Plots saved.")
