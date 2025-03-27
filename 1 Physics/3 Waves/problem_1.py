import numpy as np
import matplotlib.pyplot as plt
import os
from mpl_toolkits.mplot3d import Axes3D  # Needed for 3D plotting
from matplotlib import cm

# Create directory for pics if it doesn't exist
image_dir = os.path.join('docs', '1 Physics', '3 Waves', 'pics')
os.makedirs(image_dir, exist_ok=True)

# Constants and parameters
A = 1.0        # Amplitude
lamb = 0.5     # Wavelength (lambda)
f = 1.0        # Frequency
k = 2 * np.pi / lamb  # Wave number
omega = 2 * np.pi * f  # Angular frequency
phi = 0        # Initial phase

# Function to calculate the displacement at a point due to a single source
def calculate_displacement(x, y, t, source_pos):
    """
    Calculate the displacement of the water surface at point (x, y) and time t
    due to a wave from a source at source_pos.
    """
    x0, y0 = source_pos
    r = np.sqrt((x - x0)**2 + (y - y0)**2)
    # Avoid division by zero at the source
    if r < 1e-10:
        return 0
    return A / np.sqrt(r) * np.cos(k * r - omega * t + phi)

# Function to calculate the total displacement due to multiple sources
def calculate_total_displacement(x, y, t, sources):
    total = 0
    for source_pos in sources:
        total += calculate_displacement(x, y, t, source_pos)
    return total

# Function to generate the vertices of a regular polygon
def generate_polygon_vertices(n, radius=1.0, center=(0, 0)):
    vertices = []
    for i in range(n):
        angle = 2 * np.pi * i / n
        x = center[0] + radius * np.cos(angle)
        y = center[1] + radius * np.sin(angle)
        vertices.append((x, y))
    return vertices

# Function to analyze interference patterns and generate plots
def analyze_polygon_interference():
    # Define the grid for plotting
    x = np.linspace(-3, 3, 400)
    y = np.linspace(-3, 3, 400)
    X, Y = np.meshgrid(x, y)
    t = 0  # Time snapshot
    
    # Define polygon configurations: shape name and number of vertices
    polygons = {
        'triangle': 3,
        'square': 4,
        'pentagon': 5,
        'hexagon': 6
    }
    
    # Loop through each polygon configuration
    for shape, num_vertices in polygons.items():
        # Generate the source positions for the polygon
        sources = generate_polygon_vertices(num_vertices, radius=1.0, center=(0, 0))
        
        # Calculate total displacement at each grid point
        Z = np.zeros_like(X)
        for i in range(X.shape[0]):
            for j in range(X.shape[1]):
                Z[i, j] = calculate_total_displacement(X[i, j], Y[i, j], t, sources)
        
        # Generate and save 2D contour plot
        plt.figure(figsize=(6, 6))
        contour = plt.contourf(X, Y, Z, 50, cmap='viridis')
        plt.colorbar(contour)
        plt.title(f'{shape.capitalize()} Interference Pattern (2D)')
        two_d_path = os.path.join(image_dir, f'{shape}_interference_2d.png')
        plt.savefig(two_d_path)
        plt.close()
        
        # Generate and save 3D surface plot
        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(111, projection='3d')
        surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
        fig.colorbar(surf)
        ax.set_title(f'{shape.capitalize()} Interference Pattern (3D)')
        three_d_path = os.path.join(image_dir, f'{shape}_interference_3d.png')
        plt.savefig(three_d_path)
        plt.close()
    
    print("Interference patterns generated and saved to:", image_dir)

# Main function
if __name__ == "__main__":
    analyze_polygon_interference()
    print("All simulations and visualizations completed.")
    print(f"pics saved to {image_dir}")
