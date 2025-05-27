# Analytic Geometry

## 11. Vectors I

### Problem 11.1
**Question:** By what number should vector $\mathbf{a} = [3, 4]$ be multiplied so that its length is equal to 1?

**Solution:**
The length of vector $\mathbf{a} = [3, 4]$ is:
$$|\mathbf{a}| = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5$$

To make the length equal to 1, we need to multiply by:
$$k = \frac{1}{|\mathbf{a}|} = \frac{1}{5}$$

**Answer:** The vector should be multiplied by $\frac{1}{5}$.

### Problem 11.2
**Question:** Calculate the length of vector $\mathbf{b} = [1, 1]$ and find the unit vector of this vector.

**Solution:**
The length of vector $\mathbf{b} = [1, 1]$ is:
$$|\mathbf{b}| = \sqrt{1^2 + 1^2} = \sqrt{2}$$

The unit vector is:
$$\hat{\mathbf{b}} = \frac{\mathbf{b}}{|\mathbf{b}|} = \frac{[1, 1]}{\sqrt{2}} = \left[\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}\right] = \left[\frac{\sqrt{2}}{2}, \frac{\sqrt{2}}{2}\right]$$

**Answer:** Length = $\sqrt{2}$, Unit vector = $\left[\frac{\sqrt{2}}{2}, \frac{\sqrt{2}}{2}\right]$

### Problem 11.3
**Question:** Plot the vector and the unit vector from the previous exercise.

**Solution:**
Both vectors have the same direction but different magnitudes:
- Original vector $\mathbf{b} = [1, 1]$ has length $\sqrt{2} \approx 1.414$
- Unit vector $\hat{\mathbf{b}} = \left[\frac{\sqrt{2}}{2}, \frac{\sqrt{2}}{2}\right]$ has length 1

Both vectors make a 45° angle with the x-axis.

### Problem 11.4
**Question:** Calculate the length of vector $\mathbf{c} = [1, 2, 3]$ and find the unit vector of this vector.

**Solution:**
The length of vector $\mathbf{c} = [1, 2, 3]$ is:
$$|\mathbf{c}| = \sqrt{1^2 + 2^2 + 3^2} = \sqrt{1 + 4 + 9} = \sqrt{14}$$

The unit vector is:
$$\hat{\mathbf{c}} = \frac{\mathbf{c}}{|\mathbf{c}|} = \frac{[1, 2, 3]}{\sqrt{14}} = \left[\frac{1}{\sqrt{14}}, \frac{2}{\sqrt{14}}, \frac{3}{\sqrt{14}}\right]$$

**Answer:** Length = $\sqrt{14}$, Unit vector = $\left[\frac{1}{\sqrt{14}}, \frac{2}{\sqrt{14}}, \frac{3}{\sqrt{14}}\right]$

### Problem 11.5
**Question:** Find the Cartesian coordinates of vector $\mathbf{v} = [2, 3, 4]$ in the basis $\{\mathbf{b_1} = [1, 0, 1], \mathbf{b_2} = [0, 1, 0], \mathbf{b_3} = [1, 0, -1]\}$.

**Solution:**
We need to find coefficients $x$, $y$, $z$ such that:
$$\mathbf{v} = x\mathbf{b_1} + y\mathbf{b_2} + z\mathbf{b_3}$$
$$[2, 3, 4] = x[1, 0, 1] + y[0, 1, 0] + z[1, 0, -1]$$
$$[2, 3, 4] = [x + z, y, x - z]$$

This gives us the system:
- $x + z = 2$
- $y = 3$
- $x - z = 4$

From equations 1 and 3: $2x = 6$, so $x = 3$
From equation 1: $z = 2 - 3 = -1$

**Answer:** The coordinates in the new basis are $[3, 3, -1]$.

## 12. Vectors II

### Problem 12.1
**Question:** Perform the addition of vector $[2, 1]$ to vector $[-1, 1]$. Plot both vectors and their sum on a graph.

**Solution:**
Vector addition:
$$\mathbf{a} + \mathbf{b} = [2, 1] + [-1, 1] = [2 + (-1), 1 + 1] = [1, 2]$$

**Answer:** The sum is $[1, 2]$.

### Problem 12.2
**Question:** Calculate the area of the triangle spanned by vectors $[2, 1, 2]$ and $[-1, 1, 1]$.

**Solution:**
The area of a triangle spanned by two vectors is half the magnitude of their cross product:
$$\mathbf{a} \times \mathbf{b} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 2 & 1 & 2 \\ -1 & 1 & 1 \end{vmatrix}$$

$$= \mathbf{i}(1 \cdot 1 - 2 \cdot 1) - \mathbf{j}(2 \cdot 1 - 2 \cdot (-1)) + \mathbf{k}(2 \cdot 1 - 1 \cdot (-1))$$
$$= \mathbf{i}(1 - 2) - \mathbf{j}(2 + 2) + \mathbf{k}(2 + 1)$$
$$= [-1, -4, 3]$$

$$|\mathbf{a} \times \mathbf{b}| = \sqrt{(-1)^2 + (-4)^2 + 3^2} = \sqrt{1 + 16 + 9} = \sqrt{26}$$

Area = $\frac{1}{2}|\mathbf{a} \times \mathbf{b}| = \frac{\sqrt{26}}{2}$

**Answer:** The area is $\frac{\sqrt{26}}{2}$.

### Problem 12.3
**Question:** Calculate the volume of the parallelepiped spanned by vectors $[2, 1, -1]$, $[-1, 1, 0]$, and $[1, 2, 1]$.

**Solution:**
The volume is the absolute value of the scalar triple product:
$$V = |\mathbf{a} \cdot (\mathbf{b} \times \mathbf{c})| = \begin{vmatrix} 2 & 1 & -1 \\ -1 & 1 & 0 \\ 1 & 2 & 1 \end{vmatrix}$$

Expanding along the third column:
$$= -1 \begin{vmatrix} -1 & 1 \\ 1 & 2 \end{vmatrix} - 0 + 1 \begin{vmatrix} 2 & 1 \\ -1 & 1 \end{vmatrix}$$
$$= -1(-1 \cdot 2 - 1 \cdot 1) + 1(2 \cdot 1 - 1 \cdot (-1))$$
$$= -1(-2 - 1) + 1(2 + 1)$$
$$= -1(-3) + 3 = 3 + 3 = 6$$

**Answer:** The volume is 6.

### Problem 12.4
**Question:** Check if vectors $[2, 1]$ and $[-1, 1]$ are perpendicular.

**Solution:**
Two vectors are perpendicular if their dot product equals zero:
$$\mathbf{a} \cdot \mathbf{b} = [2, 1] \cdot [-1, 1] = 2 \cdot (-1) + 1 \cdot 1 = -2 + 1 = -1$$

Since the dot product is $-1 \neq 0$, the vectors are not perpendicular.

**Answer:** No, the vectors are not perpendicular.

### Problem 12.5
**Question:** Calculate the angle in degrees between vectors $[4, 2, 1]$ and $[1, 3, 2]$.

**Solution:**
The angle between two vectors is given by:
$$\cos \theta = \frac{\mathbf{a} \cdot \mathbf{b}}{|\mathbf{a}||\mathbf{b}|}$$

$$\mathbf{a} \cdot \mathbf{b} = 4 \cdot 1 + 2 \cdot 3 + 1 \cdot 2 = 4 + 6 + 2 = 12$$
$$|\mathbf{a}| = \sqrt{4^2 + 2^2 + 1^2} = \sqrt{16 + 4 + 1} = \sqrt{21}$$
$$|\mathbf{b}| = \sqrt{1^2 + 3^2 + 2^2} = \sqrt{1 + 9 + 4} = \sqrt{14}$$

$$\cos \theta = \frac{12}{\sqrt{21}\sqrt{14}} = \frac{12}{\sqrt{294}} = \frac{12}{7\sqrt{6}} = \frac{12\sqrt{6}}{42} = \frac{2\sqrt{6}}{7}$$

$$\theta = \arccos\left(\frac{2\sqrt{6}}{7}\right) \approx 31.0°$$

**Answer:** The angle is approximately 31.0°.

### Problem 12.6
**Question:** For three-dimensional vectors: $\mathbf{a}=[a_x, a_y, a_z]$, $\mathbf{b}=[b_x, b_y, b_z]$, $\mathbf{c}=[c_x, c_y, c_z]$, prove that the following identity is satisfied:
$$\mathbf{a} \times (\mathbf{b} \times \mathbf{c}) = (\mathbf{a} \cdot \mathbf{c}) \mathbf{b} - (\mathbf{a} \cdot \mathbf{b}) \mathbf{c}$$

**Solution:**
This is the vector triple product identity. Let's prove it by expanding both sides.

First, let's compute $\mathbf{b} \times \mathbf{c}$:
$$\mathbf{b} \times \mathbf{c} = [b_y c_z - b_z c_y, b_z c_x - b_x c_z, b_x c_y - b_y c_x]$$

Now, $\mathbf{a} \times (\mathbf{b} \times \mathbf{c})$:
$$\mathbf{a} \times (\mathbf{b} \times \mathbf{c}) = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ a_x & a_y & a_z \\ b_y c_z - b_z c_y & b_z c_x - b_x c_z & b_x c_y - b_y c_x \end{vmatrix}$$

The x-component is:
$$a_y(b_x c_y - b_y c_x) - a_z(b_z c_x - b_x c_z) = a_y b_x c_y - a_y b_y c_x - a_z b_z c_x + a_z b_x c_z$$
$$= b_x(a_y c_y + a_z c_z) - c_x(a_y b_y + a_z b_z)$$
$$= b_x(\mathbf{a} \cdot \mathbf{c} - a_x c_x) - c_x(\mathbf{a} \cdot \mathbf{b} - a_x b_x)$$
$$= b_x(\mathbf{a} \cdot \mathbf{c}) - c_x(\mathbf{a} \cdot \mathbf{b}) + a_x(c_x b_x - b_x c_x) = b_x(\mathbf{a} \cdot \mathbf{c}) - c_x(\mathbf{a} \cdot \mathbf{b})$$

This is the x-component of $(\mathbf{a} \cdot \mathbf{c}) \mathbf{b} - (\mathbf{a} \cdot \mathbf{b}) \mathbf{c}$.

By similar calculations for y and z components, the identity is proven.

## 13. Vectors III

### Problem 13.1
**Question:** Divide the line segment connecting points $A(-1, 2)$ and $B(3, -2)$ in the ratio $1:3$. Illustrate the result on a graph.

**Solution:**
To divide a line segment in ratio $m:n$, the point $P$ is given by:
$$P = \frac{n \cdot A + m \cdot B}{m + n}$$

For ratio $1:3$:
$$P = \frac{3 \cdot A + 1 \cdot B}{1 + 3} = \frac{3(-1, 2) + 1(3, -2)}{4} = \frac{(-3, 6) + (3, -2)}{4} = \frac{(0, 4)}{4} = (0, 1)$$

**Answer:** The point dividing the segment in ratio $1:3$ is $(0, 1)$.

### Problem 13.2
**Question:** Project vector $\mathbf{a} = (3, 4)$ onto the $OX$ and $OY$ axes. Illustrate the result on a graph.

**Solution:**
The projection onto coordinate axes is simply the corresponding component:
- Projection onto $OX$ axis: $\text{proj}_{OX} \mathbf{a} = (3, 0)$
- Projection onto $OY$ axis: $\text{proj}_{OY} \mathbf{a} = (0, 4)$

**Answer:** Projection onto $OX$: $(3, 0)$, Projection onto $OY$: $(0, 4)$.

### Problem 13.3
**Question:** Project vector $\mathbf{a} = (2,3)$ onto vector $\mathbf{b} = (1, 1)$. Illustrate the result on a graph.

**Solution:**
The projection of $\mathbf{a}$ onto $\mathbf{b}$ is:
$$\text{proj}_{\mathbf{b}} \mathbf{a} = \frac{\mathbf{a} \cdot \mathbf{b}}{|\mathbf{b}|^2} \mathbf{b}$$

$$\mathbf{a} \cdot \mathbf{b} = 2 \cdot 1 + 3 \cdot 1 = 5$$
$$|\mathbf{b}|^2 = 1^2 + 1^2 = 2$$

$$\text{proj}_{\mathbf{b}} \mathbf{a} = \frac{5}{2}(1, 1) = \left(\frac{5}{2}, \frac{5}{2}\right)$$

**Answer:** The projection is $\left(\frac{5}{2}, \frac{5}{2}\right)$.

### Problem 13.4
**Question:** Project vector $\mathbf{b} = (1, 1)$ onto vector $\mathbf{a} = (2, 3)$. Illustrate the result on a graph.

**Solution:**
$$\text{proj}_{\mathbf{a}} \mathbf{b} = \frac{\mathbf{b} \cdot \mathbf{a}}{|\mathbf{a}|^2} \mathbf{a}$$

$$\mathbf{b} \cdot \mathbf{a} = 1 \cdot 2 + 1 \cdot 3 = 5$$
$$|\mathbf{a}|^2 = 2^2 + 3^2 = 13$$

$$\text{proj}_{\mathbf{a}} \mathbf{b} = \frac{5}{13}(2, 3) = \left(\frac{10}{13}, \frac{15}{13}\right)$$

**Answer:** The projection is $\left(\frac{10}{13}, \frac{15}{13}\right)$.

## 14. Equations of Lines on a Plane

### Problem 14.1
**Question:** The line passes through points $A(1, 2)$ and $B(3, 4)$. Find the equation of the line.

**Solution:**
The slope is: $m = \frac{4-2}{3-1} = \frac{2}{2} = 1$

Using point-slope form with point $A(1, 2)$:
$$y - 2 = 1(x - 1)$$
$$y = x + 1$$

**Answer:** $y = x + 1$

### Problem 14.2
**Question:** The line passes through point $A(1, 2)$ and is parallel to the line $y = 2x + 3$. Find the equation of the line.

**Solution:**
Parallel lines have the same slope. The slope of $y = 2x + 3$ is $m = 2$.

Using point-slope form:
$$y - 2 = 2(x - 1)$$
$$y = 2x$$

**Answer:** $y = 2x$

### Problem 14.3
**Question:** The line passes through point $A(1, 2)$ and is perpendicular to the line $y = 2x + 3$. Find the equation of the line.

**Solution:**
Perpendicular lines have slopes that are negative reciprocals. If $m_1 = 2$, then $m_2 = -\frac{1}{2}$.

Using point-slope form:
$$y - 2 = -\frac{1}{2}(x - 1)$$
$$y = -\frac{1}{2}x + \frac{1}{2} + 2 = -\frac{1}{2}x + \frac{5}{2}$$

**Answer:** $y = -\frac{1}{2}x + \frac{5}{2}$

### Problem 14.4
**Question:** We have two lines $y = 2x + 3$ and $y = 3x + 2$. Find the intersection point of these lines and calculate the angle between them.

**Solution:**
**Intersection point:**
Setting the equations equal:
$$2x + 3 = 3x + 2$$
$$x = 1$$
$$y = 2(1) + 3 = 5$$

Intersection point: $(1, 5)$

**Angle between lines:**
The angle between two lines with slopes $m_1$ and $m_2$ is:
$$\tan \theta = \left|\frac{m_1 - m_2}{1 + m_1 m_2}\right| = \left|\frac{2 - 3}{1 + 2 \cdot 3}\right| = \left|\frac{-1}{7}\right| = \frac{1}{7}$$

$$\theta = \arctan\left(\frac{1}{7}\right) \approx 8.13°$$

**Answer:** Intersection point: $(1, 5)$, Angle: $\arctan\left(\frac{1}{7}\right) \approx 8.13°$

### Problem 14.5
**Question:** Write the equation of the line passing through point $A(1, 2)$ and parallel to the vector $\mathbf{v} = [2, 3]$.

**Solution:**
The direction vector $\mathbf{v} = [2, 3]$ gives slope $m = \frac{3}{2}$.

Using point-slope form:
$$y - 2 = \frac{3}{2}(x - 1)$$
$$y = \frac{3}{2}x + \frac{1}{2}$$

**Answer:** $y = \frac{3}{2}x + \frac{1}{2}$

### Problem 14.6
**Question:** We have the line $y = 2x + 3$. Find an example of a line perpendicular and parallel to it.

**Solution:**
**Parallel line:** Has the same slope $m = 2$
Example: $y = 2x + 1$

**Perpendicular line:** Has slope $m = -\frac{1}{2}$
Example: $y = -\frac{1}{2}x + 1$

**Answer:** Parallel: $y = 2x + 1$, Perpendicular: $y = -\frac{1}{2}x + 1$

### Problem 14.7
**Question:** We have the line $y = 2x + 3$ and point $A(1, 2)$. Find the distance from point $A$ to the line.

**Solution:**
Rewrite the line in standard form: $2x - y + 3 = 0$

The distance from point $(x_0, y_0)$ to line $ax + by + c = 0$ is:
$$d = \frac{|ax_0 + by_0 + c|}{\sqrt{a^2 + b^2}}$$

$$d = \frac{|2(1) - 1(2) + 3|}{\sqrt{2^2 + (-1)^2}} = \frac{|2 - 2 + 3|}{\sqrt{5}} = \frac{3}{\sqrt{5}} = \frac{3\sqrt{5}}{5}$$

**Answer:** $\frac{3\sqrt{5}}{5}$

### Problem 14.8
**Question:** The line intersects the coordinate axes at points $A(2, 0)$ and $B(0, 3)$. Find the equation of the line.

**Solution:**
Using the intercept form: $\frac{x}{a} + \frac{y}{b} = 1$ where $a = 2$ and $b = 3$:

$$\frac{x}{2} + \frac{y}{3} = 1$$

Multiplying by 6:
$$3x + 2y = 6$$

In slope-intercept form:
$$y = -\frac{3}{2}x + 3$$

**Answer:** $y = -\frac{3}{2}x + 3$ or $3x + 2y = 6$

### Problem 14.9
**Question:** Calculate the angle between the line $y = x + 3$ and the $Ox$ axis.

**Solution:**
The slope of the line is $m = 1$.
The angle with the x-axis is: $\theta = \arctan(m) = \arctan(1) = 45°$

**Answer:** $45°$

### Problem 14.10
**Question:** Provide a vector perpendicular to the line $x + y + 1 = 0$.

**Solution:**
For a line $ax + by + c = 0$, the normal vector is $\mathbf{n} = [a, b]$.

For the line $x + y + 1 = 0$, the normal vector is $\mathbf{n} = [1, 1]$.

**Answer:** $[1, 1]$ (or any scalar multiple like $[2, 2]$, $[-1, -1]$, etc.)

## 15. Equations of Second-Order Curves (Conic Sections)

### Problem 15.1
**Question:** Find the equation of a circle with center at point $A(1,2)$ and radius $r=3$.

**Solution:**
The general equation of a circle with center $(h, k)$ and radius $r$ is:
$$(x - h)^2 + (y - k)^2 = r^2$$

With center $(1, 2)$ and radius $3$:
$$(x - 1)^2 + (y - 2)^2 = 9$$

**Answer:** $(x - 1)^2 + (y - 2)^2 = 9$

### Problem 15.2
**Question:** Find the equation of a parabola intersecting the $Ox$ axis at points $x=2$, $x=4$, and passing through point $y(3)=1$.

**Solution:**
Since the parabola intersects the x-axis at $x = 2$ and $x = 4$, it has the form:
$$y = a(x - 2)(x - 4)$$

Using the condition $y(3) = 1$:
$$1 = a(3 - 2)(3 - 4) = a(1)(-1) = -a$$
$$a = -1$$

Therefore: $y = -(x - 2)(x - 4) = -(x^2 - 6x + 8) = -x^2 + 6x - 8$

**Answer:** $y = -x^2 + 6x - 8$

### Problem 15.3
**Question:** Find the center of the ellipse with the equation $x^2 + 4y^2 - 4x - 16y + 16 = 0$.

**Solution:**
Complete the square for both $x$ and $y$ terms:
$$x^2 - 4x + 4y^2 - 16y + 16 = 0$$
$$(x^2 - 4x + 4) + 4(y^2 - 4y + 4) + 16 - 4 - 16 = 0$$
$$(x - 2)^2 + 4(y - 2)^2 = 4$$

Dividing by 4:
$$\frac{(x - 2)^2}{4} + \frac{(y - 2)^2}{1} = 1$$

**Answer:** The center is $(2, 2)$.

### Problem 15.4
**Question:** Find the slope ($m>0$) of the line $y=mx-5$ that is tangent to the circle with the equation $x^2 + y^2=1$.

**Solution:**
For the line to be tangent to the circle, the distance from the center $(0, 0)$ to the line must equal the radius.

Rewrite the line as $mx - y - 5 = 0$.
Distance from origin to line: $d = \frac{|m(0) - 1(0) - 5|}{\sqrt{m^2 + 1}} = \frac{5}{\sqrt{m^2 + 1}}$

For tangency: $d = r = 1$
$$\frac{5}{\sqrt{m^2 + 1}} = 1$$
$$5 = \sqrt{m^2 + 1}$$
$$25 = m^2 + 1$$
$$m^2 = 24$$
$$m = 2\sqrt{6}$$ (taking positive value)

**Answer:** $m = 2\sqrt{6}$

### Problem 15.5
**Question:** Find the intersection points of the hyperbola $x^2 - y^2 = 1$ with the ellipse $x^2 + 4y^2 = 6$.

**Solution:**
From the hyperbola equation: $x^2 = 1 + y^2$
Substituting into the ellipse equation:
$$(1 + y^2) + 4y^2 = 6$$
$$1 + 5y^2 = 6$$
$$5y^2 = 5$$
$$y^2 = 1$$
$$y = \pm 1$$

When $y = \pm 1$: $x^2 = 1 + 1 = 2$, so $x = \pm\sqrt{2}$

**Answer:** The intersection points are $(\sqrt{2}, 1)$, $(\sqrt{2}, -1)$, $(-\sqrt{2}, 1)$, $(-\sqrt{2}, -1)$.

### Problem 15.6
**Question:** For the given hyperbola $x^2 - y^2 = 1$, find the distance between its branches.

**Solution:**
The hyperbola $x^2 - y^2 = 1$ can be written as $\frac{x^2}{1} - \frac{y^2}{1} = 1$.

This is a hyperbola with $a^2 = 1$, so $a = 1$.
The vertices are at $(\pm a, 0) = (\pm 1, 0)$.

The distance between the branches is the distance between the vertices: $2a = 2(1) = 2$.

**Answer:** The distance between branches is 2.

## 16. Equations of Planes in Space

### Problem 16.1
**Question:** The plane passes through points $A(1, 2, 3)$, $B(3, 4, 5)$, and $C(2, 1, 4)$. Find the equation of the plane.

**Solution:**
Find two vectors in the plane:
$$\overrightarrow{AB} = (3-1, 4-2, 5-3) = (2, 2, 2)$$
$$\overrightarrow{AC} = (2-1, 1-2, 4-3) = (1, -1, 1)$$

The normal vector is their cross product:
$$\mathbf{n} = \overrightarrow{AB} \times \overrightarrow{AC} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 2 & 2 & 2 \\ 1 & -1 & 1 \end{vmatrix}$$
$$= \mathbf{i}(2 \cdot 1 - 2 \cdot (-1)) - \mathbf{j}(2 \cdot 1 - 2 \cdot 1) + \mathbf{k}(2 \cdot (-1) - 2 \cdot 1)$$
$$= \mathbf{i}(4) - \mathbf{j}(0) + \mathbf{k}(-4) = (4, 0, -4)$$

We can simplify: $\mathbf{n} = (1, 0, -1)$

Using point $A(1, 2, 3)$:
$$1(x - 1) + 0(y - 2) + (-1)(z - 3) = 0$$
$$x - 1 - z + 3 = 0$$
$$x - z + 2 = 0$$

**Answer:** $x - z + 2 = 0$

### Problem 16.2
**Question:** The plane passes through point $A(1, 2, 3)$ and is parallel to the plane $2x + 3y + 4z = 5$. Find the equation of the plane.

**Solution:**
Parallel planes have the same normal vector. The normal vector of $2x + 3y + 4z = 5$ is $(2, 3, 4)$.

Using point $A(1, 2, 3)$:
$$2(x - 1) + 3(y - 2) + 4(z - 3) = 0$$
$$2x - 2 + 3y - 6 + 4z - 12 = 0$$
$$2x + 3y + 4z = 20$$

**Answer:** $2x + 3y + 4z = 20$

### Problem 16.3
**Question:** The plane passes through point $A(1, 2, 3)$ and is perpendicular to the normal vector $\mathbf{n} = [2, 3, 4]$. Find the equation of the plane.

**Solution:**
Using the point-normal form with point $A(1, 2, 3)$ and normal $\mathbf{n} = (2, 3, 4)$:
$$2(x - 1) + 3(y - 2) + 4(z - 3) = 0$$
$$2x - 2 + 3y - 6 + 4z - 12 = 0$$
$$2x + 3y + 4z = 20$$

**Answer:** $2x + 3y + 4z = 20$

### Problem 16.4
**Question:** We have two planes $2x + 3y + 4z = 5$ and $3x + 4y + 2z = 6$. Find the line of intersection of these planes.

**Solution:**
The line of intersection is found by solving the system and expressing one variable in terms of a parameter.

From the first equation: $2x + 3y + 4z = 5$
From the second equation: $3x + 4y + 2z = 6$

Let $z = t$ (parameter). Then:
$$2x + 3y = 5 - 4t$$
$$3x + 4y = 6 - 2t$$

Solving this system:
From the first: $x = \frac{5 - 4t - 3y}{2}$
Substituting into the second:
$$3 \cdot \frac{5 - 4t - 3y}{2} + 4y = 6 - 2t$$
$$\frac{15 - 12t - 9y}{2} + 4y = 6 - 2t$$
$$15 - 12t - 9y + 8y = 12 - 4t$$
$$15 - 12t - y = 12 - 4t$$
$$y = 3 - 8t$$

Then: $x = \frac{5 - 4t - 3(3 - 8t)}{2} = \frac{5 - 4t - 9 + 24t}{2} = \frac{-4 + 20t}{2} = -2 + 10t$

**Answer:** The line of intersection is:
$$\begin{cases} x = -2 + 10t \\ y = 3 - 8t \\ z = t \end{cases}$$

### Problem 16.5
**Question:** Write the equation of the plane passing through point $A(1, 2, 3)$ and parallel to vectors $\vec{v_1} = [1, 0, 1]$ and $\vec{v_2} = [0, 1, -1]$.

**Solution:**
The normal vector is the cross product of the two direction vectors:
$$\mathbf{n} = \vec{v_1} \times \vec{v_2} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 1 & 0 & 1 \\ 0 & 1 & -1 \end{vmatrix}$$
$$= \mathbf{i}(0 \cdot (-1) - 1 \cdot 1) - \mathbf{j}(1 \cdot (-1) - 1 \cdot 0) + \mathbf{k}(1 \cdot 1 - 0 \cdot 0)$$
$$= \mathbf{i}(-1) - \mathbf{j}(-1) + \mathbf{k}(1) = (-1, 1, 1)$$

Using point $A(1, 2, 3)$:
$$-1(x - 1) + 1(y - 2) + 1(z - 3) = 0$$
$$-x + 1 + y - 2 + z - 3 = 0$$
$$-x + y + z = 4$$

**Answer:** $-x + y + z = 4$ or $x - y - z + 4 = 0$

### Problem 16.6
**Question:** We have the plane $2x + 3y + 4z = 5$. Find an example of a plane parallel and perpendicular to it.

**Solution:**
**Parallel plane:** Has the same normal vector $(2, 3, 4)$
Example: $2x + 3y + 4z = 10$

**Perpendicular plane:** Its normal vector must be perpendicular to $(2, 3, 4)$
Example normal vector: $(1, 0, -\frac{1}{2})$ (since $2(1) + 3(0) + 4(-\frac{1}{2}) = 0$)
Example: $x - \frac{1}{2}z = 1$ or $2x - z = 2$

**Answer:** Parallel: $2x + 3y + 4z = 10$, Perpendicular: $2x - z = 2$

### Problem 16.7
**Question:** We have the plane $2x + 3y + 4z = 5$ and point $A(1, 2, 3)$. Find the distance from point $A$ to this plane.

**Solution:**
The distance from point $(x_0, y_0, z_0)$ to plane $ax + by + cz = d$ is:
$$\text{distance} = \frac{|ax_0 + by_0 + cz_0 - d|}{\sqrt{a^2 + b^2 + c^2}}$$

$$\text{distance} = \frac{|2(1) + 3(2) + 4(3) - 5|}{\sqrt{2^2 + 3^2 + 4^2}} = \frac{|2 + 6 + 12 - 5|}{\sqrt{4 + 9 + 16}} = \frac{15}{\sqrt{29}} = \frac{15\sqrt{29}}{29}$$

**Answer:** $\frac{15\sqrt{29}}{29}$

### Problem 16.8
**Question:** The plane intersects the coordinate axes at points $A(2, 0, 0)$, $B(0, 3, 0)$, and $C(0, 0, 4)$. Find the equation of the plane.

**Solution:**
Using the intercept form: $\frac{x}{a} + \frac{y}{b} + \frac{z}{c} = 1$ where $a = 2$, $b = 3$, $c = 4$:

$$\frac{x}{2} + \frac{y}{3} + \frac{z}{4} = 1$$

Multiplying by 12:
$$6x + 4y + 3z = 12$$

**Answer:** $6x + 4y + 3z = 12$

### Problem 16.9
**Question:** Calculate the angle between the plane $x + y + z = 1$ and the plane $x = 0$ (i.e., the $yz$ plane).

**Solution:**
The normal vectors are:
- Plane 1: $\mathbf{n_1} = (1, 1, 1)$
- Plane 2: $\mathbf{n_2} = (1, 0, 0)$

The angle between planes equals the angle between their normal vectors:
$$\cos \theta = \frac{\mathbf{n_1} \cdot \mathbf{n_2}}{|\mathbf{n_1}||\mathbf{n_2}|} = \frac{(1, 1, 1) \cdot (1, 0, 0)}{\sqrt{3} \cdot 1} = \frac{1}{\sqrt{3}}$$

$$\theta = \arccos\left(\frac{1}{\sqrt{3}}\right) = \arccos\left(\frac{\sqrt{3}}{3}\right) \approx 54.74°$$

**Answer:** $\arccos\left(\frac{\sqrt{3}}{3}\right) \approx 54.74°$

### Problem 16.10
**Question:** Find the vector perpendicular to the plane $x + y + z = 1$.

**Solution:**
For a plane $ax + by + cz = d$, the normal vector is $(a, b, c)$.

For the plane $x + y + z = 1$, the normal vector is $(1, 1, 1)$.

**Answer:** $(1, 1, 1)$ (or any scalar multiple)

## 17. Equations of Second-Order Surfaces

### Problem 17.1
**Question:** Write the equation of a sphere with center at point $P=(1,2,3)$ and radius $r=3$.

**Solution:**
The general equation of a sphere with center $(h, k, l)$ and radius $r$ is:
$$(x - h)^2 + (y - k)^2 + (z - l)^2 = r^2$$

With center $(1, 2, 3)$ and radius $3$:
$$(x - 1)^2 + (y - 2)^2 + (z - 3)^2 = 9$$

**Answer:** $(x - 1)^2 + (y - 2)^2 + (z - 3)^2 = 9$

### Problem 17.2
**Question:** Do the spheres with equations $x^2 + y^2 + z^2 = 1$ and $x^2 + y^2 + z^2 = 2$ have any common points?

**Solution:**
The first sphere has center $(0, 0, 0)$ and radius $r_1 = 1$.
The second sphere has center $(0, 0, 0)$ and radius $r_2 = \sqrt{2}$.

Since both spheres are concentric (same center) but have different radii, they do not intersect.

**Answer:** No, the spheres have no common points.

### Problem 17.3
**Question:** What curve in space is formed by the intersection of the sphere $x^2 + y^2 + z^2 = 1$ with the sphere $(x-1)^2 + y^2 + z^2 = 1$? Find the equation of this curve.

**Solution:**
Expanding the second equation:
$$x^2 - 2x + 1 + y^2 + z^2 = 1$$
$$x^2 + y^2 + z^2 - 2x + 1 = 1$$
$$x^2 + y^2 + z^2 = 2x$$

Substituting the first equation:
$$1 = 2x$$
$$x = \frac{1}{2}$$

From the first sphere equation with $x = \frac{1}{2}$:
$$\frac{1}{4} + y^2 + z^2 = 1$$
$$y^2 + z^2 = \frac{3}{4}$$

**Answer:** The intersection is a circle with equation $x = \frac{1}{2}$, $y^2 + z^2 = \frac{3}{4}$.

### Problem 17.4
**Question:** Write the equation of the tangent plane to the paraboloid $z=(x-1)^2+y^2+1$ at point $P(1,0,1)$.

**Solution:**
Let $f(x, y, z) = z - (x-1)^2 - y^2 - 1 = 0$

The gradient at point $(1, 0, 1)$ is:
$$\nabla f = \left(-2(x-1), -2y, 1\right) = (-2(1-1), -2(0), 1) = (0, 0, 1)$$

The tangent plane equation is:
$$0(x - 1) + 0(y - 0) + 1(z - 1) = 0$$
$$z - 1 = 0$$
$$z = 1$$

**Answer:** $z = 1$