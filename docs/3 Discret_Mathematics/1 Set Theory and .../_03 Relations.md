# Relations

## Task 1

**Question:** For the following relations in the set $S = \{0, 1, 2, 3\}$, determine which properties (Reflexive (Z), Irreflexive (PZ), Symmetric (S), Antisymmetric (AS), Transitive (P)) are satisfied:

### Solution:

Let's first write out each relation as a set of ordered pairs, then analyze the properties:

#### 1. $R_1$: $(m, n) \in R_1$ if $m + n = 3$

**Ordered pairs:** $R_1 = \{(0,3), (1,2), (2,1), (3,0)\}$

**Properties:**
- **Reflexive (Z):** ❌ No element is related to itself (e.g., $(0,0) \notin R_1$)
- **Irreflexive (PZ):** ✅ No element is related to itself
- **Symmetric (S):** ✅ If $(m,n) \in R_1$, then $(n,m) \in R_1$
- **Antisymmetric (AS):** ❌ We have $(1,2)$ and $(2,1)$ in $R_1$ but $1 \neq 2$
- **Transitive (P):** ✅ No violations (there are no chains to check)

#### 2. $R_2$: $(m, n) \in R_2$ if $m - n$ is even

**Ordered pairs:** $R_2 = \{(0,0), (0,2), (1,1), (1,3), (2,0), (2,2), (3,1), (3,3)\}$

**Properties:**
- **Reflexive (Z):** ✅ All elements are related to themselves
- **Irreflexive (PZ):** ❌ Elements are related to themselves
- **Symmetric (S):** ✅ If $m-n$ is even, then $n-m$ is also even
- **Antisymmetric (AS):** ❌ We have $(0,2)$ and $(2,0)$ but $0 \neq 2$
- **Transitive (P):** ✅ If $m-n$ and $n-p$ are even, then $m-p$ is even

#### 3. $R_3$: $(m, n) \in R_3$ if $m \leq n$

**Ordered pairs:** $R_3 = \{(0,0), (0,1), (0,2), (0,3), (1,1), (1,2), (1,3), (2,2), (2,3), (3,3)\}$

**Properties:**
- **Reflexive (Z):** ✅ All elements satisfy $m \leq m$
- **Irreflexive (PZ):** ❌ Elements are related to themselves
- **Symmetric (S):** ❌ $(0,1) \in R_3$ but $(1,0) \notin R_3$
- **Antisymmetric (AS):** ✅ If $m \leq n$ and $n \leq m$, then $m = n$
- **Transitive (P):** ✅ If $m \leq n$ and $n \leq p$, then $m \leq p$

#### 4. $R_4$: $(m, n) \in R_4$ if $m + n \leq 4$

**Ordered pairs:** $R_4 = \{(0,0), (0,1), (0,2), (0,3), (0,4), (1,0), (1,1), (1,2), (1,3), (2,0), (2,1), (2,2), (3,0), (3,1), (4,0)\}$

Wait, we need to stay within $S = \{0,1,2,3\}$:
$R_4 = \{(0,0), (0,1), (0,2), (0,3), (1,0), (1,1), (1,2), (1,3), (2,0), (2,1), (2,2), (3,0), (3,1)\}$

**Properties:**
- **Reflexive (Z):** ❌ $(3,3) \notin R_4$ since $3+3 = 6 > 4$
- **Irreflexive (PZ):** ❌ $(0,0), (1,1), (2,2) \in R_4$
- **Symmetric (S):** ✅ If $m+n \leq 4$, then $n+m \leq 4$
- **Antisymmetric (AS):** ❌ We have $(0,1)$ and $(1,0)$ but $0 \neq 1$
- **Transitive (P):** ❌ $(3,1) \in R_4$ and $(1,2) \in R_4$ but $(3,2) \notin R_4$

#### 5. $R_5$: $(m, n) \in R_5$ if $\max\{m, n\} = 3$

**Ordered pairs:** $R_5 = \{(0,3), (1,3), (2,3), (3,0), (3,1), (3,2), (3,3)\}$

**Properties:**
- **Reflexive (Z):** ❌ $(0,0), (1,1), (2,2) \notin R_5$
- **Irreflexive (PZ):** ❌ $(3,3) \in R_5$
- **Symmetric (S):** ✅ If $\max\{m,n\} = 3$, then $\max\{n,m\} = 3$
- **Antisymmetric (AS):** ❌ We have $(0,3)$ and $(3,0)$ but $0 \neq 3$
- **Transitive (P):** ❌ $(0,3) \in R_5$ and $(3,1) \in R_5$ but $(0,1) \notin R_5$

### Summary:
- $R_1$: Irreflexive, Symmetric, Transitive
- $R_2$: Reflexive, Symmetric, Transitive
- $R_3$: Reflexive, Antisymmetric, Transitive
- $R_4$: Symmetric
- $R_5$: Symmetric

## Task 2

**Question:** Let $A = \{-1, 0, 1, 2\}$. Write each relation as a set of ordered pairs:

### Solution:

1. **$m \leq n$:**
   $R_1 = \{(-1,-1), (-1,0), (-1,1), (-1,2), (0,0), (0,1), (0,2), (1,1), (1,2), (2,2)\}$

2. **$mn = 0$:**
   $R_2 = \{(-1,0), (0,-1), (0,0), (0,1), (0,2), (1,0), (2,0)\}$

3. **$m = n$:**
   $R_3 = \{(-1,-1), (0,0), (1,1), (2,2)\}$

4. **$m^2 + n^2 = 2$:**
   Need pairs where $m^2 + n^2 = 2$:
   - $(-1)^2 + 1^2 = 1 + 1 = 2$ ✓
   - $1^2 + (-1)^2 = 1 + 1 = 2$ ✓
   
   $R_4 = \{(-1,1), (1,-1)\}$

5. **$m^2 - n^2 = 2$:**
   Need pairs where $m^2 - n^2 = 2$:
   - No valid pairs in $A$
   
   $R_5 = \emptyset$

6. **$m^2 = n^2$:**
   $R_6 = \{(-1,-1), (-1,1), (0,0), (1,-1), (1,1), (2,2)\}$

7. **$m^2 = n$:**
   Need pairs where $m^2 = n$:
   - $(-1)^2 = 1$ ✓
   - $0^2 = 0$ ✓
   - $1^2 = 1$ ✓
   - $2^2 = 4 \notin A$
   
   $R_7 = \{(-1,1), (0,0), (1,1)\}$

8. **$mn = 2$:**
   Need pairs where $mn = 2$:
   - $(-1) \cdot (-2) = 2$ but $-2 \notin A$
   - $1 \cdot 2 = 2$ ✓
   - $2 \cdot 1 = 2$ ✓
   
   $R_8 = \{(1,2), (2,1)\}$

9. **$\max\{m, n\} = 1$:**
   $R_9 = \{(-1,-1), (-1,0), (-1,1), (0,-1), (0,0), (0,1), (1,-1), (1,0), (1,1)\}$

## Task 3

**Question:** Which of the relations from Task 2 are reflexive, and which are symmetric?

### Solution:

**Reflexive relations** (contain all pairs $(a,a)$ for $a \in A$):
- $R_1$ (m ≤ n): ✅ Reflexive
- $R_2$ (mn = 0): ❌ Not reflexive (missing $(-1,-1), (1,1), (2,2)$)
- $R_3$ (m = n): ✅ Reflexive
- $R_4$ (m² + n² = 2): ❌ Not reflexive
- $R_5$ (m² - n² = 2): ❌ Not reflexive (empty set)
- $R_6$ (m² = n²): ❌ Not reflexive (missing $(0,0)$ - wait, $(0,0)$ is there, missing $(2,2)$ - wait, $(2,2)$ is there too. Let me recheck... Missing $(-1,-1)$? No, $(-1)^2 = 1^2$, so $(-1,-1)$ should be there. Actually this is reflexive! ✅)
- $R_7$ (m² = n): ❌ Not reflexive (missing $(-1,-1), (2,2)$)
- $R_8$ (mn = 2): ❌ Not reflexive
- $R_9$ (max{m,n} = 1): ❌ Not reflexive (missing $(2,2)$)

**Symmetric relations** (if $(a,b) \in R$ then $(b,a) \in R$):
- $R_1$ (m ≤ n): ❌ Not symmetric
- $R_2$ (mn = 0): ✅ Symmetric
- $R_3$ (m = n): ✅ Symmetric
- $R_4$ (m² + n² = 2): ✅ Symmetric
- $R_5$ (m² - n² = 2): ✅ Symmetric (vacuously true)
- $R_6$ (m² = n²): ✅ Symmetric
- $R_7$ (m² = n): ❌ Not symmetric
- $R_8$ (mn = 2): ✅ Symmetric
- $R_9$ (max{m,n} = 1): ✅ Symmetric

## Task 4

**Question:** In the set $\mathbb{N}$, write the following binary relations:

### Solution:

1. **$R_1$ defined by $m + n = 5$:**
   $R_1 = \{(0,5), (1,4), (2,3), (3,2), (4,1), (5,0)\}$

2. **$R_2$ defined by $\max\{m, n\} = 2$:**
   $R_2 = \{(0,2), (1,2), (2,0), (2,1), (2,2)\}$

3. **$R_3$ defined by $m^3 - n^3 \equiv 0 \pmod{5}$:**
   
   This means $m^3 \equiv n^3 \pmod{5}$. Let's find the pattern of cubes modulo 5:
   - $0^3 \equiv 0 \pmod{5}$
   - $1^3 \equiv 1 \pmod{5}$
   - $2^3 \equiv 8 \equiv 3 \pmod{5}$
   - $3^3 \equiv 27 \equiv 2 \pmod{5}$
   - $4^3 \equiv 64 \equiv 4 \pmod{5}$
   - $5^3 \equiv 125 \equiv 0 \pmod{5}$

   The pattern repeats every 5 numbers: $\{0,1,3,2,4,0,1,3,2,4,...\}$

   **Yes, $R_3$ contains infinitely many ordered pairs.**
   
   **Examples:** $(0,0), (0,5), (0,10), (1,1), (1,6), (1,11), (2,2), (2,7), (3,3), (3,8), (4,4), (4,9), (5,0), (5,5), ...$

## Task 5

**Question:** For each relation from Task 4, determine which properties are satisfied:

### Solution:

#### $R_1$: $m + n = 5$
- **Symmetric:** ✅ If $m + n = 5$, then $n + m = 5$
- **Antisymmetric:** ❌ $(1,4)$ and $(4,1)$ are both in $R_1$ but $1 \neq 4$
- **Transitive:** ✅ (vacuously true - no valid chains exist)
- **Reflexive:** ❌ $(0,0) \notin R_1$ since $0 + 0 \neq 5$
- **Irreflexive:** ❌ $(2.5, 2.5)$ would be in $R_1$ if we allowed non-integers, but in $\mathbb{N}$, no element relates to itself, so it's irreflexive ✅

#### $R_2$: $\max\{m, n\} = 2$
- **Symmetric:** ✅ If $\max\{m,n\} = 2$, then $\max\{n,m\} = 2$
- **Antisymmetric:** ❌ $(0,2)$ and $(2,0)$ are both in $R_2$ but $0 \neq 2$
- **Transitive:** ❌ $(0,2) \in R_2$ and $(2,1) \in R_2$ but $(0,1) \notin R_2$
- **Reflexive:** ❌ $(0,0) \notin R_2$
- **Irreflexive:** ❌ $(2,2) \in R_2$

#### $R_3$: $m^3 - n^3 \equiv 0 \pmod{5}$
- **Symmetric:** ✅ If $m^3 \equiv n^3 \pmod{5}$, then $n^3 \equiv m^3 \pmod{5}$
- **Antisymmetric:** ❌ Many counterexamples like $(0,5)$ and $(5,0)$
- **Transitive:** ✅ If $m^3 \equiv n^3 \pmod{5}$ and $n^3 \equiv p^3 \pmod{5}$, then $m^3 \equiv p^3 \pmod{5}$
- **Reflexive:** ✅ $m^3 \equiv m^3 \pmod{5}$ for all $m$
- **Irreflexive:** ❌ All elements relate to themselves

## Task 6

**Question:** Provide an example of a relation that is:

### Solution:

1. **Antisymmetric and transitive but not reflexive:**
   
   **Example:** $R = \{(1,2), (2,3), (1,3)\}$ on set $\{1,2,3\}$
   
   - **Antisymmetric:** ✅ No pair $(a,b)$ and $(b,a)$ with $a \neq b$
   - **Transitive:** ✅ $(1,2) \in R$, $(2,3) \in R$, and $(1,3) \in R$
   - **Not reflexive:** ✅ $(1,1), (2,2), (3,3) \notin R$

2. **Symmetric but not reflexive or transitive:**
   
   **Example:** $R = \{(1,2), (2,1), (2,3), (3,2)\}$ on set $\{1,2,3\}$
   
   - **Symmetric:** ✅ If $(a,b) \in R$ then $(b,a) \in R$
   - **Not reflexive:** ✅ $(1,1), (2,2), (3,3) \notin R$
   - **Not transitive:** ✅ $(1,2) \in R$ and $(2,3) \in R$ but $(1,3) \notin R$

## Task 7

**Question:** Draw the graph of each relation from Task 1. Do not draw arrows if the relation is symmetric.

### Solution:

Since these are symmetric/antisymmetric relations, I'll describe the graph structure:

#### $R_1$: $\{(0,3), (1,2), (2,1), (3,0)\}$ (Symmetric)
```
0 ←→ 3
1 ←→ 2
```
Undirected edges since it's symmetric.

#### $R_2$: $\{(0,0), (0,2), (1,1), (1,3), (2,0), (2,2), (3,1), (3,3)\}$ (Symmetric)
```
0 ←→ 2    0 has self-loop
1 ←→ 3    1 has self-loop
          2 has self-loop
          3 has self-loop
```

#### $R_3$: $\{(0,0), (0,1), (0,2), (0,3), (1,1), (1,2), (1,3), (2,2), (2,3), (3,3)\}$ (Antisymmetric)
```
0 → 1 → 2 → 3
↓   ↓   ↓   ↓
0   1   2   3
```
Each element has arrows to all elements ≥ itself.

#### $R_4$: Symmetric - undirected graph with edges between all pairs whose sum ≤ 4

#### $R_5$: Symmetric - undirected graph where element 3 connects to all elements (including itself)

## Task 8

**Question:** Draw the graph of each relation from Task 2. Do not draw arrows if the relation is symmetric.

### Solution:

I'll describe the key graph structures for the symmetric relations:

#### $R_1$ (m ≤ n): Not symmetric - directed acyclic graph
#### $R_2$ (mn = 0): Symmetric - undirected graph with 0 connected to all elements
#### $R_3$ (m = n): Symmetric - only self-loops at each vertex
#### $R_4$ (m² + n² = 2): Symmetric - undirected edge between -1 and 1
#### $R_5$ (m² - n² = 2): Symmetric - empty graph
#### $R_6$ (m² = n²): Symmetric - undirected edges between -1↔1, self-loops at 0 and 2
#### $R_7$ (m² = n): Not symmetric - directed arrows
#### $R_8$ (mn = 2): Symmetric - undirected edge between 1↔2
#### $R_9$ (max{m,n} = 1): Symmetric - undirected complete subgraph on {-1,0,1}