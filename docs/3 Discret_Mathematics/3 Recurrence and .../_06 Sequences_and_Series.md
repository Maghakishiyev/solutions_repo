# Sequences and Series

## Task 1

Calculate:

### 1. $\frac{7!}{5!}$

$\frac{7!}{5!} = \frac{7 \cdot 6 \cdot 5!}{5!} = 7 \cdot 6 = 42$

### 2. $\frac{10!}{6!4!}$

$\frac{10!}{6!4!} = \frac{10 \cdot 9 \cdot 8 \cdot 7 \cdot 6!}{6! \cdot 4!} = \frac{10 \cdot 9 \cdot 8 \cdot 7}{4!} = \frac{5040}{24} = 210$

### 3. $\frac{9!}{0!}$

Since $0! = 1$:
$\frac{9!}{0!} = \frac{362880}{1} = 362880$

### 4. $\sum_{k=0}^{5} k!$

$\sum_{k=0}^{5} k! = 0! + 1! + 2! + 3! + 4! + 5! = 1 + 1 + 2 + 6 + 24 + 120 = 154$

### 5. $\prod_{j=3}^{5} j$

$\prod_{j=3}^{5} j = 3 \cdot 4 \cdot 5 = 60$

## Task 2

Simplify the fractions:

### 1. $\frac{n!}{(n-1)!}$

$\frac{n!}{(n-1)!} = \frac{n \cdot (n-1)!}{(n-1)!} = n$

### 2. $\frac{(n!)^2}{(n+1)!(n-1)!}$

$\frac{(n!)^2}{(n+1)!(n-1)!} = \frac{(n!)^2}{(n+1) \cdot n! \cdot (n-1)!} = \frac{(n!)^2}{(n+1) \cdot n \cdot (n-1)! \cdot (n-1)!} = \frac{n! \cdot n!}{(n+1) \cdot n \cdot (n-1)!^2}$

Since $n! = n \cdot (n-1)!$:
$\frac{(n!)^2}{(n+1)!(n-1)!} = \frac{n \cdot (n-1)! \cdot n!}{(n+1) \cdot n!} = \frac{n \cdot (n-1)!}{n+1} = \frac{n!}{n+1}$

## Task 3

Calculate:

### 1. $\sum_{k=1}^{n} 3^k$ for $n = 1, 2, 3, 4$

Using the geometric series formula: $\sum_{k=1}^{n} 3^k = 3 \cdot \frac{3^n - 1}{3 - 1} = \frac{3(3^n - 1)}{2}$

- For $n = 1$: $\sum_{k=1}^{1} 3^k = 3^1 = 3$
- For $n = 2$: $\sum_{k=1}^{2} 3^k = 3^1 + 3^2 = 3 + 9 = 12$
- For $n = 3$: $\sum_{k=1}^{3} 3^k = 3^1 + 3^2 + 3^3 = 3 + 9 + 27 = 39$
- For $n = 4$: $\sum_{k=1}^{4} 3^k = 3^1 + 3^2 + 3^3 + 3^4 = 3 + 9 + 27 + 81 = 120$

### 2. $\sum_{k=n}^{10} k^3$ for $n = 3, 4, 5$

Using the formula $\sum_{k=1}^{m} k^3 = \left(\frac{m(m+1)}{2}\right)^2$:

- For $n = 3$: $\sum_{k=3}^{10} k^3 = \sum_{k=1}^{10} k^3 - \sum_{k=1}^{2} k^3 = 3025 - (1 + 8) = 3025 - 9 = 3016$
- For $n = 4$: $\sum_{k=4}^{10} k^3 = \sum_{k=1}^{10} k^3 - \sum_{k=1}^{3} k^3 = 3025 - (1 + 8 + 27) = 3025 - 36 = 2989$
- For $n = 5$: $\sum_{k=5}^{10} k^3 = \sum_{k=1}^{10} k^3 - \sum_{k=1}^{4} k^3 = 3025 - (1 + 8 + 27 + 64) = 3025 - 100 = 2925$

### 3. $\sum_{j=1}^{n} j$ for $n = 1, 2, 5$

Using the formula $\sum_{j=1}^{n} j = \frac{n(n+1)}{2}$:

- For $n = 1$: $\sum_{j=1}^{1} j = 1$
- For $n = 2$: $\sum_{j=1}^{2} j = 1 + 2 = 3$
- For $n = 5$: $\sum_{j=1}^{5} j = 1 + 2 + 3 + 4 + 5 = 15$

## Task 4

Calculate:

### 1. $\sum_{i=0}^{\infty} (-1)^i$

This series alternates: $1 - 1 + 1 - 1 + 1 - 1 + \ldots$

The series does not converge. The partial sums oscillate between 1 and 0.

### 2. $\prod_{n=1}^{\infty} (2n + 1)$

$\prod_{n=1}^{\infty} (2n + 1) = 3 \cdot 5 \cdot 7 \cdot 9 \cdot 11 \cdot \ldots$

This infinite product diverges to infinity.

### 3. $\sum_{k=3}^{8} (k^2 + 1)$

$\sum_{k=3}^{8} (k^2 + 1) = \sum_{k=3}^{8} k^2 + \sum_{k=3}^{8} 1$

$= (9 + 16 + 25 + 36 + 49 + 64) + 6 = 199 + 6 = 205$

### 4. $\left(\sum_{k=3}^{8} k^2\right) + 1$

$\left(\sum_{k=3}^{8} k^2\right) + 1 = (9 + 16 + 25 + 36 + 49 + 64) + 1 = 199 + 1 = 200$

## Task 5

Calculate:

### 1. $\prod_{n=1}^{m} (n - 3)$ for $m = 1, 2, 3, 4, 73$

- For $m = 1$: $\prod_{n=1}^{1} (n - 3) = (1 - 3) = -2$
- For $m = 2$: $\prod_{n=1}^{2} (n - 3) = (1 - 3)(2 - 3) = (-2)(-1) = 2$
- For $m = 3$: $\prod_{n=1}^{3} (n - 3) = (1 - 3)(2 - 3)(3 - 3) = (-2)(-1)(0) = 0$
- For $m = 4$: $\prod_{n=1}^{4} (n - 3) = (1 - 3)(2 - 3)(3 - 3)(4 - 3) = (-2)(-1)(0)(1) = 0$
- For $m = 73$: $\prod_{n=1}^{73} (n - 3) = 0$ (since one factor is 0 when $n = 3$)

### 2. $\prod_{m=1}^{k} \frac{k+1}{k}$ for $k = 1, 2, 3$

Note: The problem statement seems to have a variable confusion. Assuming it means $\prod_{m=1}^{k} \frac{m+1}{m}$:

- For $k = 1$: $\prod_{m=1}^{1} \frac{m+1}{m} = \frac{2}{1} = 2$
- For $k = 2$: $\prod_{m=1}^{2} \frac{m+1}{m} = \frac{2}{1} \cdot \frac{3}{2} = 3$
- For $k = 3$: $\prod_{m=1}^{3} \frac{m+1}{m} = \frac{2}{1} \cdot \frac{3}{2} \cdot \frac{4}{3} = 4$

**General formula:** $\prod_{m=1}^{k} \frac{m+1}{m} = k+1$ (telescoping product)

## Task 6

Calculate and find the general formula for:

### 1. $\sum_{k=0}^{n} k^2$ for $n = 1, 2, 3, 4, 5$

Note: The problem states $\sum_{k=0}^{2} k^2$ but asks for different values of $n$. Assuming it means $\sum_{k=0}^{n} k^2$.

Using the formula $\sum_{k=0}^{n} k^2 = \frac{n(n+1)(2n+1)}{6}$:

- For $n = 1$: $\sum_{k=0}^{1} k^2 = 0^2 + 1^2 = 1$
- For $n = 2$: $\sum_{k=0}^{2} k^2 = 0^2 + 1^2 + 2^2 = 5$
- For $n = 3$: $\sum_{k=0}^{3} k^2 = 0^2 + 1^2 + 2^2 + 3^2 = 14$
- For $n = 4$: $\sum_{k=0}^{4} k^2 = 0^2 + 1^2 + 2^2 + 3^2 + 4^2 = 30$
- For $n = 5$: $\sum_{k=0}^{5} k^2 = 0^2 + 1^2 + 2^2 + 3^2 + 4^2 + 5^2 = 55$

**General formula:** $\sum_{k=0}^{n} k^2 = \frac{n(n+1)(2n+1)}{6}$

## Task 7

Consider the sequence defined by $a_n = \frac{n-1}{n+1}$ for $n \in \mathbb{N}_{+}$.

### 1. Write the first six terms of this sequence

- $a_1 = \frac{1-1}{1+1} = \frac{0}{2} = 0$
- $a_2 = \frac{2-1}{2+1} = \frac{1}{3}$
- $a_3 = \frac{3-1}{3+1} = \frac{2}{4} = \frac{1}{2}$
- $a_4 = \frac{4-1}{4+1} = \frac{3}{5}$
- $a_5 = \frac{5-1}{5+1} = \frac{4}{6} = \frac{2}{3}$
- $a_6 = \frac{6-1}{6+1} = \frac{5}{7}$

**First six terms:** $0, \frac{1}{3}, \frac{1}{2}, \frac{3}{5}, \frac{2}{3}, \frac{5}{7}$

### 2. Calculate $a_{n+1} - a_n$ for $n = 1, 2, 3$

$a_{n+1} - a_n = \frac{(n+1)-1}{(n+1)+1} - \frac{n-1}{n+1} = \frac{n}{n+2} - \frac{n-1}{n+1}$

$= \frac{n(n+1) - (n-1)(n+2)}{(n+2)(n+1)} = \frac{n^2 + n - (n^2 + 2n - n - 2)}{(n+2)(n+1)} = \frac{n^2 + n - n^2 - n + 2}{(n+2)(n+1)} = \frac{2}{(n+1)(n+2)}$

- For $n = 1$: $a_2 - a_1 = \frac{2}{2 \cdot 3} = \frac{1}{3}$
- For $n = 2$: $a_3 - a_2 = \frac{2}{3 \cdot 4} = \frac{1}{6}$
- For $n = 3$: $a_4 - a_3 = \frac{2}{4 \cdot 5} = \frac{1}{10}$

### 3. Prove that $a_{n+1} + a_n = \frac{n(n+1)}{(n+1)(n+2)}$ for $n \in \mathbb{N}_{+}$

$a_{n+1} + a_n = \frac{n}{n+2} + \frac{n-1}{n+1}$

$= \frac{n(n+1) + (n-1)(n+2)}{(n+1)(n+2)} = \frac{n^2 + n + n^2 + 2n - n - 2}{(n+1)(n+2)} = \frac{2n^2 + 2n - 2}{(n+1)(n+2)}$

$= \frac{2(n^2 + n - 1)}{(n+1)(n+2)}$

Note: The given formula $\frac{n(n+1)}{(n+1)(n+2)} = \frac{n}{n+2}$ doesn't match our calculation. The correct result is $\frac{2(n^2 + n - 1)}{(n+1)(n+2)}$.

## Task 8

Consider the sequence defined by $b_n = \frac{1}{2}(1 + (-1)^n)$ for $n \in \mathbb{N}$.

### 1. Write the first seven terms of this sequence

- $b_0 = \frac{1}{2}(1 + (-1)^0) = \frac{1}{2}(1 + 1) = 1$
- $b_1 = \frac{1}{2}(1 + (-1)^1) = \frac{1}{2}(1 - 1) = 0$
- $b_2 = \frac{1}{2}(1 + (-1)^2) = \frac{1}{2}(1 + 1) = 1$
- $b_3 = \frac{1}{2}(1 + (-1)^3) = \frac{1}{2}(1 - 1) = 0$
- $b_4 = \frac{1}{2}(1 + (-1)^4) = \frac{1}{2}(1 + 1) = 1$
- $b_5 = \frac{1}{2}(1 + (-1)^5) = \frac{1}{2}(1 - 1) = 0$
- $b_6 = \frac{1}{2}(1 + (-1)^6) = \frac{1}{2}(1 + 1) = 1$

**First seven terms:** $1, 0, 1, 0, 1, 0, 1$

### 2. What is the set of all values of this sequence?

The sequence alternates between 1 (when $n$ is even) and 0 (when $n$ is odd).

**Set of all values:** $\{0, 1\}$

