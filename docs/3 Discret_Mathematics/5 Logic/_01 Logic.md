# Logic

## Task 1

Let $p$, $q$, and $r$ be the following statements:
- $p$: "It is raining."
- $q$: "The sun is shining."
- $r$: "There are clouds in the sky."

Write the following statements using logical symbols:

### 1. It is raining, and the sun is shining.
$p \land q$

### 2. If it is raining, then there are clouds in the sky.
$p \rightarrow r$

### 3. If it is not raining, then the sun is not shining, and there are no clouds in the sky.
$\neg p \rightarrow (\neg q \land \neg r)$

### 4. The sun is shining if and only if it is not raining.
$q \leftrightarrow \neg p$

### 5. If there are no clouds in the sky, then the sun is shining.
$\neg r \rightarrow q$

## Task 2

Translate the following logical expressions into plain English:

### 1. $p \land q \rightarrow r$
"If it is raining and the sun is shining, then there are clouds in the sky."

### 2. $\neg p \rightarrow q \lor r$
"If it is not raining, then the sun is shining or there are clouds in the sky."

### 3. $\neg (p \lor q \lor r)$
"It is not raining, the sun is not shining, and there are no clouds in the sky."

### 4. $(p \rightarrow r) \rightarrow q$
"If (it is raining implies there are clouds in the sky), then the sun is shining."

## Task 3

Truth values depend on the actual weather conditions. Since these are weather-related statements, we can construct truth tables for all possible combinations:

**Truth Table for Task 1:**

| $p$ | $q$ | $r$ | $p \land q$ | $p \rightarrow r$ | $\neg p \rightarrow (\neg q \land \neg r)$ | $q \leftrightarrow \neg p$ | $\neg r \rightarrow q$ |
|-----|-----|-----|-------------|-------------------|---------------------------------------------|--------------------------|------------------------|
| T   | T   | T   | T           | T                 | T                                           | F                        | T                      |
| T   | T   | F   | T           | F                 | T                                           | F                        | T                      |
| T   | F   | T   | F           | T                 | T                                           | T                        | T                      |
| T   | F   | F   | F           | F                 | T                                           | T                        | F                      |
| F   | T   | T   | F           | T                 | F                                           | T                        | T                      |
| F   | T   | F   | F           | T                 | F                                           | T                        | T                      |
| F   | F   | T   | F           | T                 | F                                           | F                        | T                      |
| F   | F   | F   | F           | T                 | T                                           | F                        | F                      |

**Truth Table for Task 2:**

| $p$ | $q$ | $r$ | $p \land q \rightarrow r$ | $\neg p \rightarrow q \lor r$ | $\neg (p \lor q \lor r)$ | $(p \rightarrow r) \rightarrow q$ |
|-----|-----|-----|---------------------------|-------------------------------|--------------------------|-----------------------------------|
| T   | T   | T   | T                         | T                             | F                        | T                                 |
| T   | T   | F   | F                         | T                             | F                        | T                                 |
| T   | F   | T   | T                         | T                             | F                        | F                                 |
| T   | F   | F   | T                         | T                             | F                        | T                                 |
| F   | T   | T   | T                         | T                             | F                        | T                                 |
| F   | T   | F   | T                         | T                             | F                        | T                                 |
| F   | F   | T   | T                         | T                             | F                        | T                                 |
| F   | F   | F   | T                         | F                             | T                        | T                                 |

## Task 4

Determine which expressions are statements and provide their truth values:

### 1. $x^2 = 2 \quad \forall x \in \mathbb{R}$
**Statement:** Yes
**Truth value:** False
**Explanation:** This claims that $x^2 = 2$ for all real numbers $x$, which is false since $1^2 = 1 \neq 2$.

### 2. $x^2 = 2$ for some $x \in \mathbb{R}$
**Statement:** Yes
**Truth value:** True
**Explanation:** There exists $x = \pm\sqrt{2} \in \mathbb{R}$ such that $x^2 = 2$.

### 3. $x^2 = x$
**Statement:** No
**Truth value:** N/A
**Explanation:** This is an open sentence with free variable $x$. It's neither true nor false without specifying $x$.

### 4. $x^2 = x$ for exactly one $x \in \mathbb{R}$
**Statement:** Yes
**Truth value:** False
**Explanation:** The equation $x^2 = x$ has two solutions: $x = 0$ and $x = 1$, not exactly one.

### 5. $xy = z$ implies $y = z$ for all $x, y, z \in \mathbb{R}$
**Statement:** Yes
**Truth value:** False
**Explanation:** This is false. For example, if $x = 0$, $y = 1$, $z = 0$, then $xy = 0 = z$ but $y \neq z$.

## Task 5

Rewrite the ambiguous expression $x^2 = y^2$:

### 1. A precise statement whose logical value is true:
"For all real numbers $x$ and $y$, if $x = y$, then $x^2 = y^2$."
OR
"There exist real numbers $x$ and $y$ such that $x^2 = y^2$." (True, e.g., $x = 1, y = -1$)

### 2. A precise statement whose logical value is false:
"For all real numbers $x$ and $y$, $x^2 = y^2$ implies $x = y$."
**Explanation:** This is false because $(-1)^2 = 1^2$ but $-1 \neq 1$.

## Task 6

Provide the contrapositive of the following statements:

### 1. "If I am smart, then I am rich."
**Original:** $S \rightarrow R$
**Contrapositive:** "If I am not rich, then I am not smart." ($\neg R \rightarrow \neg S$)

### 2. "If $x^2 = x$, then $x = 0$ or $x = 1$."
**Original:** $x^2 = x \rightarrow (x = 0 \lor x = 1)$
**Contrapositive:** "If $x \neq 0$ and $x \neq 1$, then $x^2 \neq x$." ($\neg(x = 0 \lor x = 1) \rightarrow x^2 \neq x$)

### 3. "If $2 + 2 = 4$, then $2 + 4 = 8$."
**Original:** $(2 + 2 = 4) \rightarrow (2 + 4 = 8)$
**Contrapositive:** "If $2 + 4 \neq 8$, then $2 + 2 \neq 4$." ($2 + 4 \neq 8 \rightarrow 2 + 2 \neq 4$)

## Task 7

Verify Goldbach's conjecture for small numbers:

**Goldbach's Conjecture:** Every even integer greater than 2 can be expressed as the sum of two primes.

### For 6:
$6 = 3 + 3$ (both 3 is prime)
**Verified:** ✓

### For 8:
$8 = 3 + 5$ (both 3 and 5 are prime)
**Verified:** ✓

### For 10:
$10 = 3 + 7$ (both 3 and 7 are prime)
OR $10 = 5 + 5$ (both 5 is prime)
**Verified:** ✓

### For 98:
We need to find primes $p$ and $q$ such that $p + q = 98$.

Checking systematically:
- $98 = 19 + 79$ (both 19 and 79 are prime)
- $98 = 31 + 67$ (both 31 and 67 are prime)
- $98 = 37 + 61$ (both 37 and 61 are prime)

**Verified:** ✓

All tested cases confirm Goldbach's conjecture.

