# L8 Exercises

## Exercise L8.E1: Fibonacci Sequence Computation

**Objective:**  
Develop a Python program to compute the Fibonacci sequence \( F(n) \) for a given integer \( n \) between 0 and 20.

**Fibonacci Sequence Definition:**

The Fibonacci sequence is defined as:

\[
F(n) = \begin{cases} 
0 & \text{if } n = 0 \\
1 & \text{if } n = 1 \\
F(n-1) + F(n-2) & \text{for } n \geq 2
\end{cases}
\]

**Input Range:**  
- \( 0 \leq n \leq 20 \)

**Output Format:**  
- For a given \( n \), output the computed Fibonacci value \( F(n) \) in the format: `Fibonacci(n) = result`

**Task Instructions:**

1. **File Creation:**
   - Create a text file containing the value of \( n \). This text file should be saved in the same directory as the source file. The file name will be provided as input through the terminal.

2. **Function Development:**
   - **Function 1: `getNum`**
     - Read the integer \( n \) from the text file.
   - **Function 2: `show`**
     - Display the given value \( n \) and the computed value \( F(n) \) on the screen in the format: `Fibonacci(n) = result`.
   - **Function 3: `saveFile`**
     - Write the output displayed in `show` to a text file named `result.txt`. This file should be saved in the same directory as the source file.

3. **Error Handling:**
   - If \( n \) is outside the range \( 0 \leq n \leq 20 \) or if there are other incompatible values, print `Invalid input.`

**Expected Output Format:**

| Input \( n \) | Output                |
|---------------|-----------------------|
| 3             | Fibonacci(3) = 2      |
| 10            | Fibonacci(10) = 55    |

---

**Note:** Ensure all files (`result.txt` and the input file containing \( n \)) are saved in the same directory as the Python source file.
