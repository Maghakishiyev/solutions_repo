# Interference Patterns on a Water Surface

## Motivation

Interference occurs when waves from different sources overlap, creating new
patterns. On a water surface, this can be easily observed when ripples from
different points meet, forming distinctive interference patterns. These patterns
can show us how waves combine in different ways, either reinforcing each other
or canceling out.

Studying these patterns helps us understand wave behavior in a simple, visual
way. It also allows us to explore important concepts, like the relationship
between wave phase and the effects of multiple sources. This task offers a
hands-on approach to learning about wave interactions and their real-world
applications, making it an interesting and engaging way to dive into wave
physics.

## Theoretical Background

A circular wave on the water surface, emanating from a point source located at
$(x_0, y_0)$, can be described by the Single Disturbance equation:

$$\eta(x, y, t) = \frac{A}{\sqrt{r}} \cdot \cos(kr - \omega t + \phi)$$

where:

-   $\eta(x, y, t)$ is the displacement of the water surface at point $(x, y)$
    and time $t$,
-   $A$ is the amplitude of the wave,
-   $k = \frac{2\pi}{\lambda}$ is the wave number, related to the wavelength
    $\lambda$,
-   $\omega = 2\pi f$ is the angular frequency, related to the frequency $f$,
-   $r = \sqrt{(x - x_0)^2 + (y - y_0)^2}$ is the distance from the source to
    the point $(x, y)$,
-   $\phi$ is the initial phase.

### Principle of Superposition

When multiple waves overlap at a point, the resulting displacement is the sum of
the individual displacements. For $N$ sources, the total displacement is given
by:

$$\eta_{sum}(x, y, t) = \sum_{i=1}^{N} \eta_i(x, y, t)$$

where $N$ is the number of sources (vertices of the polygon).

### Constructive and Destructive Interference

-   **Constructive interference** occurs when waves combine to create a larger
    amplitude. This happens when the waves are in phase.
-   **Destructive interference** occurs when waves combine to create a smaller
    amplitude or cancel out completely. This happens when the waves are out of
    phase.

## Analysis of Interference Patterns for Regular Polygons

In this study, we analyze the interference patterns formed by waves emitted from
sources placed at the vertices of regular polygons. We consider four different
configurations: triangle, square, pentagon, and hexagon.

## Computational Model and Visualization

<details>
<summary>Click to expand Python code</summary>

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import os
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# Create directory for pics if it doesn't exist
image_dir = os.path.join('docs', '1 Physics', '3 Waves', 'pics')
os.makedirs(image_dir, exist_ok=True)

# Constants and parameters
A = 1.0  # Amplitude
lamb = 0.5  # Wavelength (lambda)
f = 1.0  # Frequency
k = 2 * np.pi / lamb  # Wave number
omega = 2 * np.pi * f  # Angular frequency
phi = 0  # Initial phase

# Function to calculate the displacement at a point due to a single source
def calculate_displacement(x, y, t, source_pos):
    """
    Calculate the displacement of the water surface at point (x, y) and time t
    due to a wave from a source at source_pos.

    Args:
        x, y: Coordinates of the point
        t: Time
        source_pos: Position of the source (x0, y0)

    Returns:
        Displacement at point (x, y) and time t
    """
    x0, y0 = source_pos
    r = np.sqrt((x - x0)**2 + (y - y0)**2)
    # Avoid division by zero at the source
    if r < 1e-10:
        return 0
    return A / np.sqrt(r) * np.cos(k * r - omega * t + phi)

# Function to calculate the total displacement due to multiple sources
def calculate_total_displacement(x, y, t, sources):
    """
    Calculate the total displacement at point (x, y) and time t due to all sources.

    Args:
        x, y: Coordinates of the point
        t: Time
        sources: List of source positions [(x1, y1), (x2, y2), ...]

    Returns:
        Total displacement at point (x, y) and time t
    """
    total = 0
    for source_pos in sources:
        total += calculate_displacement(x, y, t, source_pos)
    return total

# Function to generate the vertices of a regular polygon
def generate_polygon_vertices(n, radius=1.0, center=(0, 0)):
    """
    Generate the vertices of a regular polygon.

    Args:
        n: Number of sides (vertices)
        radius: Distance from center to vertices
        center: Center position (x, y)

    Returns:
        List of vertex positions [(x1, y1), (x2, y2), ...]
    """
    vertices = []
    for i in range(n):
        angle = 2 * np.pi * i / n
        x = center[0] + radius * np.cos(angle)
        y = center[1] + radius * np.sin(angle)
        vertices.append((x, y))
    return vertices

# Main function
if __name__ == "__main__":
    # Analyze interference patterns for different polygons
    analyze_polygon_interference()

    print("All simulations and visualizations completed.")
    print(f"pics saved to {image_dir}")
```

</details>

The computational model simulates the interference patterns formed by waves
emitted from sources placed at the vertices of regular polygons. It calculates
the displacement at each point on the water surface by summing the contributions
from all sources, following the principle of superposition. The model visualizes
the interference patterns using 2D color maps, 3D surface plots, and animations
to show the time evolution of the patterns.

By varying the number of vertices in the polygon, we can observe how the
complexity and symmetry of the interference pattern change. This provides
insights into how waves combine and interact in different geometric
configurations, demonstrating fundamental principles of wave physics.

### Triangle (3 Vertices)

For a triangle, three wave sources are placed at the vertices of an equilateral
triangle. The interference pattern shows:

-   A central region of constructive interference where waves from all three
    sources arrive approximately in phase.
-   Three primary axes of constructive interference extending outward from the
    center along the angle bisectors of the triangle.
-   Regions of destructive interference between these axes.

![Triangle Interference Pattern](./pics/triangle_interference_2d.png)

![Triangle 3D Interference Pattern](./pics/triangle_interference_3d.png)

### Square (4 Vertices)

For a square, four wave sources are placed at the vertices. The interference
pattern shows:

-   A central region of constructive interference.
-   Four primary axes of constructive interference along the diagonals of the
    square.
-   A more complex pattern of secondary maxima compared to the triangle case.
-   More pronounced regions of destructive interference due to the increased
    number of sources.

![Square Interference Pattern](./pics/square_interference_2d.png)

![Square 3D Interference Pattern](./pics/square_interference_3d.png)

### Pentagon (5 Vertices)

For a pentagon, five wave sources are placed at the vertices. The interference
pattern shows:

-   A central region of constructive interference.
-   Five primary axes of constructive interference.
-   A more complex and symmetric pattern compared to the triangle and square
    cases.
-   More regions of destructive interference creating a more intricate pattern.

![Pentagon Interference Pattern](./pics/pentagon_interference_2d.png)

![Pentagon 3D Interference Pattern](./pics/pentagon_interference_3d.png)

### Hexagon (6 Vertices)

For a hexagon, six wave sources are placed at the vertices. The interference
pattern shows:

-   A central region of constructive interference.
-   Six primary axes of constructive interference.
-   A highly symmetric pattern with six-fold rotational symmetry.
-   Multiple rings of constructive and destructive interference.

![Hexagon Interference Pattern](./pics/hexagon_interference_2d.png)

![Hexagon 3D Interference Pattern](./pics/hexagon_interference_3d.png)

## Observations and Conclusions

1. **Symmetry**: The interference pattern reflects the symmetry of the polygon.
   A regular polygon with $n$ sides produces an interference pattern with
   $n$-fold rotational symmetry.

2. **Central Constructive Interference**: All configurations show a region of
   constructive interference at the center of the polygon, where waves from all
   sources can arrive approximately in phase.

3. **Radial Pattern**: The interference patterns exhibit radial structures with
   alternating bands of constructive and destructive interference.

4. **Complexity with Increasing Vertices**: As the number of vertices increases,
   the interference pattern becomes more complex and intricate, with more
   regions of constructive and destructive interference.

5. **Distance Effect**: The amplitude of the waves decreases with distance from
   the sources (as $1/\sqrt{r}$), leading to less pronounced interference
   effects far from the sources.

## Applications

Understanding interference patterns has numerous applications:

1. **Acoustic Design**: Designing concert halls and auditoriums to optimize
   sound distribution.

2. **Antenna Arrays**: Designing antenna arrays to focus electromagnetic waves
   in specific directions.

3. **Optical Instruments**: Understanding and utilizing interference in
   microscopes, telescopes, and other optical instruments.

4. **Water Wave Energy Harvesting**: Optimizing the placement of wave energy
   converters to maximize energy extraction.

5. **Educational Demonstrations**: Providing visual demonstrations of wave
   principles for educational purposes.
