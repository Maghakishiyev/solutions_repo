# Calculus

## 18. Functions

### Problem 18.1
**Question:** Draw in a single Geogebra notebook the following functions:
- $f(x) = x^2$
- $g(x) = \sqrt{x}$
- $h(x) = \frac{1}{x}$
- $j(x) = \sin(x)$

Find value of all the above functions at $x = 2$.

**Solution:**
At $x = 2$:
- $f(2) = 2^2 = 4$
- $g(2) = \sqrt{2} \approx 1.414$
- $h(2) = \frac{1}{2} = 0.5$
- $j(2) = \sin(2) \approx 0.909$

**Answer:** $f(2) = 4$, $g(2) = \sqrt{2}$, $h(2) = 0.5$, $j(2) = \sin(2)$

### Problem 18.2
**Question:** Let $f(x) = 3x - 1$ and $g(x) = \sqrt{x}$. Find:
- $f(g(x))$
- $g(f(x))$
- $f(f(x))$
- $g(g(x))$

**Solution:**
- $f(g(x)) = f(\sqrt{x}) = 3\sqrt{x} - 1$
- $g(f(x)) = g(3x - 1) = \sqrt{3x - 1}$
- $f(f(x)) = f(3x - 1) = 3(3x - 1) - 1 = 9x - 3 - 1 = 9x - 4$
- $g(g(x)) = g(\sqrt{x}) = \sqrt{\sqrt{x}} = x^{1/4}$

**Answer:** 
- $f(g(x)) = 3\sqrt{x} - 1$
- $g(f(x)) = \sqrt{3x - 1}$
- $f(f(x)) = 9x - 4$
- $g(g(x)) = x^{1/4}$

### Problem 18.3
**Question:** Let $f(x) = e^x$ and $g(x) = \ln(x)$. Check: $f(g(x))$ and $g(f(x))$. What do you notice?

**Solution:**
- $f(g(x)) = f(\ln(x)) = e^{\ln(x)} = x$
- $g(f(x)) = g(e^x) = \ln(e^x) = x$

**Observation:** Both compositions equal $x$, which means $f$ and $g$ are inverse functions of each other.

**Answer:** $f(g(x)) = x$ and $g(f(x)) = x$. The functions are inverses.

### Problem 18.4
**Question:** We have function $f=\{(1,7), (2,9), (3,11)\}$. Give inverse function $f^{-1}$.

**Solution:**
To find the inverse function, we swap the input and output values of each ordered pair.

**Answer:** $f^{-1} = \{(7,1), (9,2), (11,3)\}$

### Problem 18.5
**Question:** We have function $f=\{(1,7), (2,7), (3,11)\}$. Give inverse function $f^{-1}$.

**Solution:**
This function is not one-to-one because both inputs 1 and 2 map to the same output 7. Since the function fails the horizontal line test, it does not have an inverse function.

**Answer:** $f^{-1}$ does not exist because $f$ is not one-to-one.

### Problem 18.6
**Question:** We have function $f(x)= x-1$. Give inverse function $f^{-1}$. Show both functions on the same Geogebra notebook.

**Solution:**
To find the inverse:
1. Let $y = x - 1$
2. Solve for $x$: $x = y + 1$
3. Swap variables: $y = x + 1$

Therefore, $f^{-1}(x) = x + 1$

**Verification:** 
- $f(f^{-1}(x)) = f(x + 1) = (x + 1) - 1 = x$ ✓
- $f^{-1}(f(x)) = f^{-1}(x - 1) = (x - 1) + 1 = x$ ✓

**Answer:** $f^{-1}(x) = x + 1$

## 19. Limits of Sequences

### Problem 19.1
**Question:** Calculate:
- $\displaystyle \lim_{n \to \infty} \frac{n^2 + 3n}{2 n^2 - 2n}$
- $\displaystyle \lim_{n \to \infty} \frac{(2n+3)^3}{n^3-1}$

**Solution:**
**Part 1:** $\displaystyle \lim_{n \to \infty} \frac{n^2 + 3n}{2 n^2 - 2n}$

Divide numerator and denominator by $n^2$:
$$\lim_{n \to \infty} \frac{1 + \frac{3}{n}}{2 - \frac{2}{n}} = \frac{1 + 0}{2 - 0} = \frac{1}{2}$$

**Part 2:** $\displaystyle \lim_{n \to \infty} \frac{(2n+3)^3}{n^3-1}$

Expand $(2n+3)^3 = 8n^3 + 36n^2 + 54n + 27$:
$$\lim_{n \to \infty} \frac{8n^3 + 36n^2 + 54n + 27}{n^3-1}$$

Divide by $n^3$:
$$\lim_{n \to \infty} \frac{8 + \frac{36}{n} + \frac{54}{n^2} + \frac{27}{n^3}}{1 - \frac{1}{n^3}} = \frac{8 + 0 + 0 + 0}{1 - 0} = 8$$

**Answer:** $\frac{1}{2}$ and $8$

### Problem 19.2
**Question:** Prove using the squeeze theorem: $\displaystyle\lim_{n \to \infty} \frac{\sin(n)}{n}$

**Solution:**
We know that $-1 \leq \sin(n) \leq 1$ for all $n$.

Dividing by $n > 0$:
$$-\frac{1}{n} \leq \frac{\sin(n)}{n} \leq \frac{1}{n}$$

Since $\lim_{n \to \infty} \left(-\frac{1}{n}\right) = 0$ and $\lim_{n \to \infty} \frac{1}{n} = 0$,

by the squeeze theorem: $\displaystyle\lim_{n \to \infty} \frac{\sin(n)}{n} = 0$

**Answer:** $0$

### Problem 19.3
**Question:** Find the limit of the sequence: $a_n = (1+\frac{1}{n})^n$

**Solution:**
This is the definition of the mathematical constant $e$.

$$\lim_{n \to \infty} \left(1+\frac{1}{n}\right)^n = e \approx 2.71828$$

**Answer:** $e$

## 20. Limits of Real Functions

### Problem 20.1
**Question:** Compute: $\displaystyle\lim_{x \to \infty} \frac{x^3 + 2x^2}{x^4 - 3x^3}$

**Solution:**
Divide numerator and denominator by $x^4$:
$$\lim_{x \to \infty} \frac{\frac{1}{x} + \frac{2}{x^2}}{1 - \frac{3}{x}} = \frac{0 + 0}{1 - 0} = 0$$

**Answer:** $0$

### Problem 20.2
**Question:** Find: $\displaystyle \lim_{x \to 0} \frac{\sin(3x)}{2x+1}$

**Solution:**
Direct substitution:
$$\lim_{x \to 0} \frac{\sin(3x)}{2x+1} = \frac{\sin(0)}{2(0)+1} = \frac{0}{1} = 0$$

**Answer:** $0$

### Problem 20.3
**Question:** Find the asymptotes of the functions:
- $f(x) = \frac{x^2 - 1}{x^2 + 1}$
- $g(x) = \frac{\sin(x)}{x^2+1}$

**Solution:**
**For $f(x) = \frac{x^2 - 1}{x^2 + 1}$:**

*Vertical asymptotes:* None (denominator never equals zero)

*Horizontal asymptotes:*
$$\lim_{x \to \pm\infty} \frac{x^2 - 1}{x^2 + 1} = \lim_{x \to \pm\infty} \frac{1 - \frac{1}{x^2}}{1 + \frac{1}{x^2}} = \frac{1-0}{1+0} = 1$$

So $y = 1$ is a horizontal asymptote.

**For $g(x) = \frac{\sin(x)}{x^2+1}$:**

*Vertical asymptotes:* None (denominator never equals zero)

*Horizontal asymptotes:*
Since $-1 \leq \sin(x) \leq 1$:
$$\lim_{x \to \pm\infty} \frac{\sin(x)}{x^2+1} = 0$$

So $y = 0$ is a horizontal asymptote.

**Answer:** 
- $f(x)$: horizontal asymptote $y = 1$
- $g(x)$: horizontal asymptote $y = 0$

## 21. Derivatives

### Problem 21.1
**Question:** Compute derivatives of functions:

**Solution:**
- $\frac{d}{dx}(-3x+3) = -3$
- $\frac{d}{dx}(\pi x + \sin(1)) = \pi$ (since $\sin(1)$ is constant)
- $\frac{d}{dx}(4+\sin(2)) = 0$ (constant function)
- $\frac{d}{dx}(2x^3 - 3x^2 + 8x - 9) = 6x^2 - 6x + 8$
- $\frac{d}{dx}(6 x^{1/3}) = 6 \cdot \frac{1}{3}x^{-2/3} = 2x^{-2/3}$
- $\frac{d}{dx}(\sqrt{x}) = \frac{d}{dx}(x^{1/2}) = \frac{1}{2}x^{-1/2} = \frac{1}{2\sqrt{x}}$
- $\frac{d}{dx}(\cos(x) + \sin(x)) = -\sin(x) + \cos(x)$
- $\frac{d}{dx}(2\sin(x) \cos(x)) = \frac{d}{dx}(\sin(2x)) = 2\cos(2x)$
- $\frac{d}{dx}(x\sin(x)) = \sin(x) + x\cos(x)$ (product rule)
- $\frac{d}{dx}((x+1)(x+1)) = \frac{d}{dx}((x+1)^2) = 2(x+1)$
- $\frac{d}{dx}\left(\frac{x}{x+1}\right) = \frac{(x+1) \cdot 1 - x \cdot 1}{(x+1)^2} = \frac{1}{(x+1)^2}$ (quotient rule)
- $\frac{d}{dx}((x+1)e^x) = e^x + (x+1)e^x = e^x(x+2)$ (product rule)
- $\frac{d}{dx}(\sin(x^2)) = \cos(x^2) \cdot 2x = 2x\cos(x^2)$ (chain rule)
- $\frac{d}{dx}(e^{-2x}) = e^{-2x} \cdot (-2) = -2e^{-2x}$ (chain rule)
- $\frac{d}{dx}\left(\frac{1}{\sin(x+1)}\right) = -\frac{\cos(x+1)}{\sin^2(x+1)}$ (chain rule)
- $\frac{d}{dx}(\sqrt{2x+1}) = \frac{1}{2\sqrt{2x+1}} \cdot 2 = \frac{1}{\sqrt{2x+1}}$ (chain rule)

### Problem 21.2
**Question:** Prove $\frac{d}{dx} (\ln(\sin(x))) = \cot(x)$

**Solution:**
Using the chain rule:
$$\frac{d}{dx}(\ln(\sin(x))) = \frac{1}{\sin(x)} \cdot \frac{d}{dx}(\sin(x)) = \frac{1}{\sin(x)} \cdot \cos(x) = \frac{\cos(x)}{\sin(x)} = \cot(x)$$

**Answer:** Proven ✓

### Problem 21.3
**Question:** For $f(x) = \cos(x)$, verify that $f''(x) = -f(x)$.

**Solution:**
$$f(x) = \cos(x)$$
$$f'(x) = -\sin(x)$$
$$f''(x) = -\cos(x) = -f(x)$$

**Answer:** Verified ✓

### Problem 21.4
**Question:** Using de l'Hospital's Rule, find the improper limits:

**Solution:**
**Part 1:** $\displaystyle \lim_{x\to 0} \frac{\sin{x}}{x}$ (form $\frac{0}{0}$)

$$\lim_{x\to 0} \frac{\sin{x}}{x} = \lim_{x\to 0} \frac{\cos{x}}{1} = \frac{\cos(0)}{1} = 1$$

**Part 2:** $\displaystyle \lim_{x\to \infty} \frac{\ln x}{x}$ (form $\frac{\infty}{\infty}$)

$$\lim_{x\to \infty} \frac{\ln x}{x} = \lim_{x\to \infty} \frac{\frac{1}{x}}{1} = \lim_{x\to \infty} \frac{1}{x} = 0$$

**Part 3:** $\displaystyle \lim_{x\to \infty} \frac{e^x}{x}$ (form $\frac{\infty}{\infty}$)

$$\lim_{x\to \infty} \frac{e^x}{x} = \lim_{x\to \infty} \frac{e^x}{1} = \infty$$

**Answer:** $1$, $0$, $\infty$

### Problem 21.5
**Question:** In physics, the position of a particle is given by $x(t) = 3t^2 - 6t + 1$. Find the velocity $V(t)=x'(t)$ and acceleration $a(t)=V'(t)=x''(t)$ of the particle at time $t = 2$.

**Solution:**
$$x(t) = 3t^2 - 6t + 1$$
$$V(t) = x'(t) = 6t - 6$$
$$a(t) = V'(t) = x''(t) = 6$$

At $t = 2$:
- $V(2) = 6(2) - 6 = 6$
- $a(2) = 6$

**Answer:** $V(2) = 6$, $a(2) = 6$

## 22. Extremum

### Problem 22.1
**Question:** The profit function is $P(u) = -2u^2 + 50u - 300$, where $u$ is the number of units sold. Find the number of units that maximize profit.

**Solution:**
To find the maximum, take the derivative and set it equal to zero:
$$P'(u) = -4u + 50 = 0$$
$$u = \frac{50}{4} = 12.5$$

Since $P''(u) = -4 < 0$, this is indeed a maximum.

**Answer:** 12.5 units maximize profit.

### Problem 22.2
**Question:** You have 10 meters of string, and you need to use it to enclose the largest possible rectangle. Find the dimensions of the rectangle.

**Solution:**
Let the rectangle have length $l$ and width $w$.

Constraint: $2l + 2w = 10$, so $l + w = 5$, giving us $w = 5 - l$

Area to maximize: $A = lw = l(5-l) = 5l - l^2$

Taking the derivative: $A'(l) = 5 - 2l = 0$

Solving: $l = 2.5$ and $w = 5 - 2.5 = 2.5$

**Answer:** The rectangle should be a square with dimensions $2.5 \times 2.5$ meters.

### Problem 22.3
**Question:** Find extremum of $f(x) = x^2 + 3x - 5$.

**Solution:**
$$f'(x) = 2x + 3 = 0$$
$$x = -\frac{3}{2}$$

Since $f''(x) = 2 > 0$, this is a minimum.

$$f\left(-\frac{3}{2}\right) = \left(-\frac{3}{2}\right)^2 + 3\left(-\frac{3}{2}\right) - 5 = \frac{9}{4} - \frac{9}{2} - 5 = -\frac{29}{4}$$

**Answer:** Minimum at $x = -\frac{3}{2}$ with value $f\left(-\frac{3}{2}\right) = -\frac{29}{4}$

### Problem 22.4
**Question:** Find extremum of $f(x) =\frac{x^2+2x+1}{x-1}$.

**Solution:**
Note that $x^2 + 2x + 1 = (x+1)^2$, so $f(x) = \frac{(x+1)^2}{x-1}$

Using the quotient rule:
$$f'(x) = \frac{2(x+1)(x-1) - (x+1)^2 \cdot 1}{(x-1)^2} = \frac{(x+1)[2(x-1) - (x+1)]}{(x-1)^2} = \frac{(x+1)(x-3)}{(x-1)^2}$$

Setting $f'(x) = 0$: $(x+1)(x-3) = 0$

Critical points: $x = -1$ and $x = 3$

Evaluating:
- $f(-1) = \frac{0}{-2} = 0$ (minimum)
- $f(3) = \frac{16}{2} = 8$ (maximum)

**Answer:** Minimum at $x = -1$ with value $0$; maximum at $x = 3$ with value $8$.

## 23. Taylor Series

### Problem 23.1
**Question:** Find the Taylor series and visualize obtained functions in Geogebra:

**Solution:**
**For $f(x) = \cos(x)$ around $x = 0$ up to 4th degree:**

$$\cos(x) = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} + O(x^6) = 1 - \frac{x^2}{2} + \frac{x^4}{24}$$

**For $h(x) = \frac{1}{1-x}$ around $x = 0$ up to 3rd degree:**

$$\frac{1}{1-x} = 1 + x + x^2 + x^3 + O(x^4)$$

**For $g(x) = \sin(x)$ around $x = \pi$ up to 3rd degree:**

First, find derivatives at $x = \pi$:
- $g(\pi) = \sin(\pi) = 0$
- $g'(\pi) = \cos(\pi) = -1$
- $g''(\pi) = -\sin(\pi) = 0$
- $g'''(\pi) = -\cos(\pi) = 1$

$$\sin(x) = 0 - 1(x-\pi) + 0 + \frac{1}{6}(x-\pi)^3 = -(x-\pi) + \frac{(x-\pi)^3}{6}$$

**Answer:**
- $\cos(x) \approx 1 - \frac{x^2}{2} + \frac{x^4}{24}$
- $\frac{1}{1-x} \approx 1 + x + x^2 + x^3$
- $\sin(x) \approx -(x-\pi) + \frac{(x-\pi)^3}{6}$

### Problem 23.2
**Question:** Find a tangent line $y = f'(x_0) (x-x_0) + f(x_0)$ to the function $f(x) = e^{\sin(x)}$ at $x_0 = \pi$.

**Solution:**
$$f(x) = e^{\sin(x)}$$
$$f'(x) = e^{\sin(x)} \cos(x)$$

At $x_0 = \pi$:
- $f(\pi) = e^{\sin(\pi)} = e^0 = 1$
- $f'(\pi) = e^{\sin(\pi)} \cos(\pi) = e^0 \cdot (-1) = -1$

Tangent line: $y = -1(x - \pi) + 1 = -x + \pi + 1$

**Answer:** $y = -x + \pi + 1$

## 24. Integrals

### Problem 24.1
**Question:** Compute indefinite integrals:

**Solution:**
- $\int 1 \, dx = x + C$
- $\int (x^2 +2) \, dx = \frac{x^3}{3} + 2x + C$
- $\int 2\sin(x) \, dx = -2\cos(x) + C$
- $\int \frac{3}{x} \, dx = 3\ln|x| + C$
- $\int \frac{1}{x^2} \, dx = \int x^{-2} \, dx = -x^{-1} + C = -\frac{1}{x} + C$
- $\int \left( \frac{1}{3}x^4 - 5 \right) \, dx = \frac{x^5}{15} - 5x + C$
- $\int (\sin^2 x + \cos^2 x) \, dx = \int 1 \, dx = x + C$
- $\int (5 \sin x + 3e^x) \, dx = -5\cos x + 3e^x + C$
- $\int \sqrt[3]{x} \, dx = \int x^{1/3} \, dx = \frac{3x^{4/3}}{4} + C$
- $\int \sqrt{10x} \, dx = \sqrt{10} \int x^{1/2} \, dx = \sqrt{10} \cdot \frac{2x^{3/2}}{3} + C = \frac{2\sqrt{10x^3}}{3} + C$
- $\int \cos\left(\frac{5}{2}x + 3\right) \, dx = \frac{2}{5}\sin\left(\frac{5}{2}x + 3\right) + C$
- $\int \frac{\cos(\ln(x))}{x} \, dx = \sin(\ln(x)) + C$ (substitution $u = \ln(x)$)
- $\int x \ln(x) \, dx = \frac{x^2\ln(x)}{2} - \frac{x^2}{4} + C$ (integration by parts)
- $\int x e^x \, dx = xe^x - e^x + C = e^x(x-1) + C$ (integration by parts)

### Problem 24.2
**Question:** Calculate integrals over the interval $[0, \pi]$ and visualize them in Geogebra:

**Solution:**
**For $f(x)=2x+1$:**
$$\int_0^\pi (2x+1) \, dx = \left[x^2 + x\right]_0^\pi = \pi^2 + \pi - 0 = \pi^2 + \pi$$

**For $g(x)=x^2$:**
$$\int_0^\pi x^2 \, dx = \left[\frac{x^3}{3}\right]_0^\pi = \frac{\pi^3}{3}$$

**Answer:** $\pi^2 + \pi$ and $\frac{\pi^3}{3}$

### Problem 24.3
**Question:** Calculate the area of the region bounded by the lines: $x = 1$, $x = 2$, $y = 0$, and $y = x^2 + 1$.

**Solution:**
$$\text{Area} = \int_1^2 (x^2 + 1) \, dx = \left[\frac{x^3}{3} + x\right]_1^2 = \left(\frac{8}{3} + 2\right) - \left(\frac{1}{3} + 1\right) = \frac{7}{3} + 1 = \frac{10}{3}$$

**Answer:** $\frac{10}{3}$ square units

### Problem 24.4
**Question:** Calculate the area under the sine curve over the interval $[0, \pi]$:

**Solution:**
$$P = \int_0^\pi \sin(x) \, dx = [-\cos(x)]_0^\pi = -\cos(\pi) - (-\cos(0)) = -(-1) - (-1) = 2$$

**Answer:** $2$ square units

### Problem 24.5
**Question:** Calculate the length of the sine curve over the interval $[0, \pi]$:

**Solution:**
$$L = \int_0^\pi \sqrt{1 + \cos^2(x)} \, dx$$

This integral does not have a closed-form solution in terms of elementary functions. It must be evaluated numerically.

$$L \approx 3.82$$

**Answer:** $L = \int_0^\pi \sqrt{1 + \cos^2(x)} \, dx \approx 3.82$

### Problem 24.6
**Question:** Find the distance of the moving particle between time $t=0$ and $t=2$ for the position function: $x(t) = 3t^2 - 6t + 1$.

**Solution:**
Distance is the integral of speed (absolute value of velocity):
$$v(t) = x'(t) = 6t - 6$$

$v(t) = 0$ when $t = 1$

For $t \in [0,1]$: $v(t) < 0$, so $|v(t)| = 6 - 6t$
For $t \in [1,2]$: $v(t) > 0$, so $|v(t)| = 6t - 6$

$$\text{Distance} = \int_0^1 (6 - 6t) \, dt + \int_1^2 (6t - 6) \, dt$$
$$= \left[6t - 3t^2\right]_0^1 + \left[3t^2 - 6t\right]_1^2$$
$$= (6 - 3) - 0 + (12 - 12) - (3 - 6) = 3 + 3 = 6$$

**Answer:** 6 units

## 25. Differential Equations

### Problem 25.1
**Question:** Solve the following first-order ordinary differential equations:

**Solution:**
**Part 1:** $y'(x)= y$

This is a separable equation:
$$\frac{dy}{dx} = y \Rightarrow \frac{dy}{y} = dx$$
$$\int \frac{dy}{y} = \int dx \Rightarrow \ln|y| = x + C$$
$$y = Ae^x$$ where $A = e^C$

**Part 2:** $y'(x) = \frac{1}{2y(x)}$

Separating variables:
$$\frac{dy}{dx} = \frac{1}{2y} \Rightarrow 2y \, dy = dx$$
$$\int 2y \, dy = \int dx \Rightarrow y^2 = x + C$$
$$y = \pm\sqrt{x + C}$$

**Answer:** $y = Ae^x$ and $y = \pm\sqrt{x + C}$

### Problem 25.2
**Question:** Solve using separation of variables:

**Solution:**
**Part 1:** $\frac{dy}{dx} = \frac{x}{y}$

$$y \, dy = x \, dx$$
$$\int y \, dy = \int x \, dx$$
$$\frac{y^2}{2} = \frac{x^2}{2} + C$$
$$y^2 = x^2 + 2C$$
$$y = \pm\sqrt{x^2 + K}$$ where $K = 2C$

**Part 2:** $\frac{dy}{dx} = \frac{y}{x}$

$$\frac{dy}{y} = \frac{dx}{x}$$
$$\int \frac{dy}{y} = \int \frac{dx}{x}$$
$$\ln|y| = \ln|x| + C$$
$$y = Ax$$ where $A = e^C$

**Part 3:** $\frac{dy}{dx} = xy$

$$\frac{dy}{y} = x \, dx$$
$$\int \frac{dy}{y} = \int x \, dx$$
$$\ln|y| = \frac{x^2}{2} + C$$
$$y = Ae^{x^2/2}$$ where $A = e^C$

**Answer:** $y = \pm\sqrt{x^2 + K}$, $y = Ax$, $y = Ae^{x^2/2}$

### Problem 25.3
**Question:** Solve the second-order ordinary differential equations:

**Solution:**
**Part 1:** $y''(x) + y'(x) = 0$ with $y(0) = 2$, $y'(0) = -1$

Characteristic equation: $r^2 + r = 0 \Rightarrow r(r+1) = 0$
Roots: $r = 0, -1$

General solution: $y = C_1 + C_2 e^{-x}$

Using initial conditions:
- $y(0) = C_1 + C_2 = 2$
- $y'(x) = -C_2 e^{-x}$, so $y'(0) = -C_2 = -1 \Rightarrow C_2 = 1$
- Therefore $C_1 = 1$

**Solution:** $y = 1 + e^{-x}$

**Part 2:** $y''(x) - y(x)= 0$ with $y(0) = 2$, $y'(0) = 0$

Characteristic equation: $r^2 - 1 = 0 \Rightarrow r = \pm 1$

General solution: $y = C_1 e^x + C_2 e^{-x}$

Using initial conditions:
- $y(0) = C_1 + C_2 = 2$
- $y'(x) = C_1 e^x - C_2 e^{-x}$, so $y'(0) = C_1 - C_2 = 0 \Rightarrow C_1 = C_2$
- Therefore $C_1 = C_2 = 1$

**Solution:** $y = e^x + e^{-x} = 2\cosh(x)$

**Part 3:** $\frac{d^2\,y(x)}{dx^2} = -\omega^2 y(x)$

Characteristic equation: $r^2 + \omega^2 = 0 \Rightarrow r = \pm i\omega$

**General solution:** $y = C_1 \cos(\omega x) + C_2 \sin(\omega x)$

**Answer:** $y = 1 + e^{-x}$, $y = 2\cosh(x)$, $y = C_1 \cos(\omega x) + C_2 \sin(\omega x)$

### Problem 25.4
**Question:** Check if $\psi(t, x) = A \cos(\omega t + kx)$ is a solution of the wave equation:

**Solution:**
Given: $\psi(t, x) = A \cos(\omega t + kx)$ and $v = \frac{\omega}{k}$

Compute partial derivatives:
$$\frac{\partial \psi}{\partial t} = -A\omega \sin(\omega t + kx)$$
$$\frac{\partial^2 \psi}{\partial t^2} = -A\omega^2 \cos(\omega t + kx)$$

$$\frac{\partial \psi}{\partial x} = -Ak \sin(\omega t + kx)$$
$$\frac{\partial^2 \psi}{\partial x^2} = -Ak^2 \cos(\omega t + kx)$$

Substitute into the wave equation:
$$\frac{\partial^2 \psi}{\partial t^2} - v^2 \frac{\partial^2 \psi}{\partial x^2} = -A\omega^2 \cos(\omega t + kx) - v^2(-Ak^2 \cos(\omega t + kx))$$
$$= -A\omega^2 \cos(\omega t + kx) + v^2 Ak^2 \cos(\omega t + kx)$$
$$= A\cos(\omega t + kx)(-\omega^2 + v^2 k^2)$$

Since $v = \frac{\omega}{k}$, we have $v^2 = \frac{\omega^2}{k^2}$, so $v^2 k^2 = \omega^2$

Therefore: $-\omega^2 + v^2 k^2 = -\omega^2 + \omega^2 = 0$

**Answer:** Yes, $\psi(t, x) = A \cos(\omega t + kx)$ is a solution of the wave equation.