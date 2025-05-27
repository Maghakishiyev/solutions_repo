# Number Theory

## Task 1

**Question:** Check the following congruences:

### Solution:

1. **$12 \equiv 2 \pmod{5}$**
   
   We need to check if $5$ divides $(12 - 2)$.
   $12 - 2 = 10 = 5 \cdot 2$
   
   Since $5$ divides $10$, the congruence is **TRUE**.

2. **$12 \equiv 3 \pmod{10}$**
   
   We need to check if $10$ divides $(12 - 3)$.
   $12 - 3 = 9$
   
   Since $10$ does not divide $9$, the congruence is **FALSE**.

3. **$21 \equiv 1 \pmod{5}$**
   
   We need to check if $5$ divides $(21 - 1)$.
   $21 - 1 = 20 = 5 \cdot 4$
   
   Since $5$ divides $20$, the congruence is **TRUE**.

4. **$23 \equiv 3 \pmod{4}$**
   
   We need to check if $4$ divides $(23 - 3)$.
   $23 - 3 = 20 = 4 \cdot 5$
   
   Since $4$ divides $20$, the congruence is **TRUE**.

## Task 2

**Question:** Prove that if $a \equiv b \pmod{n}$ and $c \equiv d \pmod{n}$, then:

### Solution:

**Given:** $a \equiv b \pmod{n}$ and $c \equiv d \pmod{n}$

This means:
- $n \mid (a - b)$, so $a - b = kn$ for some integer $k$
- $n \mid (c - d)$, so $c - d = ln$ for some integer $l$

Therefore: $a = b + kn$ and $c = d + ln$

#### 1. Prove: $a + c \equiv b + d \pmod{n}$

**Proof:**
$$a + c = (b + kn) + (d + ln) = (b + d) + (k + l)n$$

Therefore: $(a + c) - (b + d) = (k + l)n$

Since $(k + l)$ is an integer, $n \mid ((a + c) - (b + d))$.

Thus: $a + c \equiv b + d \pmod{n}$ ✓

#### 2. Prove: $a - c \equiv b - d \pmod{n}$

**Proof:**
$$a - c = (b + kn) - (d + ln) = (b - d) + (k - l)n$$

Therefore: $(a - c) - (b - d) = (k - l)n$

Since $(k - l)$ is an integer, $n \mid ((a - c) - (b - d))$.

Thus: $a - c \equiv b - d \pmod{n}$ ✓

#### 3. Prove: $ac \equiv bd \pmod{n}$

**Proof:**
$$ac = (b + kn)(d + ln) = bd + b(ln) + d(kn) + (kn)(ln)$$
$$= bd + bln + dkn + kln^2 = bd + n(bl + dk + kln)$$

Therefore: $ac - bd = n(bl + dk + kln)$

Since $(bl + dk + kln)$ is an integer, $n \mid (ac - bd)$.

Thus: $ac \equiv bd \pmod{n}$ ✓

#### 4. Prove: $a^k \equiv b^k \pmod{n}$ for all $k \in \mathbb{N}$

**Proof by induction:**

**Base case:** $k = 1$
$a^1 \equiv b^1 \pmod{n}$ is given.

**Inductive step:** Assume $a^k \equiv b^k \pmod{n}$ for some $k \geq 1$.

We want to show: $a^{k+1} \equiv b^{k+1} \pmod{n}$

$$a^{k+1} = a \cdot a^k$$

By the inductive hypothesis: $a^k \equiv b^k \pmod{n}$
By the given condition: $a \equiv b \pmod{n}$

Using the multiplication property (part 3):
$$a \cdot a^k \equiv b \cdot b^k \pmod{n}$$
$$a^{k+1} \equiv b^{k+1} \pmod{n}$$

By mathematical induction, $a^k \equiv b^k \pmod{n}$ for all $k \in \mathbb{N}$ ✓

## Task 3

**Question:** Compute the following greatest common divisors using the Euclidean algorithm:

### Solution:

#### 1. $\gcd(12, 75)$

**Euclidean Algorithm:**
$$75 = 12 \cdot 6 + 3$$
$$12 = 3 \cdot 4 + 0$$

Since the remainder is 0, $\gcd(12, 75) = 3$.

#### 2. $\gcd(12, 68)$

**Euclidean Algorithm:**
$$68 = 12 \cdot 5 + 8$$
$$12 = 8 \cdot 1 + 4$$
$$8 = 4 \cdot 2 + 0$$

Since the remainder is 0, $\gcd(12, 68) = 4$.

#### 3. $\gcd(72, 55)$

**Euclidean Algorithm:**
$$72 = 55 \cdot 1 + 17$$
$$55 = 17 \cdot 3 + 4$$
$$17 = 4 \cdot 4 + 1$$
$$4 = 1 \cdot 4 + 0$$

Since the remainder is 0, $\gcd(72, 55) = 1$.

#### 4. $\gcd(45, 42)$

**Euclidean Algorithm:**
$$45 = 42 \cdot 1 + 3$$
$$42 = 3 \cdot 14 + 0$$

Since the remainder is 0, $\gcd(45, 42) = 3$.

## Task 4

**Question:** Compute the following least common multiples:

### Solution:

We use the formula: $\text{lcm}(a, b) = \frac{|a \cdot b|}{\gcd(a, b)}$

#### 1. $\text{lcm}(12, 10)$

First find $\gcd(12, 10)$:
$$12 = 10 \cdot 1 + 2$$
$$10 = 2 \cdot 5 + 0$$

So $\gcd(12, 10) = 2$.

Therefore: $\text{lcm}(12, 10) = \frac{12 \cdot 10}{2} = \frac{120}{2} = 60$

#### 2. $\text{lcm}(12, 14)$

First find $\gcd(12, 14)$:
$$14 = 12 \cdot 1 + 2$$
$$12 = 2 \cdot 6 + 0$$

So $\gcd(12, 14) = 2$.

Therefore: $\text{lcm}(12, 14) = \frac{12 \cdot 14}{2} = \frac{168}{2} = 84$

#### 3. $\text{lcm}(72, 25)$

First find $\gcd(72, 25)$:
$$72 = 25 \cdot 2 + 22$$
$$25 = 22 \cdot 1 + 3$$
$$22 = 3 \cdot 7 + 1$$
$$3 = 1 \cdot 3 + 0$$

So $\gcd(72, 25) = 1$.

Therefore: $\text{lcm}(72, 25) = \frac{72 \cdot 25}{1} = 1800$

#### 4. $\text{lcm}(45, 60)$

First find $\gcd(45, 60)$:
$$60 = 45 \cdot 1 + 15$$
$$45 = 15 \cdot 3 + 0$$

So $\gcd(45, 60) = 15$.

Therefore: $\text{lcm}(45, 60) = \frac{45 \cdot 60}{15} = \frac{2700}{15} = 180$

## Task 5

**Question:** Solve congruences of the form $ax \equiv b \pmod{m}$:

### Solution:

To solve $ax \equiv b \pmod{m}$, we need $\gcd(a, m) \mid b$ for a solution to exist.

#### 1. $2x \equiv 3 \pmod{5}$

Check: $\gcd(2, 5) = 1$ and $1 \mid 3$ ✓

We need the multiplicative inverse of $2$ modulo $5$.
Since $2 \cdot 3 = 6 \equiv 1 \pmod{5}$, we have $2^{-1} \equiv 3 \pmod{5}$.

Therefore: $x \equiv 3 \cdot 3 \equiv 9 \equiv 4 \pmod{5}$

**Answer:** $x \equiv 4 \pmod{5}$

#### 2. $3x \equiv 4 \pmod{7}$

Check: $\gcd(3, 7) = 1$ and $1 \mid 4$ ✓

We need the multiplicative inverse of $3$ modulo $7$.
Since $3 \cdot 5 = 15 \equiv 1 \pmod{7}$, we have $3^{-1} \equiv 5 \pmod{7}$.

Therefore: $x \equiv 4 \cdot 5 \equiv 20 \equiv 6 \pmod{7}$

**Answer:** $x \equiv 6 \pmod{7}$

#### 3. $4x \equiv 5 \pmod{6}$

Check: $\gcd(4, 6) = 2$ and $2 \nmid 5$ ✗

Since $\gcd(4, 6) = 2$ does not divide $5$, this congruence has **no solution**.

#### 4. $5x \equiv 6 \pmod{8}$

Check: $\gcd(5, 8) = 1$ and $1 \mid 6$ ✓

We need the multiplicative inverse of $5$ modulo $8$.
Since $5 \cdot 5 = 25 \equiv 1 \pmod{8}$, we have $5^{-1} \equiv 5 \pmod{8}$.

Therefore: $x \equiv 6 \cdot 5 \equiv 30 \equiv 6 \pmod{8}$

**Answer:** $x \equiv 6 \pmod{8}$

#### 5. $6x \equiv 7 \pmod{9}$

Check: $\gcd(6, 9) = 3$ and $3 \nmid 7$ ✗

Since $\gcd(6, 9) = 3$ does not divide $7$, this congruence has **no solution**.

### Summary of Solutions:

1. $x \equiv 4 \pmod{5}$
2. $x \equiv 6 \pmod{7}$
3. No solution
4. $x \equiv 6 \pmod{8}$
5. No solution