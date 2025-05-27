# Graph Theory

## Task 1 - Graph Representation

For each graph listed below, complete the other two methods of graph representation.

### Graph 1 (Undirected)
**Given Edge List:** [(1, 3), (1, 4), (1, 5), (2, 6), (3, 6), (4, 5)]

**Vertex Set:** {1, 2, 3, 4, 5, 6}

**Adjacency Matrix:**
```
    1  2  3  4  5  6
1 [ 0  0  1  1  1  0 ]
2 [ 0  0  0  0  0  1 ]
3 [ 1  0  0  0  0  1 ]
4 [ 1  0  0  0  1  0 ]
5 [ 1  0  0  1  0  0 ]
6 [ 0  1  1  0  0  0 ]
```

**Adjacency List:**
```
{1: [3, 4, 5],
 2: [6],
 3: [1, 6],
 4: [1, 5],
 5: [1, 4],
 6: [2, 3]}
```

### Graph 2 (Undirected)
**Given Adjacency Matrix:**
```
[[0 0 1 0 0 0]
 [0 0 0 0 0 0]
 [1 0 0 0 1 1]
 [0 0 0 0 1 0]
 [0 0 1 1 0 1]
 [0 0 1 0 1 0]]
```

**Vertex Set:** {1, 2, 3, 4, 5, 6} (vertices indexed 1-6)

**Edge List:** [(1, 3), (3, 5), (3, 6), (4, 5), (5, 6)]

**Adjacency List:**
```
{1: [3],
 2: [],
 3: [1, 5, 6],
 4: [5],
 5: [3, 4, 6],
 6: [3, 5]}
```

### Graph 3 (Undirected)
**Given Adjacency List:**
```
{1: [4],
 2: [4],
 3: [5, 6],
 4: [1, 2, 6],
 5: [3],
 6: [3, 4]}
```

**Vertex Set:** {1, 2, 3, 4, 5, 6}

**Edge List:** [(1, 4), (2, 4), (3, 5), (3, 6), (4, 6)]

**Adjacency Matrix:**
```
    1  2  3  4  5  6
1 [ 0  0  0  1  0  0 ]
2 [ 0  0  0  1  0  0 ]
3 [ 0  0  0  0  1  1 ]
4 [ 1  1  0  0  0  1 ]
5 [ 0  0  1  0  0  0 ]
6 [ 0  0  1  1  0  0 ]
```

### Graph 4 (Directed)
**Given Edge List:** [(1, 2), (2, 5), (3, 4), (4, 1), (5, 2), (5, 3), (6, 3), (6, 5)]

**Vertex Set:** {1, 2, 3, 4, 5, 6}

**Adjacency Matrix:**
```
    1  2  3  4  5  6
1 [ 0  1  0  0  0  0 ]
2 [ 0  0  0  0  1  0 ]
3 [ 0  0  0  1  0  0 ]
4 [ 1  0  0  0  0  0 ]
5 [ 0  1  1  0  0  0 ]
6 [ 0  0  1  0  1  0 ]
```

**Adjacency List:**
```
{1: [2],
 2: [5],
 3: [4],
 4: [1],
 5: [2, 3],
 6: [3, 5]}
```

### Graph 5 (Directed)
**Given Adjacency Matrix:**
```
[[0 1 0 1 0 1]
 [0 0 0 0 0 0]
 [0 1 0 0 1 0]
 [1 0 0 0 1 0]
 [1 0 0 1 0 1]
 [0 1 0 1 1 0]]
```

**Vertex Set:** {1, 2, 3, 4, 5, 6}

**Edge List:** [(1, 2), (1, 4), (1, 6), (3, 2), (3, 5), (4, 1), (4, 5), (5, 1), (5, 4), (5, 6), (6, 2), (6, 4), (6, 5)]

**Adjacency List:**
```
{1: [2, 4, 6],
 2: [],
 3: [2, 5],
 4: [1, 5],
 5: [1, 4, 6],
 6: [2, 4, 5]}
```

### Graph 6 (Directed)
**Given Adjacency List:**
```
{1: [2, 6],
 2: [1, 4],
 3: [4, 5],
 4: [1, 6],
 5: [2, 3],
 6: [1, 3, 5]}
```

**Vertex Set:** {1, 2, 3, 4, 5, 6}

**Edge List:** [(1, 2), (1, 6), (2, 1), (2, 4), (3, 4), (3, 5), (4, 1), (4, 6), (5, 2), (5, 3), (6, 1), (6, 3), (6, 5)]

**Adjacency Matrix:**
```
    1  2  3  4  5  6
1 [ 0  1  0  0  0  1 ]
2 [ 1  0  0  1  0  0 ]
3 [ 0  0  0  1  1  0 ]
4 [ 1  0  0  0  0  1 ]
5 [ 0  1  1  0  0  0 ]
6 [ 1  0  1  0  1  0 ]
```

## Task 2

For the following undirected graph:
```
1: [3],
2: [1, 4],
3: [1, 4, 5],
4: [6, 7],
5: [6, 2],
6: [4, 5],
7: [8],
8: [7]
```

**Note:** There's an inconsistency in the given adjacency list. Correcting it to be symmetric for undirected graph:
```
1: [3, 2],
2: [1, 4, 5],
3: [1, 4, 5],
4: [2, 3, 6, 7],
5: [3, 2, 6],
6: [4, 5],
7: [4, 8],
8: [7]
```

### Answers:

1. **How many vertices and edges are there in the graph?**
   - **Vertices:** 8
   - **Edges:** 9 (counting each edge once: (1,2), (1,3), (2,4), (2,5), (3,4), (3,5), (4,6), (4,7), (5,6), (6,5) = duplicate, (7,8))
   - **Corrected count:** 8 edges

2. **Is the graph connected? Justify your answer.**
   - **Yes**, the graph is connected. All vertices can be reached from any other vertex through a path.

3. **What is the diameter of the graph?**
   - The diameter is **4** (longest shortest path, e.g., from vertex 8 to vertex 1: 8→7→4→2→1)

4. **What is the radius of the graph?**
   - The radius is **2** (minimum eccentricity among all vertices)

5. **Which vertex (or vertices) is in the center of the graph?**
   - Vertices **2, 3, 4** are in the center (vertices with eccentricity equal to radius)

6. **Is the graph Eulerian? Why or why not?**
   - **No**, the graph is not Eulerian because vertices 1 and 8 have odd degree (degree 1), while Eulerian graphs require all vertices to have even degree.

7. **Find the degree of vertex 4.**
   - **Degree of vertex 4:** 4 (connected to vertices 2, 3, 6, 7)

8. **Find the shortest path from vertex 5 to vertex 8 using Dijkstra's algorithm.**
   - **Shortest path:** 5 → 2 → 4 → 7 → 8

9. **What is the length of the shortest path from vertex 5 to vertex 8?**
   - **Length:** 4

10. **Does the graph contain a cycle? If yes, what is the length of one cycle?**
    - **Yes**, the graph contains cycles. One example: 2 → 4 → 3 → 5 → 2, which has **length 4**.

## Task 3

Consider the above graph as a directed graph. In this case, the adjacency list represents directed edges:

```
1: [3],
2: [1, 4],
3: [1, 4, 5],
4: [6, 7],
5: [6, 2],
6: [4, 5],
7: [8],
8: [7]
```

For a directed graph interpretation:
- The graph may not be strongly connected
- Some vertices may not be reachable from others
- The analysis would need to consider directed paths only
- Eulerian properties would require all vertices to have equal in-degree and out-degree

