# Set Theory

## Task 1

**Question:** Write down five elements for each of the following sets:

### Solution:

1. $\{n \in \mathbb{N}: n \text{ is divisible by 5}\}$
   
   **Five elements:** $0, 5, 10, 15, 20$

2. $\{2n + 1: n \in \mathbb{N}_{+}\}$
   
   For $n = 1, 2, 3, 4, 5$: $2(1)+1=3, 2(2)+1=5, 2(3)+1=7, 2(4)+1=9, 2(5)+1=11$
   
   **Five elements:** $3, 5, 7, 9, 11$

3. $\mathcal{P}(\{1, 2, 3, 4, 5\})$ (power set)
   
   **Five elements:** $\emptyset, \{1\}, \{2\}, \{1,2\}, \{1,2,3\}$

4. $\{2^n: n \in \mathbb{N}\}$
   
   For $n = 0, 1, 2, 3, 4$: $2^0=1, 2^1=2, 2^2=4, 2^3=8, 2^4=16$
   
   **Five elements:** $1, 2, 4, 8, 16$

5. $\{1/n: n \in \mathbb{N}_{+}\}$
   
   For $n = 1, 2, 3, 4, 5$: $1/1=1, 1/2=0.5, 1/3≈0.333, 1/4=0.25, 1/5=0.2$
   
   **Five elements:** $1, \frac{1}{2}, \frac{1}{3}, \frac{1}{4}, \frac{1}{5}$

6. $\{r \in \mathbb{Q}: 0 < r < 1\}$
   
   **Five elements:** $\frac{1}{2}, \frac{1}{3}, \frac{2}{3}, \frac{1}{4}, \frac{3}{4}$

7. $\{n \in \mathbb{N}: n + 1 \text{ is a prime number}\}$
   
   We need $n$ such that $n+1$ is prime. If $n+1$ is prime, then $n+1 \in \{2,3,5,7,11,...\}$
   So $n \in \{1,2,4,6,10,...\}$
   
   **Five elements:** $1, 2, 4, 6, 10$

## Task 2

**Question:** Write the elements of the following sets:

### Solution:

1. $\{1/n: n = 1, 2, 3, 4\}$
   
   **Elements:** $\{1, \frac{1}{2}, \frac{1}{3}, \frac{1}{4}\}$

2. $\{n^2 - n: n = 0, 1, 2, 3, 4\}$
   
   For $n = 0, 1, 2, 3, 4$: $0-0=0, 1-1=0, 4-2=2, 9-3=6, 16-4=12$
   
   **Elements:** $\{0, 2, 6, 12\}$

3. $\{1/n^2: n \in \mathbb{P}, n \text{ is even}\}$
   
   The only even prime number is $2$.
   
   **Elements:** $\{\frac{1}{4}\}$

4. $\{2 + (-1)^n: n \in \mathbb{N}\}$
   
   For even $n$: $2 + (-1)^n = 2 + 1 = 3$
   For odd $n$: $2 + (-1)^n = 2 - 1 = 1$
   
   **Elements:** $\{1, 3\}$

## Task 3

**Question:** Determine the following sets, i.e., write down their elements if the sets are non-empty and write $\emptyset$ if they are empty:

### Solution:

1. $\{n \in \mathbb{N}: n^2 = 9\}$
   
   Since $3^2 = 9$ and $3 \in \mathbb{N}$: $\{3\}$

2. $\{n \in \mathbb{Z}: n^2 = 9\}$
   
   Since $(\pm 3)^2 = 9$: $\{-3, 3\}$

3. $\{n \in \mathbb{Z}: n^2 = -9\}$
   
   No real number squared equals a negative number: $\emptyset$

4. $\{n \in \mathbb{N}: 3 < n < 7\}$
   
   Natural numbers between 3 and 7: $\{4, 5, 6\}$

5. $\{n \in \mathbb{Z}: 3 < |n| < 7\}$
   
   We need $|n| \in \{4, 5, 6\}$, so $n \in \{-6, -5, -4, 4, 5, 6\}$

6. $\{x \in \mathbb{Q}: x^2 = 2\}$
   
   $\sqrt{2}$ is irrational, so no rational solution exists: $\emptyset$

7. $\{x \in \mathbb{R}: x^2 = 2\}$
   
   Real solutions exist: $\{-\sqrt{2}, \sqrt{2}\}$

8. $\{x \in \mathbb{R}: x^2 = -2\}$
   
   No real solutions: $\emptyset$

9. $\{x \in \mathbb{R}: x < 1 \land x \geq 2\}$
   
   No number can be both less than 1 and greater than or equal to 2: $\emptyset$

10. $\{3n + 1: n \in \mathbb{N} \land n \leq 6\}$
    
    For $n = 0, 1, 2, 3, 4, 5, 6$: $1, 4, 7, 10, 13, 16, 19$
    
    **Elements:** $\{1, 4, 7, 10, 13, 16, 19\}$

11. $\{n \in \mathbb{P}: n \text{ is a prime number and } n \leq 15\}$
    
    Prime numbers ≤ 15: $\{2, 3, 5, 7, 11, 13\}$

## Task 4

**Question:** How many elements do the following sets have? Write $\infty$ if the set is infinite:

### Solution:

1. $\{n \in \mathbb{N}: n^2 = 2\}$
   
   No natural number squared equals 2: **0 elements**

2. $\{n \in \mathbb{Z}: 0 < |n| \leq 73\}$
   
   $n \in \{-73, -72, ..., -1, 1, 2, ..., 73\}$: **146 elements**

3. $\{n \in \mathbb{Z}: 5 \leq |n| \leq 73\}$
   
   $n \in \{-73, -72, ..., -5, 5, 6, ..., 73\}$: **138 elements**

4. $\{n \in \mathbb{Z}: 5 < |n| < 73\}$
   
   $n \in \{-72, -71, ..., -6, 6, 7, ..., 72\}$: **134 elements**

5. $\{n \in \mathbb{Z}: n \text{ is even and } |n| \leq 73\}$
   
   Even integers from -72 to 72: **74 elements**

6. $\{x \in \mathbb{Q}: 0 < x \leq 73\}$
   
   Infinitely many rational numbers in this interval: **$\infty$**

7. $\{x \in \mathbb{Q}: x^2 = 2\}$
   
   No rational solutions: **0 elements**

8. $\{x \in \mathbb{R}: 0.99 < x < 1.00\}$
   
   Infinitely many real numbers: **$\infty$**

9. $\mathcal{P}(\{0, 1, 2, 3\})$
   
   Power set of 4-element set: **$2^4 = 16$ elements**

10. $\mathcal{P}(\mathbb{N})$
    
    Power set of infinite set: **$\infty$**

11. $\{n \in \mathbb{N}: n \text{ is even}\}$
    
    Infinitely many even natural numbers: **$\infty$**

12. $\{n \in \mathbb{N}: n \text{ is prime}\}$
    
    Infinitely many prime numbers: **$\infty$**

13. $\{n \in \mathbb{N}: n \text{ is even and prime}\}$
    
    Only 2 is even and prime: **1 element**

14. $\{n \in \mathbb{N}: n \text{ is even or prime}\}$
    
    Infinitely many numbers that are either even or prime: **$\infty$**

## Task 5

**Question:** Consider the sets $\{0, 1\}$, $(0, 1)$, and $[0, 1)$. Are the following statements true?

### Solution:

1. $\{0, 1\} \subseteq (0, 1)$
   
   **False.** $(0, 1)$ doesn't contain 0 or 1, so $\{0, 1\} \not\subseteq (0, 1)$

2. $\{0, 1\} \subseteq [0, 1)$
   
   **False.** $[0, 1)$ contains 0 but not 1, so $\{0, 1\} \not\subseteq [0, 1)$

3. $(0, 1) \subseteq \{0, 1\}$
   
   **False.** $(0, 1)$ contains infinitely many elements like $0.5$, while $\{0, 1\}$ only contains 0 and 1

4. $(0, 1) \subseteq [0, 1)$
   
   **True.** Every element in $(0, 1)$ is also in $[0, 1)$

5. $\{0, 1\} \cap (0, 1) = \emptyset$
   
   **True.** $(0, 1)$ contains neither 0 nor 1, so the intersection is empty

6. $(0, 1) \cap \mathbb{Q} = \emptyset$
   
   **False.** There are rational numbers in $(0, 1)$, such as $\frac{1}{2}$

## Task 6

**Question:** Let 
- $U = \{1, 2, 3, 4, 5, \dots, 12\}$
- $A = \{1, 3, 5, 7, 11\}$
- $B = \{2, 3, 5, 7, 11\}$
- $C = \{2, 3, 6, 12\}$
- $D = \{2, 4, 8\}$

Determine the following sets:

### Solution:

1. $A \cup B = \{1, 2, 3, 5, 7, 11\}$

2. $A \cap C = \{3\}$

3. $(A \cup B) \cap C^c$
   
   First: $A \cup B = \{1, 2, 3, 5, 7, 11\}$
   Then: $C^c = U \setminus C = \{1, 4, 5, 7, 8, 9, 10, 11\}$
   Finally: $(A \cup B) \cap C^c = \{1, 5, 7, 11\}$

4. $A \setminus B = \{1\}$

5. $B \oplus D$ (symmetric difference)
   
   $B \oplus D = (B \setminus D) \cup (D \setminus B) = \{3, 5, 7, 11\} \cup \{4, 8\} = \{3, 4, 5, 7, 8, 11\}$

6. How many subsets does the set $C$ have?
   
   $C$ has 4 elements, so it has $2^4 = 16$ subsets.

## Task 7

**Question:** Let $A = \{1, 2, 3\}$, $B = \{n \in \mathbb{P}: n \text{ is even}\}$, and $C = \{n \in \mathbb{P}: n \text{ is odd}\}$.

### Solution:

**Note:** $B = \{2\}$ (only even prime) and $C = \{3, 5, 7, 11, 13, ...\}$ (all odd primes)

1. Determine the sets:
   - $A \cap B = \{1, 2, 3\} \cap \{2\} = \{2\}$
   - $B \cap C = \{2\} \cap \{3, 5, 7, ...\} = \emptyset$
   - $B \cup C = \{2\} \cup \{3, 5, 7, ...\} = \{2, 3, 5, 7, 11, ...\}$ (all primes)
   - $B \oplus C = (B \setminus C) \cup (C \setminus B) = \{2\} \cup \{3, 5, 7, ...\} = \{2, 3, 5, 7, 11, ...\}$

2. All subsets of $A = \{1, 2, 3\}$:
   
   $\mathcal{P}(A) = \{\emptyset, \{1\}, \{2\}, \{3\}, \{1,2\}, \{1,3\}, \{2,3\}, \{1,2,3\}\}$

3. Which sets are infinite?
   - $A \oplus B = \{1, 3\} \cup \{3, 5, 7, ...\} = \{1, 3, 5, 7, 11, ...\}$ → **Infinite**
   - $A \oplus C = \{1, 2\} \cup \emptyset = \{1, 2\}$ → **Finite**
   - $A \setminus C = \{1, 2, 3\} \setminus \{3, 5, 7, ...\} = \{1, 2\}$ → **Finite**

## Task 8

**Question:** What is the set $A \oplus A$ for any set $A$? What is $A \oplus \emptyset$?

### Solution:

1. $A \oplus A$ (symmetric difference of $A$ with itself):
   
   $A \oplus A = (A \setminus A) \cup (A \setminus A) = \emptyset \cup \emptyset = \emptyset$

2. $A \oplus \emptyset$ (symmetric difference of $A$ with empty set):
   
   $A \oplus \emptyset = (A \setminus \emptyset) \cup (\emptyset \setminus A) = A \cup \emptyset = A$

**Answer:** $A \oplus A = \emptyset$ and $A \oplus \emptyset = A$

## Task 9

**Question:** Let $A = \{a, b, c\}$ and $B = \{a, b, d\}$.

### Solution:

1. **All ordered pairs from $A \times A$:**
   
   $A \times A = \{(a,a), (a,b), (a,c), (b,a), (b,b), (b,c), (c,a), (c,b), (c,c)\}$

2. **All ordered pairs from $A \times B$:**
   
   $A \times B = \{(a,a), (a,b), (a,d), (b,a), (b,b), (b,d), (c,a), (c,b), (c,d)\}$

3. **All elements of $\{(x, y): x \in A, y \in B, x = y\}$:**
   
   We need pairs where both coordinates are the same and the first is in $A$, second is in $B$.
   Common elements: $A \cap B = \{a, b\}$
   
   **Result:** $\{(a,a), (b,b)\}$

## Task 10

**Question:** Write the elements of the following sets:

### Solution:

1. $\{(m, n) \in \mathbb{N}^2: m = n\}$
   
   **Elements:** $\{(0,0), (1,1), (2,2), (3,3), (4,4), ...\}$
   
   **Set notation:** All pairs $(n,n)$ where $n \in \mathbb{N}$

2. $\{(m, n) \in \mathbb{N}^2: m + n = 6\}$
   
   **Elements:** $\{(0,6), (1,5), (2,4), (3,3), (4,2), (5,1), (6,0)\}$

3. $\{(m, n) \in \mathbb{N}^2: m = 3 \text{ and } n \text{ is prime}\}$
   
   **Elements:** $\{(3,2), (3,3), (3,5), (3,7), (3,11), (3,13), ...\}$

4. $\{(m, n) \in \mathbb{N}^2: \min(m, n) = 3\}$
   
   At least one coordinate is 3, and the other is ≥ 3:
   
   **Elements:** $\{(3,3), (3,4), (3,5), ..., (4,3), (5,3), (6,3), ...\}$

5. $\{(m, n) \in \mathbb{N}^2: \max(m, n) = 3\}$
   
   At least one coordinate is 3, and both coordinates are ≤ 3:
   
   **Elements:** $\{(0,3), (1,3), (2,3), (3,0), (3,1), (3,2), (3,3)\}$