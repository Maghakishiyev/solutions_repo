import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
repo_root = os.path.dirname(script_dir)
image_dir = os.path.join(repo_root, 'docs', '1 Physics', '5 Circuits', 'pics')
os.makedirs(image_dir, exist_ok=True)

def draw_circuit_graph(G, pos=None, title="Circuit Graph", save_path=None):
    """Draw a circuit graph with resistor values as edge labels."""
    plt.figure(figsize=(12, 8))
    
    if pos is None:
        pos = nx.spring_layout(G, seed=42)  
    
    # Draw nodes and edges
    nx.draw(G, pos, with_labels=True, node_color='lightblue', 
           node_size=800, font_size=14, font_weight='bold',
           edge_color='gray', width=2)
    
    # Create edge labels
    if isinstance(G, nx.MultiGraph):
        # For MultiGraph, handle multiple edges between same nodes
        edge_labels = {}
        for u, v, key, data in G.edges(keys=True, data=True):
            if (u, v) not in edge_labels:
                edge_labels[(u, v)] = f"{data['resistance']:.1f}Ω"
            else:
                edge_labels[(u, v)] += f", {data['resistance']:.1f}Ω"
    else:
        # For regular Graph
        edge_labels = {(u, v): f"{d['resistance']:.1f}Ω" for u, v, d in G.edges(data=True)}
    
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10, bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.8))
    
    plt.title(title, fontsize=16, fontweight='bold')
    plt.axis('off')
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Saved: {save_path}")
    
    plt.close()

def identify_series_nodes(G):
    series_nodes = [node for node in G.nodes() if G.degree(node) == 2]
    return series_nodes

def reduce_series(G, node):
    neighbors = list(G.neighbors(node))
    if len(neighbors) != 2:
        raise ValueError(f"Node {node} does not have exactly two connections")
    
    n1, n2 = neighbors
    
    r1 = G[n1][node]['resistance']
    r2 = G[node][n2]['resistance']
    
    r_eq = r1 + r2
    
    G.remove_node(node)
    
    G.add_edge(n1, n2, resistance=r_eq)
    
    return G

def identify_parallel_edges(G):
    """
    Identify pairs of nodes that have multiple edges between them (parallel resistors).
    For regular graphs, this means checking if there are duplicate edges.
    """
    parallel_pairs = []
    
    # For MultiGraph, check for multiple edges between same nodes
    if isinstance(G, nx.MultiGraph):
        for u, v in G.edges():
            if G.number_of_edges(u, v) > 1:
                if (u, v) not in parallel_pairs and (v, u) not in parallel_pairs:
                    parallel_pairs.append((u, v))
    else:
        # For regular Graph, we need to look for artificially created parallel paths
        # This is less common but can happen in certain circuit representations
        pass
    
    return parallel_pairs

def reduce_parallel(G, node_pair):
    """
    Reduce parallel connections between a pair of nodes.
    """
    u, v = node_pair
    
    # Get all resistances between the nodes
    if isinstance(G, nx.MultiGraph):
        # For MultiGraph, get all edges between u and v
        edges = [data['resistance'] for key, data in G[u][v].items()]
    else:
        # For regular Graph, there should only be one edge, but check anyway
        edges = []
        for n1, n2, data in G.edges(data=True):
            if (n1 == u and n2 == v) or (n1 == v and n2 == u):
                edges.append(data['resistance'])
    
    if len(edges) <= 1:
        return G  # No parallel edges to reduce
    
    # Calculate the equivalent resistance (1/R_eq = 1/R1 + 1/R2 + ...)
    r_eq = 1.0 / sum(1.0 / r for r in edges)
    
    # Remove all edges between the nodes
    if isinstance(G, nx.MultiGraph):
        G.remove_edges_from([(u, v, key) for key in G[u][v].keys()])
    else:
        while G.has_edge(u, v):
            G.remove_edge(u, v)
    
    # Add a new edge with the equivalent resistance
    G.add_edge(u, v, resistance=r_eq)
    
    return G

def delta_to_wye_transformation(G, nodes):
    if len(nodes) != 3:
        raise ValueError("Delta to Wye transformation requires exactly three nodes")
    
    a, b, c = nodes
    
    if not (G.has_edge(a, b) and G.has_edge(b, c) and G.has_edge(c, a)):
        raise ValueError("The three nodes must form a complete triangle")
    
    r_ab = G[a][b]['resistance']
    r_bc = G[b][c]['resistance']
    r_ca = G[c][a]['resistance']
    
    denominator = r_ab + r_bc + r_ca
    r_a = (r_ab * r_ca) / denominator
    r_b = (r_ab * r_bc) / denominator
    r_c = (r_bc * r_ca) / denominator
    
    new_node = max(G.nodes()) + 1
    
    G.remove_edge(a, b)
    G.remove_edge(b, c)
    G.remove_edge(c, a)
    
    G.add_edge(a, new_node, resistance=r_a)
    G.add_edge(b, new_node, resistance=r_b)
    G.add_edge(c, new_node, resistance=r_c)
    
    return G

def find_delta_configurations(G):
    delta_configs = []
    
    for a in G.nodes():
        for b in G.neighbors(a):
            for c in G.neighbors(a):
                if b != c and G.has_edge(b, c):
                    triangle = tuple(sorted([a, b, c]))
                    if triangle not in delta_configs:
                        delta_configs.append(triangle)
    
    return delta_configs

def calculate_equivalent_resistance(G, source, target):
    # Handle both Graph and MultiGraph types properly
    if isinstance(G, nx.MultiGraph):
        H = nx.MultiGraph(G)
    else:
        H = nx.Graph(G)
    
    reduction_steps = []
    reduction_steps.append((H.copy(), "Initial Circuit"))
    
    iteration = 0
    max_iterations = 100  
    
    # Special case: if we already have only 2 nodes, check for parallel edges first
    if len(H.nodes()) == 2:
        parallel_pairs = identify_parallel_edges(H)
        if parallel_pairs:
            pair = parallel_pairs[0]
            H = reduce_parallel(H, pair)
            reduction_steps.append((H.copy(), f"Initial Parallel Reduction between Nodes {pair}"))
    
    while len(H.nodes()) > 2 and iteration < max_iterations:
        iteration += 1
        
        series_nodes = identify_series_nodes(H)
        
        series_nodes = [node for node in series_nodes if node != source and node != target]
        
        if series_nodes:
            node = series_nodes[0]
            H = reduce_series(H, node)
            reduction_steps.append((H.copy(), f"After Series Reduction at Node {node}"))
            continue
        
        parallel_pairs = identify_parallel_edges(H)
        if parallel_pairs:
            pair = parallel_pairs[0]
            H = reduce_parallel(H, pair)
            reduction_steps.append((H.copy(), f"After Parallel Reduction between Nodes {pair}"))
            continue
        
        delta_configs = find_delta_configurations(H)
        if delta_configs:
            delta_configs = [config for config in delta_configs 
                            if source not in config and target not in config]
            
            if delta_configs:
                config = delta_configs[0]
                try:
                    H = delta_to_wye_transformation(H, config)
                    reduction_steps.append((H.copy(), f"After Delta-Wye Transformation at Nodes {config}"))
                    continue
                except Exception as e:
                    print(f"Error in delta-wye transformation: {e}")
        
        break
    
    # Check if the reduction was successful
    if len(H.nodes()) == 2 and H.has_edge(source, target):
        if isinstance(H, nx.MultiGraph):
            # For MultiGraph, get the resistance from the first (and should be only) edge
            edge_data = list(H[source][target].values())[0]
            equivalent_resistance = edge_data['resistance']
        else:
            # For regular Graph
            equivalent_resistance = H[source][target]['resistance']
    else:
        raise ValueError("Could not reduce the circuit completely. Try using delta-wye transformations or other methods.")
    
    return equivalent_resistance, reduction_steps

def create_example_circuits():
    """Create example circuits for testing the algorithm."""
    examples = []
    
    # Example 1: Simple Series Circuit
    G1 = nx.Graph()
    G1.add_edge(0, 1, resistance=10.0)
    G1.add_edge(1, 2, resistance=20.0)
    G1.add_edge(2, 3, resistance=30.0)
    examples.append((G1, 0, 3, "Simple Series Circuit"))
    
    # Example 2: Simple Parallel Circuit (needs MultiGraph for multiple edges)
    G2 = nx.MultiGraph()
    G2.add_edge(0, 1, resistance=10.0)
    G2.add_edge(0, 1, resistance=20.0)  # Parallel resistor
    examples.append((G2, 0, 1, "Simple Parallel Circuit"))
    
    # Example 3: Mixed Series-Parallel Circuit
    G3 = nx.Graph()
    G3.add_edge(0, 1, resistance=10.0)
    G3.add_edge(1, 2, resistance=20.0)
    G3.add_edge(1, 3, resistance=30.0)
    G3.add_edge(2, 4, resistance=40.0)
    G3.add_edge(3, 4, resistance=50.0)
    G3.add_edge(4, 5, resistance=60.0)
    examples.append((G3, 0, 5, "Mixed Series-Parallel Circuit"))
    
    # Example 4: Wheatstone Bridge Circuit
    G4 = nx.Graph()
    G4.add_edge(0, 1, resistance=10.0)  # Left arm
    G4.add_edge(0, 2, resistance=20.0)  # Right arm
    G4.add_edge(1, 3, resistance=30.0)  # Left bottom
    G4.add_edge(2, 3, resistance=40.0)  # Right bottom
    G4.add_edge(1, 2, resistance=50.0)  # Bridge resistor
    examples.append((G4, 0, 3, "Wheatstone Bridge Circuit"))
    
    return examples

def create_theory_diagrams():
    """Create theoretical diagrams for series, parallel, and delta-wye transformations."""
    
    # Series Reduction Diagram
    G_series = nx.Graph()
    G_series.add_edge('A', 'B', resistance=10.0)
    G_series.add_edge('B', 'C', resistance=20.0)
    G_series.add_edge('C', 'D', resistance=30.0)
    
    pos_series = {'A': (0, 0), 'B': (1, 0), 'C': (2, 0), 'D': (3, 0)}
    draw_circuit_graph(G_series, pos_series, 
                      title="Series Reduction Example: R₁ + R₂ + R₃ = 60Ω",
                      save_path=os.path.join(image_dir, 'series_reduction.png'))
    
    # Parallel Reduction Diagram
    G_parallel = nx.MultiGraph()
    G_parallel.add_edge('A', 'B', resistance=30.0)
    G_parallel.add_edge('A', 'B', resistance=60.0)
    
    pos_parallel = {'A': (0, 0), 'B': (2, 0)}
    draw_circuit_graph(G_parallel, pos_parallel,
                      title="Parallel Reduction Example: (30×60)/(30+60) = 20Ω", 
                      save_path=os.path.join(image_dir, 'parallel_reduction.png'))
    
    # Delta-Wye Transformation Diagram
    G_delta = nx.Graph()
    G_delta.add_edge('A', 'B', resistance=10.0)
    G_delta.add_edge('B', 'C', resistance=20.0)
    G_delta.add_edge('C', 'A', resistance=30.0)
    
    pos_delta = {'A': (0, 1), 'B': (1, 0), 'C': (1, 2)}
    draw_circuit_graph(G_delta, pos_delta,
                      title="Delta Configuration: R₁₂=10Ω, R₂₃=20Ω, R₃₁=30Ω",
                      save_path=os.path.join(image_dir, 'delta_wye_transformation.png'))

def analyze_example_circuits():
    """Analyze all example circuits and generate visualizations."""
    
    print("Creating theoretical diagrams...")
    create_theory_diagrams()
    
    examples = create_example_circuits()
    results = []
    
    for i, (G, source, target, description) in enumerate(examples):
        print(f"\nAnalyzing {description}...")
        
        # Create a good layout for the specific circuit type
        if "Series" in description:
            pos = {j: (j, 0) for j in range(len(G.nodes()))}
        elif "Parallel" in description:
            pos = {0: (0, 0), 1: (2, 0)}
        elif "Wheatstone" in description:
            pos = {0: (0, 1), 1: (1, 2), 2: (1, 0), 3: (2, 1)}
        else:
            pos = nx.spring_layout(G, seed=42)
        
        # Draw initial circuit
        draw_circuit_graph(G, pos, 
                          title=f"Example {i+1}: {description}",
                          save_path=os.path.join(image_dir, f"example_{i+1}_circuit.png"))
        
        try:
            equivalent_resistance, reduction_steps = calculate_equivalent_resistance(G, source, target)
            
            print(f"  Source: Node {source}, Target: Node {target}")
            print(f"  Equivalent resistance: {equivalent_resistance:.3f}Ω")
            print(f"  Reduction steps: {len(reduction_steps) - 1}")
            
            # Visualize reduction steps
            for j, (H, step_description) in enumerate(reduction_steps[1:], 1):  # Skip initial state
                # Try to maintain similar layout
                step_pos = {node: pos.get(node, (0, 0)) for node in H.nodes() if node in pos}
                if not step_pos:
                    step_pos = nx.spring_layout(H, seed=42)
                
                draw_circuit_graph(H, step_pos, 
                                  title=f"Step {j}: {step_description}",
                                  save_path=os.path.join(image_dir, f"example_{i+1}_step_{j}.png"))
            
            results.append({
                "example": i+1,
                "description": description,
                "source": source,
                "target": target,
                "equivalent_resistance": equivalent_resistance,
                "num_steps": len(reduction_steps) - 1  
            })
            
        except Exception as e:
            print(f"  Error: {e}")
            # Still add to results for completeness
            results.append({
                "example": i+1,
                "description": description,
                "source": source,
                "target": target,
                "equivalent_resistance": "Error",
                "num_steps": 0
            })
    
    return results

def create_graph_representation_diagram():
    """Create a diagram showing how circuits are represented as graphs."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    # Circuit diagram representation (conceptual)
    ax1.text(0.5, 0.9, 'Circuit Representation', ha='center', va='top', fontsize=16, fontweight='bold')
    ax1.text(0.5, 0.8, 'Nodes = Junctions', ha='center', va='center', fontsize=12)
    ax1.text(0.5, 0.7, 'Edges = Resistors', ha='center', va='center', fontsize=12)
    ax1.text(0.5, 0.6, 'Edge Weights = Resistance Values', ha='center', va='center', fontsize=12)
    
    # Example circuit as graph
    G_example = nx.Graph()
    G_example.add_edge('A', 'B', resistance=10.0)
    G_example.add_edge('B', 'C', resistance=20.0)
    
    ax1.set_xlim(-0.1, 1.1)
    ax1.set_ylim(0, 1)
    ax1.axis('off')
    
    # Graph representation
    ax2.text(0.5, 0.95, 'Graph Theory Representation', ha='center', va='top', fontsize=16, fontweight='bold', transform=ax2.transAxes)
    
    # Draw the graph on ax2
    pos_graph = {'A': (0.2, 0.5), 'B': (0.5, 0.5), 'C': (0.8, 0.5)}
    nx.draw(G_example, pos_graph, ax=ax2, with_labels=True, node_color='lightblue', 
           node_size=1000, font_size=12, font_weight='bold')
    
    edge_labels = {('A', 'B'): '10Ω', ('B', 'C'): '20Ω'}
    nx.draw_networkx_edge_labels(G_example, pos_graph, edge_labels, ax=ax2, font_size=10)
    
    ax2.set_title('Series Circuit: R_eq = 10Ω + 20Ω = 30Ω', fontsize=12)
    
    plt.tight_layout()
    plt.savefig(os.path.join(image_dir, 'graph_representation.png'), dpi=300, bbox_inches='tight')
    plt.close()
    print("Saved: graph_representation.png")

if __name__ == "__main__":
    print("="*60)
    print("EQUIVALENT RESISTANCE CALCULATION USING GRAPH THEORY")
    print("="*60)
    
    # Create graph representation diagram
    print("\nCreating graph representation diagram...")
    create_graph_representation_diagram()
    
    # Analyze all circuits
    results = analyze_example_circuits()
    
    print("\n" + "="*80)
    print("SUMMARY OF RESULTS")
    print("="*80)
    print(f"{'Ex':<3} {'Description':<35} {'Source':<6} {'Target':<6} {'R_eq (Ω)':<12} {'Steps':<6}")
    print("-" * 80)
    
    for result in results:
        if isinstance(result['equivalent_resistance'], str):
            r_eq_str = result['equivalent_resistance']
        else:
            r_eq_str = f"{result['equivalent_resistance']:.3f}"
        
        print(f"{result['example']:<3} {result['description']:<35} {result['source']:<6} {result['target']:<6} {r_eq_str:<12} {result['num_steps']:<6}")
    
    print("\n" + "="*60)
    print("ANALYSIS COMPLETED SUCCESSFULLY")
    print("="*60)
    print(f"All visualizations saved to: {image_dir}")
    
    # List generated files
    generated_files = [
        'graph_representation.png',
        'series_reduction.png', 
        'parallel_reduction.png',
        'delta_wye_transformation.png'
    ]
    
    for i in range(1, 5):  # Examples 1-4
        generated_files.append(f'example_{i}_circuit.png')
    
    print(f"\nGenerated {len(generated_files)} visualization files:")
    for filename in generated_files:
        filepath = os.path.join(image_dir, filename)
        if os.path.exists(filepath):
            print(f"  ✓ {filename}")
        else:
            print(f"  ✗ {filename} - NOT FOUND")
