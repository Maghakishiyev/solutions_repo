# Recurrence

## Task 1

Compute first 5 elements of the following sequences:

### 1. $a_0 = 1$, $a_{n+1} = 2a_n + 1$ for $n \in \mathbb{N}\setminus\{0\}$

- $a_0 = 1$
- $a_1 = 2a_0 + 1 = 2(1) + 1 = 3$
- $a_2 = 2a_1 + 1 = 2(3) + 1 = 7$
- $a_3 = 2a_2 + 1 = 2(7) + 1 = 15$
- $a_4 = 2a_3 + 1 = 2(15) + 1 = 31$

**First 5 elements:** $1, 3, 7, 15, 31$

### 2. $b_0 = 2$, $b_{n+1} = b_n^2 - 1$ for $n \in \mathbb{N}\setminus\{0\}$

- $b_0 = 2$
- $b_1 = b_0^2 - 1 = 2^2 - 1 = 4 - 1 = 3$
- $b_2 = b_1^2 - 1 = 3^2 - 1 = 9 - 1 = 8$
- $b_3 = b_2^2 - 1 = 8^2 - 1 = 64 - 1 = 63$
- $b_4 = b_3^2 - 1 = 63^2 - 1 = 3969 - 1 = 3968$

**First 5 elements:** $2, 3, 8, 63, 3968$

### 3. $c_0 = 2, c_1 = 3$, $c_{n+2} = c_{n+1} \cdot c_n$ for $n \in \mathbb{N}\setminus\{0,1\}$

- $c_0 = 2$
- $c_1 = 3$
- $c_2 = c_1 \cdot c_0 = 3 \cdot 2 = 6$
- $c_3 = c_2 \cdot c_1 = 6 \cdot 3 = 18$
- $c_4 = c_3 \cdot c_2 = 18 \cdot 6 = 108$

**First 5 elements:** $2, 3, 6, 18, 108$

### 4. $d_0 = 1, d_1 = 2$, $d_{n+2} = d_{n+1}/d_n$ for $n \in \mathbb{N}\setminus\{0,1\}$

- $d_0 = 1$
- $d_1 = 2$
- $d_2 = d_1/d_0 = 2/1 = 2$
- $d_3 = d_2/d_1 = 2/2 = 1$
- $d_4 = d_3/d_2 = 1/2 = 0.5$

**First 5 elements:** $1, 2, 2, 1, 0.5$

### 5. $e_0 = 1, e_1 = 2$, $e_{n+2} = e_{n+1} - e_n$ for $n \in \mathbb{N}\setminus\{0,1\}$

- $e_0 = 1$
- $e_1 = 2$
- $e_2 = e_1 - e_0 = 2 - 1 = 1$
- $e_3 = e_2 - e_1 = 1 - 2 = -1$
- $e_4 = e_3 - e_2 = -1 - 1 = -2$

**First 5 elements:** $1, 2, 1, -1, -2$

## Task 2

Define following formulas and sequences using recurrence:

### 1. Factorial: $n! = 1 \cdot 2 \cdot 3 \cdot \ldots \cdot n$ for $n \geq 1$

**Recurrence definition:**
- $0! = 1$ (by convention)
- $n! = n \cdot (n-1)!$ for $n \geq 1$

### 2. Fibonacci numbers

**Recurrence definition:**
- $F_0 = 0$
- $F_1 = 1$
- $F_n = F_{n-1} + F_{n-2}$ for $n \geq 2$

The sequence: $0, 1, 1, 2, 3, 5, 8, 13, 21, 34, \ldots$

### 3. Napier's number (Euler's number $e$)

**Recurrence definition using series approximation:**
- $e_0 = 1$
- $e_n = e_{n-1} + \frac{1}{n!}$ for $n \geq 1$

This gives the partial sums: $e_n = \sum_{k=0}^{n} \frac{1}{k!}$

### 4. Sequence $(2, 2^2, (2^2)^2, ((2^2)^2)^2, \ldots)$

**Recurrence definition:**
- $a_0 = 2$
- $a_{n+1} = (a_n)^2$ for $n \geq 0$

This gives: $2, 4, 16, 256, 65536, \ldots$

### 5. Sequence $(2, 2^2, 2^{2^2}, 2^{2^{2^2}}, \ldots)$

**Recurrence definition:**
- $b_0 = 2$
- $b_{n+1} = 2^{b_n}$ for $n \geq 0$

This gives: $2, 4, 16, 65536, 2^{65536}, \ldots$

Note: This is the tetration sequence where each term is 2 raised to the power of the previous term.

