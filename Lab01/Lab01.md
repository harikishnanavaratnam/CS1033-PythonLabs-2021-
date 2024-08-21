# Problem Statement: Quadratic Equation Roots Computation

### L1

**Objective:**  
Try out the code given under Step 8 of L1.4 from your Lab notes.

**Task:**  
Implement a Python program intended to compute the roots of the quadratic equation provided that \( b^2 - 4ac \geq 0 \), given integers `a`, `b`, and `c`.

**Input:**  
Three integers `a`, `b`, and `c` representing the coefficients of the quadratic equation.

**Output:**  
The roots of the quadratic equation.

**Example:**

| Input | Result               |
|-------|----------------------|
| 1     | Enter a :1           |
| 5     | Enter b :5           |
| 6     | Enter c :6           |
|       | Roots are: -3.0 -2.0 |

**Instructions:**

1. Take integer inputs for `a`, `b`, and `c`.
2. Calculate the roots of the quadratic equation using the formula:
   \[
   x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
   \]
3. Ensure that the discriminant \( b^2 - 4ac \) is non-negative.
4. Display the roots.
