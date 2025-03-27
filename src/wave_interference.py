import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import os
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

image_dir = os.path.join('docs', '1 Physics', '3 Waves', 'pics')
os.makedirs(image_dir, exist_ok=True)

A = 1.0  
lamb = 0.5  
f = 1.0  
k = 2 * np.pi / lamb  
omega = 2 * np.pi * f  
phi = 0  

def calculate_displacement(x, y, t, source_pos):
    x0, y0 = source_pos
    r = np.sqrt((x - x0)**2 + (y - y0)**2)
    if r < 1e-10:
        return 0
    return A / np.sqrt(r) * np.cos(k * r - omega * t + phi)

def calculate_total_displacement(x, y, t, sources):
    total = 0
    for source_pos in sources:
        total += calculate_displacement(x, y, t, source_pos)
    return total

def generate_polygon_vertices(n, radius=1.0, center=(0, 0)):
    vertices = []
    for i in range(n):
        angle = 2 * np.pi * i / n
        x = center[0] + radius * np.cos(angle)
        y = center[1] + radius * np.sin(angle)
        vertices.append((x, y))
    return vertices

def plot_interference_pattern(sources, title, save_path=None, t=0, grid_size=100, plot_range=(-5, 5)):
    x = np.linspace(plot_range[0], plot_range[1], grid_size)
    y = np.linspace(plot_range[0], plot_range[1], grid_size)
    X, Y = np.meshgrid(x, y)
    
    Z = np.zeros_like(X)
    for i in range(grid_size):
        for j in range(grid_size):
            Z[i, j] = calculate_total_displacement(X[i, j], Y[i, j], t, sources)
    
    fig, ax = plt.subplots(figsize=(10, 8))
    
    im = ax.imshow(Z, extent=[plot_range[0], plot_range[1], plot_range[0], plot_range[1]],
                  cmap='coolwarm', origin='lower', vmin=-3*A, vmax=3*A)
    
    cbar = fig.colorbar(im, ax=ax)
    cbar.set_label('Displacement')
    
    for i, source in enumerate(sources):
        ax.plot(source[0], source[1], 'ko', markersize=5)
        ax.text(source[0]+0.1, source[1]+0.1, f'S{i+1}', fontsize=10)
    
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)
    ax.set_title(title, fontsize=14)
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    return fig, ax

def plot_3d_interference_pattern(sources, title, save_path=None, t=0, grid_size=100, plot_range=(-5, 5)):
    x = np.linspace(plot_range[0], plot_range[1], grid_size)
    y = np.linspace(plot_range[0], plot_range[1], grid_size)
    X, Y = np.meshgrid(x, y)
    
    Z = np.zeros_like(X)
    for i in range(grid_size):
        for j in range(grid_size):
            Z[i, j] = calculate_total_displacement(X[i, j], Y[i, j], t, sources)
    
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=True)
    
    cbar = fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)
    cbar.set_label('Displacement')
    
    for i, source in enumerate(sources):
        ax.plot([source[0], source[0]], [source[1], source[1]], [-3*A, 3*A], 'k-', linewidth=1)
        ax.text(source[0], source[1], 3*A, f'S{i+1}', fontsize=10)
    
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)
    ax.set_zlabel('Displacement', fontsize=12)
    ax.set_title(title, fontsize=14)
    
    ax.set_zlim(-3*A, 3*A)
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    return fig, ax

def create_interference_animation(sources, title, save_path=None, duration=2.0, fps=20, grid_size=100, plot_range=(-5, 5)):
    fig, ax = plt.subplots(figsize=(10, 8))
    
    x = np.linspace(plot_range[0], plot_range[1], grid_size)
    y = np.linspace(plot_range[0], plot_range[1], grid_size)
    X, Y = np.meshgrid(x, y)
    
    n_frames = int(duration * fps)
    times = np.linspace(0, duration, n_frames)
    
    im = ax.imshow(np.zeros((grid_size, grid_size)), extent=[plot_range[0], plot_range[1], plot_range[0], plot_range[1]],
                  cmap='coolwarm', origin='lower', vmin=-3*A, vmax=3*A, animated=True)
    
    cbar = fig.colorbar(im, ax=ax)
    cbar.set_label('Displacement')
    
    for i, source in enumerate(sources):
        ax.plot(source[0], source[1], 'ko', markersize=5)
        ax.text(source[0]+0.1, source[1]+0.1, f'S{i+1}', fontsize=10)
    
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)
    ax.set_title(title, fontsize=14)
    
    def update(frame):
        t = times[frame]
        Z = np.zeros_like(X)
        for i in range(grid_size):
            for j in range(grid_size):
                Z[i, j] = calculate_total_displacement(X[i, j], Y[i, j], t, sources)
        im.set_array(Z)
        return [im]
    
    anim = FuncAnimation(fig, update, frames=n_frames, interval=1000/fps, blit=True)
    
    if save_path:
        anim.save(save_path, writer='pillow', fps=fps)
    
    return anim

def analyze_polygon_interference(n_vertices_list=[3, 4, 5, 6], radius=3.0, plot_range=(-5, 5)):
    for n_vertices in n_vertices_list:
        sources = generate_polygon_vertices(n_vertices, radius=radius)
        
        if n_vertices == 3:
            polygon_name = "Triangle"
        elif n_vertices == 4:
            polygon_name = "Square"
        elif n_vertices == 5:
            polygon_name = "Pentagon"
        elif n_vertices == 6:
            polygon_name = "Hexagon"
        else:
            polygon_name = f"{n_vertices}-gon"
        
        plot_interference_pattern(
            sources,
            f"Interference Pattern for {polygon_name}",
            save_path=os.path.join(image_dir, f"{polygon_name.lower()}_interference_2d.png"),
            grid_size=200
        )
        
        plot_3d_interference_pattern(
            sources,
            f"3D Interference Pattern for {polygon_name}",
            save_path=os.path.join(image_dir, f"{polygon_name.lower()}_interference_3d.png"),
            grid_size=100
        )
        
        create_interference_animation(
            sources,
            f"Interference Animation for {polygon_name}",
            save_path=os.path.join(image_dir, f"{polygon_name.lower()}_interference_animation.gif"),
            grid_size=100
        )

if __name__ == "__main__":
    analyze_polygon_interference()
    
    print("All simulations and visualizations completed.")
    print(f"Images saved to {image_dir}")
