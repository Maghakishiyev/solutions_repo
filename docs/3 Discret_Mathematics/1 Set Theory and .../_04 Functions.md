# Functions

## Basics

### Task 1

**Question:** For function $f: \mathbb{R} \to \mathbb{R}$ defined as:
$$f(x) = \begin{cases}
x^3, & \text{if } x \geq 1, \\
x, & \text{if } 0 \leq x < 1, \\
-x^3, & \text{if } x < 0.
\end{cases}$$

### Solution:

#### 1. Calculate function values:

- $f(3) = 3^3 = 27$ (since $3 \geq 1$)
- $f(1/3) = 1/3$ (since $0 \leq 1/3 < 1$)
- $f(-1/3) = -(-1/3)^3 = -(-1/27) = 1/27$ (since $-1/3 < 0$)
- $f(-3) = -(-3)^3 = -(-27) = 27$ (since $-3 < 0$)

#### 2. Graph description:
- For $x \geq 1$: cubic function $y = x^3$
- For $0 \leq x < 1$: linear function $y = x$
- For $x < 0$: reflected cubic function $y = -x^3$

#### 3. Image of $f$:
- For $x \geq 1$: $f(x) = x^3 \geq 1$, so range is $[1, \infty)$
- For $0 \leq x < 1$: $f(x) = x \in [0, 1)$
- For $x < 0$: $f(x) = -x^3 > 0$, and as $x \to -\infty$, $f(x) \to \infty$, so range is $(0, \infty)$

**Answer:** $\text{Im}(f) = [0, \infty)$

### Task 2

**Question:** Let $S = \{1, 2, 3, 4, 5\}$ and $T = \{a, b, c, d\}$. Answer YES or NO with justification:

### Solution:

Given: $|S| = 5$ and $|T| = 4$

1. **Are there injective functions from $S$ to $T$?**
   
   **NO.** For a function to be injective, distinct elements in the domain must map to distinct elements in the codomain. Since $|S| = 5 > 4 = |T|$, by the pigeonhole principle, at least two elements of $S$ must map to the same element of $T$.

2. **Are there surjective functions from $S$ to $T$?**
   
   **YES.** Since $|S| = 5 > 4 = |T|$, we can map at least one element of $S$ to each element of $T$, ensuring every element of $T$ is hit.

3. **Are there injective functions from $T$ to $S$?**
   
   **YES.** Since $|T| = 4 < 5 = |S|$, we can map each element of $T$ to a distinct element of $S$.

4. **Are there surjective functions from $T$ to $S$?**
   
   **NO.** Since $|T| = 4 < 5 = |S|$, we cannot hit all 5 elements of $S$ with only 4 elements from $T$.

5. **Are there bijections between $S$ and $T$?**
   
   **NO.** A bijection requires the sets to have the same cardinality. Since $|S| = 5 \neq 4 = |T|$, no bijection exists.

### Task 4

**Question:** Let $S = \{1, 2, 3, 4, 5\}$. Consider functions:
- $f(n) = n$
- $g(n) = 6 - n$
- $h(n) = \max(3, n)$
- $k(n) = \max(1, n - 1)$

### Solution:

#### 1. Functions as sets of ordered pairs:

- $f = \{(1,1), (2,2), (3,3), (4,4), (5,5)\}$
- $g = \{(1,5), (2,4), (3,3), (4,2), (5,1)\}$
- $h = \{(1,3), (2,3), (3,3), (4,4), (5,5)\}$
- $k = \{(1,1), (2,1), (3,2), (4,3), (5,4)\}$

#### 2. Graph sketches:
- $f$: Identity function (diagonal line)
- $g$: Decreasing linear function
- $h$: Constant 3 for $n \leq 3$, then identity
- $k$: Constant 1 for $n \leq 2$, then $n-1$

#### 3. Injective functions:
- $f$: **Injective** (identity function)
- $g$: **Injective** (strictly decreasing)
- $h$: **Not injective** ($h(1) = h(2) = h(3) = 3$)
- $k$: **Not injective** ($k(1) = k(2) = 1$)

### Task 5

**Question:** Define $f: \mathbb{N} \times \mathbb{N} \to \mathbb{N}$ as $f(m, n) = 2^{m + 3n}$.

### Solution:

#### 1. Five distinct function values:
- $f(0,0) = 2^{0+0} = 1$
- $f(1,0) = 2^{1+0} = 2$
- $f(0,1) = 2^{0+3} = 8$
- $f(2,0) = 2^{2+0} = 4$
- $f(1,1) = 2^{1+3} = 16$

#### 2. Why $f$ is not injective:
$f$ is not injective because different pairs can give the same output. For example:
- $f(3,0) = 2^3 = 8$
- $f(0,1) = 2^3 = 8$

So $(3,0) \neq (0,1)$ but $f(3,0) = f(0,1)$.

#### 3. Does $f$ map onto $\mathbb{N}$?
**NO.** The range of $f$ consists only of powers of 2: $\{1, 2, 4, 8, 16, 32, ...\}$. Numbers like 3, 5, 6, 7, etc., are not in the image of $f$.

#### 4. Show $g(m, n) = 2^{4m}n$ is not injective:
- $g(0,2) = 2^0 \cdot 2 = 2$
- $g(0,2) = 2^0 \cdot 2 = 2$

But we can find: $g(1,1) = 2^4 \cdot 1 = 16$ and $g(0,16) = 2^0 \cdot 16 = 16$.
So $(1,1) \neq (0,16)$ but $g(1,1) = g(0,16)$, proving $g$ is not injective.

### Task 6

**Question:** Define functions on $\mathbb{N}$:
- $f(n) = 3n$
- $g(n) = n + (-1)^n$
- $h(n) = \min(n, 100)$
- $k(n) = \max(10, n - 5)$

### Solution:

#### 1. Which functions are injective?

- $f(n) = 3n$: **Injective** (if $3m = 3n$ then $m = n$)
- $g(n) = n + (-1)^n$: **Not injective** ($g(0) = 0 + 1 = 1$ and $g(2) = 2 - 1 = 1$)
- $h(n) = \min(n, 100)$: **Not injective** ($h(100) = h(101) = h(102) = ... = 100$)
- $k(n) = \max(10, n - 5)$: **Not injective** ($k(0) = k(1) = ... = k(15) = 10$)

#### 2. Which functions map $\mathbb{N}$ onto $\mathbb{N}$?

- $f(n) = 3n$: **Not surjective** (numbers like 1, 2, 4, 5, 7, 8, ... are not multiples of 3)
- $g(n) = n + (-1)^n$: **Not surjective** (only produces values $\geq 0$, and pattern analysis shows gaps)
- $h(n) = \min(n, 100)$: **Not surjective** (never produces values > 100)
- $k(n) = \max(10, n - 5)$: **Not surjective** (never produces values < 10)

**None** of these functions are surjective onto $\mathbb{N}$.

## Function Composition

### Task 1

**Question:** Define functions $f(x) = x^3 - 4x$, $g(x) = \frac{1}{x^2 + 1}$, $h(x) = x^4$. Find compositions:

### Solution:

1. **$f \circ g$:**
   $(f \circ g)(x) = f(g(x)) = f\left(\frac{1}{x^2 + 1}\right) = \left(\frac{1}{x^2 + 1}\right)^3 - 4\left(\frac{1}{x^2 + 1}\right)$
   
   $= \frac{1}{(x^2 + 1)^3} - \frac{4}{x^2 + 1}$

2. **$g \circ f$:**
   $(g \circ f)(x) = g(f(x)) = g(x^3 - 4x) = \frac{1}{(x^3 - 4x)^2 + 1}$

3. **$h \circ g$:**
   $(h \circ g)(x) = h(g(x)) = h\left(\frac{1}{x^2 + 1}\right) = \left(\frac{1}{x^2 + 1}\right)^4 = \frac{1}{(x^2 + 1)^4}$

4. **$g \circ h$:**
   $(g \circ h)(x) = g(h(x)) = g(x^4) = \frac{1}{(x^4)^2 + 1} = \frac{1}{x^8 + 1}$

### Task 2

**Question:** Show that if $f: S \to T$ and $g: T \to U$ are injective, then $g \circ f$ is injective.

### Solution:

**Proof:** Let $f: S \to T$ and $g: T \to U$ be injective functions.

To prove $(g \circ f)$ is injective, we need to show: if $(g \circ f)(x_1) = (g \circ f)(x_2)$, then $x_1 = x_2$.

Assume $(g \circ f)(x_1) = (g \circ f)(x_2)$ for some $x_1, x_2 \in S$.

Then $g(f(x_1)) = g(f(x_2))$.

Since $g$ is injective, this implies $f(x_1) = f(x_2)$.

Since $f$ is injective, this implies $x_1 = x_2$.

Therefore, $g \circ f$ is injective. ∎

### Task 15

**Question:** Let $f(n) = n - 1$ and $g(n) = \begin{cases} 1, & \text{if } n \text{ is even} \\ 0, & \text{if } n \text{ is odd} \end{cases}$

### Solution:

#### 1. Compute compositions:
- $(g \circ f)(6) = g(f(6)) = g(5) = 0$ (since 5 is odd)
- $(g \circ f)(7) = g(f(7)) = g(6) = 1$ (since 6 is even)
- $(g \circ f)(11) = g(f(11)) = g(10) = 1$ (since 10 is even)
- $(g \circ f)(12) = g(f(12)) = g(11) = 0$ (since 11 is odd)

#### 2. Determine $g \circ f$ and $f \circ g$:

**$g \circ f$:** $(g \circ f)(n) = g(n-1) = \begin{cases} 1, & \text{if } n-1 \text{ is even (i.e., } n \text{ is odd)} \\ 0, & \text{if } n-1 \text{ is odd (i.e., } n \text{ is even)} \end{cases}$

**$f \circ g$:** $(f \circ g)(n) = f(g(n)) = \begin{cases} f(1) = 0, & \text{if } n \text{ is even} \\ f(0) = -1, & \text{if } n \text{ is odd} \end{cases}$

#### 3. Show $g \circ f \neq f \circ g$:
- $(g \circ f)(2) = 0$ but $(f \circ g)(2) = 0$
- $(g \circ f)(3) = 1$ but $(f \circ g)(3) = -1$

Since the values differ, $g \circ f \neq f \circ g$.

The second part follows from the definition: $g \circ f$ outputs 0 exactly when $n$ is even.

## Inverse Functions

### Task 1

**Question:** Find inverse functions:

### Solution:

1. **$f(x) = 2x + 3$:**
   Let $y = 2x + 3$, solve for $x$: $x = \frac{y-3}{2}$
   **Answer:** $f^{-1}(x) = \frac{x-3}{2}$

2. **$g(x) = x^3 - 2$:**
   Let $y = x^3 - 2$, solve for $x$: $x = \sqrt[3]{y + 2}$
   **Answer:** $g^{-1}(x) = \sqrt[3]{x + 2}$

3. **$h(x) = (x - 2)^3$:**
   Let $y = (x - 2)^3$, solve for $x$: $x = \sqrt[3]{y} + 2$
   **Answer:** $h^{-1}(x) = \sqrt[3]{x} + 2$

4. **$k(x) = \sqrt{x} + 7$:** (assuming $x \geq 0$)
   Let $y = \sqrt{x} + 7$, solve for $x$: $x = (y - 7)^2$
   **Answer:** $k^{-1}(x) = (x - 7)^2$ for $x \geq 7$

### Task 2

**Question:** Analyze calculator functions $\log x$, $x^2$, $\sqrt{x}$, and $1/x$.

### Solution:

#### 1. Domains:
- $\log x$: $(0, \infty)$
- $x^2$: $\mathbb{R}$
- $\sqrt{x}$: $[0, \infty)$
- $1/x$: $\mathbb{R} \setminus \{0\}$

#### 2. Inverse relationships:
- $\log x$ and $10^x$ (or $e^x$) are inverses
- $x^2$ and $\sqrt{x}$ are inverses on appropriate restricted domains
- $1/x$ is its own inverse (self-inverse)

### Task 3

**Question:** Functions mapping $\mathcal{P}(N) \times \mathcal{P}(N) \to \mathcal{P}(N)$:
- SUM$(A, B) = A \cup B$
- PRODUCT$(A, B) = A \cap B$  
- SYM$(A, B) = A \oplus B$

### Solution:

#### 1. Well-defined functions:
All three operations (union, intersection, symmetric difference) on subsets of $N$ produce subsets of $N$, so they are well-defined.

#### 2. None are injective:
- SUM: $\{1\} \cup \{2\} = \{1,2\} = \{1,2\} \cup \emptyset$
- PRODUCT: $\{1\} \cap \{2\} = \emptyset = \{3\} \cap \{4\}$
- SYM: $\{1\} \oplus \{1\} = \emptyset = \{2\} \oplus \{2\}$

#### 3. Preimage sizes (assuming $N = \{0,1,2,3,4\}$):
For a 5-element set, $|\mathcal{P}(N)| = 32$.

**$F^{-1}(\{\emptyset\})$:**
- SUM: Only $(\emptyset, \emptyset)$ gives $\emptyset$. Size: 1
- PRODUCT: Any disjoint sets. Size: many pairs
- SYM: Identical sets $(A,A)$. Size: 32

**$F^{-1}(\{\{4\}\})$:**
- SUM: Pairs where union is $\{4\}$
- PRODUCT: Pairs where intersection is $\{4\}$  
- SYM: Pairs whose symmetric difference is $\{4\}$

### Task 4

**Question:** Functions $f(n) = n + 1$ and $g(n) = \max(0, n - 1)$ on $\mathbb{N}$.

### Solution:

#### 1. Calculate $f(n)$:
$f(0) = 1, f(1) = 2, f(2) = 3, f(3) = 4, f(4) = 5, f(73) = 74$

#### 2. Calculate $g(n)$:
$g(0) = 0, g(1) = 0, g(2) = 1, g(3) = 2, g(4) = 3, g(73) = 72$

#### 3. Properties of $f$:
- **Injective:** If $f(m) = f(n)$, then $m + 1 = n + 1$, so $m = n$.
- **Not surjective:** 0 is not in the range of $f$.

#### 4. Properties of $g$:
- **Surjective:** For any $k \in \mathbb{N}$, $g(k+1) = k$.
- **Not injective:** $g(0) = g(1) = 0$.

#### 5. Compositions:
- $(g \circ f)(n) = g(n+1) = \max(0, n) = n$ for all $n \in \mathbb{N}$, so $g \circ f = 1_\mathbb{N}$
- $(f \circ g)(0) = f(0) = 1 \neq 0$, so $f \circ g \neq 1_\mathbb{N}$

### Task 5

**Question:** Show functions are self-inverse if $f \circ f = 1_S$:

### Solution:

#### 1. $f(x) = 1/x$ on $(0, \infty)$:
$(f \circ f)(x) = f(f(x)) = f(1/x) = 1/(1/x) = x$ ✓

#### 2. $f(A) = A^c$ for $A \subseteq S$:
$(f \circ f)(A) = f(f(A)) = f(A^c) = (A^c)^c = A$ ✓

#### 3. $f(x) = 1 - x$ on $\mathbb{R}$:
$(f \circ f)(x) = f(f(x)) = f(1-x) = 1-(1-x) = x$ ✓

### Task 6

**Question:** If $f: S \to T$ and $g: T \to U$ are bijections, prove $g \circ f$ is bijection and $(g \circ f)^{-1} = f^{-1} \circ g^{-1}$.

### Solution:

**Proof that $g \circ f$ is bijection:**
- **Injective:** Shown in Task 2 (composition of injective functions)
- **Surjective:** For any $u \in U$, since $g$ is surjective, $\exists t \in T$ such that $g(t) = u$. Since $f$ is surjective, $\exists s \in S$ such that $f(s) = t$. Then $(g \circ f)(s) = g(f(s)) = g(t) = u$.

**Proof of inverse formula:**
Let $h = f^{-1} \circ g^{-1}$. We need to show $h = (g \circ f)^{-1}$.

$(g \circ f) \circ h = (g \circ f) \circ (f^{-1} \circ g^{-1}) = g \circ (f \circ f^{-1}) \circ g^{-1} = g \circ 1_T \circ g^{-1} = g \circ g^{-1} = 1_U$

Similarly, $h \circ (g \circ f) = 1_S$.

Therefore, $(g \circ f)^{-1} = f^{-1} \circ g^{-1}$. ∎

### Task 7

**Question:** Function $f: \mathbb{R} \times \mathbb{R} \to \mathbb{R} \times \mathbb{R}$ as $f(x, y) = (x + y, x - y)$.

### Solution:

#### 1. Prove $f$ is bijection:
**Injective:** If $f(x_1, y_1) = f(x_2, y_2)$, then:
$(x_1 + y_1, x_1 - y_1) = (x_2 + y_2, x_2 - y_2)$

This gives us: $x_1 + y_1 = x_2 + y_2$ and $x_1 - y_1 = x_2 - y_2$

Adding: $2x_1 = 2x_2$, so $x_1 = x_2$
Subtracting: $2y_1 = 2y_2$, so $y_1 = y_2$

Therefore $(x_1, y_1) = (x_2, y_2)$.

#### 2. $f$ maps onto $\mathbb{R} \times \mathbb{R}$:
For any $(a, b) \in \mathbb{R} \times \mathbb{R}$, we need $(x, y)$ such that $f(x, y) = (a, b)$.

From $x + y = a$ and $x - y = b$:
$x = \frac{a + b}{2}$ and $y = \frac{a - b}{2}$

These are real numbers, so $f$ is surjective.

#### 3. Inverse function:
$f^{-1}(a, b) = \left(\frac{a + b}{2}, \frac{a - b}{2}\right)$

#### 4. Compositions:
$(f \circ f^{-1})(a, b) = f\left(\frac{a + b}{2}, \frac{a - b}{2}\right) = (a, b) = 1_{\mathbb{R} \times \mathbb{R}}$

$(f^{-1} \circ f)(x, y) = f^{-1}(x + y, x - y) = (x, y) = 1_{\mathbb{R} \times \mathbb{R}}$