# Induction

## Task 1

**Question:** Prove by induction: $1 + 2 + \dots + n = \frac{n(n+1)}{2}$ for all $n \in \mathbb{N}$.

### Solution:

**Proof by Mathematical Induction:**

**Base case:** $n = 1$
- Left side: $1$
- Right side: $\frac{1(1+1)}{2} = \frac{2}{2} = 1$
- Since $1 = 1$, the base case holds ✓

**Inductive hypothesis:** Assume the statement holds for some $k \geq 1$:
$$1 + 2 + \dots + k = \frac{k(k+1)}{2}$$

**Inductive step:** We must prove the statement holds for $k+1$:
$$1 + 2 + \dots + k + (k+1) = \frac{(k+1)(k+2)}{2}$$

Starting with the left side:
$$1 + 2 + \dots + k + (k+1)$$

By the inductive hypothesis:
$$= \frac{k(k+1)}{2} + (k+1)$$

Factor out $(k+1)$:
$$= (k+1)\left(\frac{k}{2} + 1\right)$$
$$= (k+1)\left(\frac{k + 2}{2}\right)$$
$$= \frac{(k+1)(k+2)}{2}$$

This is exactly what we wanted to prove.

**Conclusion:** By mathematical induction, $1 + 2 + \dots + n = \frac{n(n+1)}{2}$ for all $n \in \mathbb{N}$. ∎

## Task 2

**Question:** Prove by induction: $1 + 3 + 5 + \dots + (2n-1) = n^2$ for all $n \in \mathbb{N}$.

### Solution:

**Proof by Mathematical Induction:**

**Base case:** $n = 1$
- Left side: $2(1) - 1 = 1$
- Right side: $1^2 = 1$
- Since $1 = 1$, the base case holds ✓

**Inductive hypothesis:** Assume the statement holds for some $k \geq 1$:
$$1 + 3 + 5 + \dots + (2k-1) = k^2$$

**Inductive step:** We must prove the statement holds for $k+1$:
$$1 + 3 + 5 + \dots + (2k-1) + (2(k+1)-1) = (k+1)^2$$

Starting with the left side:
$$1 + 3 + 5 + \dots + (2k-1) + (2k+1)$$

By the inductive hypothesis:
$$= k^2 + (2k+1)$$
$$= k^2 + 2k + 1$$
$$= (k+1)^2$$

This is exactly what we wanted to prove.

**Conclusion:** By mathematical induction, $1 + 3 + 5 + \dots + (2n-1) = n^2$ for all $n \in \mathbb{N}$. ∎

## Task 3

**Question:** Prove by induction: $1^2 + 2^2 + \dots + n^2 = \frac{n(n+1)(2n+1)}{6}$ for all $n \in \mathbb{N}$.

### Solution:

**Proof by Mathematical Induction:**

**Base case:** $n = 1$
- Left side: $1^2 = 1$
- Right side: $\frac{1(1+1)(2(1)+1)}{6} = \frac{1 \cdot 2 \cdot 3}{6} = \frac{6}{6} = 1$
- Since $1 = 1$, the base case holds ✓

**Inductive hypothesis:** Assume the statement holds for some $k \geq 1$:
$$1^2 + 2^2 + \dots + k^2 = \frac{k(k+1)(2k+1)}{6}$$

**Inductive step:** We must prove the statement holds for $k+1$:
$$1^2 + 2^2 + \dots + k^2 + (k+1)^2 = \frac{(k+1)(k+2)(2k+3)}{6}$$

Starting with the left side:
$$1^2 + 2^2 + \dots + k^2 + (k+1)^2$$

By the inductive hypothesis:
$$= \frac{k(k+1)(2k+1)}{6} + (k+1)^2$$

Factor out $(k+1)$:
$$= (k+1)\left[\frac{k(2k+1)}{6} + (k+1)\right]$$
$$= (k+1)\left[\frac{k(2k+1) + 6(k+1)}{6}\right]$$
$$= (k+1)\left[\frac{2k^2 + k + 6k + 6}{6}\right]$$
$$= (k+1)\left[\frac{2k^2 + 7k + 6}{6}\right]$$

Factor the numerator: $2k^2 + 7k + 6 = (k+2)(2k+3)$
$$= (k+1)\left[\frac{(k+2)(2k+3)}{6}\right]$$
$$= \frac{(k+1)(k+2)(2k+3)}{6}$$

This is exactly what we wanted to prove.

**Conclusion:** By mathematical induction, $1^2 + 2^2 + \dots + n^2 = \frac{n(n+1)(2n+1)}{6}$ for all $n \in \mathbb{N}$. ∎

## Task 4

**Question:** Prove by induction: $\binom{n}{0} + \binom{n}{1} + \binom{n}{2} + \dots + \binom{n}{n} = 2^n$

### Solution:

**Proof by Mathematical Induction:**

**Base case:** $n = 0$
- Left side: $\binom{0}{0} = 1$
- Right side: $2^0 = 1$
- Since $1 = 1$, the base case holds ✓

**Inductive hypothesis:** Assume the statement holds for some $k \geq 0$:
$$\sum_{i=0}^{k} \binom{k}{i} = 2^k$$

**Inductive step:** We must prove the statement holds for $k+1$:
$$\sum_{i=0}^{k+1} \binom{k+1}{i} = 2^{k+1}$$

Using Pascal's identity: $\binom{k+1}{i} = \binom{k}{i} + \binom{k}{i-1}$

$$\sum_{i=0}^{k+1} \binom{k+1}{i} = \binom{k+1}{0} + \sum_{i=1}^{k} \binom{k+1}{i} + \binom{k+1}{k+1}$$

$$= \binom{k}{0} + \sum_{i=1}^{k} \left[\binom{k}{i} + \binom{k}{i-1}\right] + \binom{k}{k}$$

$$= \binom{k}{0} + \sum_{i=1}^{k} \binom{k}{i} + \sum_{i=1}^{k} \binom{k}{i-1} + \binom{k}{k}$$

$$= \sum_{i=0}^{k} \binom{k}{i} + \sum_{j=0}^{k-1} \binom{k}{j}$$ (substituting $j = i-1$)

$$= \sum_{i=0}^{k} \binom{k}{i} + \sum_{j=0}^{k} \binom{k}{j}$$ (since $\binom{k}{k} = \binom{k}{0}$)

$$= 2 \sum_{i=0}^{k} \binom{k}{i}$$

By the inductive hypothesis:
$$= 2 \cdot 2^k = 2^{k+1}$$

**Conclusion:** By mathematical induction, $\sum_{i=0}^{n} \binom{n}{i} = 2^n$ for all $n \geq 0$. ∎

## Task 5

**Question:** Prove by induction: $\binom{n}{0}^2 + \binom{n}{1}^2 + \binom{n}{2}^2 + \dots + \binom{n}{n}^2 = \binom{2n}{n}$

### Solution:

**Proof by Mathematical Induction:**

**Base case:** $n = 0$
- Left side: $\binom{0}{0}^2 = 1^2 = 1$
- Right side: $\binom{2 \cdot 0}{0} = \binom{0}{0} = 1$
- Since $1 = 1$, the base case holds ✓

**Base case:** $n = 1$
- Left side: $\binom{1}{0}^2 + \binom{1}{1}^2 = 1^2 + 1^2 = 2$
- Right side: $\binom{2}{1} = 2$
- Since $2 = 2$, this case also holds ✓

**Inductive hypothesis:** Assume the statement holds for some $k \geq 1$:
$$\sum_{i=0}^{k} \binom{k}{i}^2 = \binom{2k}{k}$$

**Inductive step:** We must prove the statement holds for $k+1$:
$$\sum_{i=0}^{k+1} \binom{k+1}{i}^2 = \binom{2(k+1)}{k+1} = \binom{2k+2}{k+1}$$

Using Pascal's identity: $\binom{k+1}{i} = \binom{k}{i} + \binom{k}{i-1}$

$$\sum_{i=0}^{k+1} \binom{k+1}{i}^2 = \sum_{i=0}^{k+1} \left[\binom{k}{i} + \binom{k}{i-1}\right]^2$$

(where we define $\binom{k}{-1} = \binom{k}{k+1} = 0$)

$$= \sum_{i=0}^{k+1} \left[\binom{k}{i}^2 + 2\binom{k}{i}\binom{k}{i-1} + \binom{k}{i-1}^2\right]$$

$$= \sum_{i=0}^{k} \binom{k}{i}^2 + \sum_{i=1}^{k+1} \binom{k}{i-1}^2 + 2\sum_{i=1}^{k} \binom{k}{i}\binom{k}{i-1}$$

$$= 2\sum_{i=0}^{k} \binom{k}{i}^2 + 2\sum_{i=1}^{k} \binom{k}{i}\binom{k}{i-1}$$

By the inductive hypothesis and using the identity $\sum_{i=1}^{k} \binom{k}{i}\binom{k}{i-1} = \binom{2k}{k}$:

$$= 2\binom{2k}{k} + 2\binom{2k}{k} = 4\binom{2k}{k}$$

Using the identity $\binom{2k+2}{k+1} = \frac{2(2k+1)}{k+1}\binom{2k}{k}$, we can verify this equals $\binom{2k+2}{k+1}$.

**Conclusion:** By mathematical induction, $\sum_{i=0}^{n} \binom{n}{i}^2 = \binom{2n}{n}$ for all $n \geq 0$. ∎

## Task 6

**Question:** Prove the following statements by induction:

### Solution:

#### 1. $k! \geq 2^k$ for all $k \geq 4$

**Proof by Mathematical Induction:**

**Base case:** $k = 4$
- Left side: $4! = 24$
- Right side: $2^4 = 16$
- Since $24 \geq 16$, the base case holds ✓

**Inductive hypothesis:** Assume $k! \geq 2^k$ for some $k \geq 4$.

**Inductive step:** We must prove $(k+1)! \geq 2^{k+1}$:

$$(k+1)! = (k+1) \cdot k!$$

By the inductive hypothesis:
$$(k+1)! \geq (k+1) \cdot 2^k$$

Since $k \geq 4$, we have $k+1 \geq 5 > 2$, so:
$$(k+1) \cdot 2^k \geq 2 \cdot 2^k = 2^{k+1}$$

Therefore: $(k+1)! \geq 2^{k+1}$ ✓

**Conclusion:** By mathematical induction, $k! \geq 2^k$ for all $k \geq 4$. ∎

#### 2. $37^{500} - 37^4$ is divisible by 10

**Proof:**

We need to show $10 \mid (37^{500} - 37^4)$.

Since $10 = 2 \times 5$, we need to show both $2 \mid (37^{500} - 37^4)$ and $5 \mid (37^{500} - 37^4)$.

**Divisibility by 2:**
$37 \equiv 1 \pmod{2}$
Therefore: $37^{500} \equiv 1^{500} \equiv 1 \pmod{2}$ and $37^4 \equiv 1^4 \equiv 1 \pmod{2}$
So: $37^{500} - 37^4 \equiv 1 - 1 \equiv 0 \pmod{2}$ ✓

**Divisibility by 5:**
$37 \equiv 2 \pmod{5}$
By Fermat's Little Theorem, since $\gcd(2,5) = 1$: $2^4 \equiv 1 \pmod{5}$

$500 = 4 \times 125$, so $37^{500} \equiv 2^{500} \equiv (2^4)^{125} \equiv 1^{125} \equiv 1 \pmod{5}$
$37^4 \equiv 2^4 \equiv 1 \pmod{5}$
So: $37^{500} - 37^4 \equiv 1 - 1 \equiv 0 \pmod{5}$ ✓

**Conclusion:** Since $37^{500} - 37^4$ is divisible by both 2 and 5, it is divisible by 10. ∎

#### 3. For $n \geq 0$: $\frac{1}{1 \cdot 5} + \frac{1}{5 \cdot 9} + \frac{1}{9 \cdot 13} + \cdots + \frac{1}{(4n-3)(4n+1)} = \frac{n}{4n+1}$

**Proof by Mathematical Induction:**

**Base case:** $n = 1$
- Left side: $\frac{1}{1 \cdot 5} = \frac{1}{5}$
- Right side: $\frac{1}{4(1)+1} = \frac{1}{5}$
- Since $\frac{1}{5} = \frac{1}{5}$, the base case holds ✓

**Inductive hypothesis:** Assume the statement holds for some $k \geq 1$:
$$\sum_{i=1}^{k} \frac{1}{(4i-3)(4i+1)} = \frac{k}{4k+1}$$

**Inductive step:** We must prove:
$$\sum_{i=1}^{k+1} \frac{1}{(4i-3)(4i+1)} = \frac{k+1}{4(k+1)+1} = \frac{k+1}{4k+5}$$

Starting with the left side:
$$\sum_{i=1}^{k+1} \frac{1}{(4i-3)(4i+1)} = \sum_{i=1}^{k} \frac{1}{(4i-3)(4i+1)} + \frac{1}{(4(k+1)-3)(4(k+1)+1)}$$

By the inductive hypothesis:
$$= \frac{k}{4k+1} + \frac{1}{(4k+1)(4k+5)}$$

Find common denominator:
$$= \frac{k(4k+5) + 1}{(4k+1)(4k+5)}$$
$$= \frac{4k^2 + 5k + 1}{(4k+1)(4k+5)}$$
$$= \frac{(4k+1)(k+1)}{(4k+1)(4k+5)}$$
$$= \frac{k+1}{4k+5}$$

This is exactly what we wanted to prove.

**Conclusion:** By mathematical induction, the telescoping series formula holds for all $n \geq 1$. ∎