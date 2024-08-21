# L5 Exercises

## Exercise L5.E1: Minimum and Maximum Finder

**Objective:**  
Develop a program to find and display the minimum and the maximum among 10 numbers separated by white spaces entered from the keyboard. The numbers can be negative or non-integers.

**Input/Output:**  
The program should output the minimum and maximum values among the entered numbers.

**Example:**

| Input                               | Result              |
|-------------------------------------|---------------------|
| 4 -6 5.2 -3 4 2.4 35 734 9 -35.3    | Minimum = -35.3     |
|                                     | Maximum = 734       |

**Instructions:**

1. Read a single line of input containing 10 numbers separated by spaces.
2. Store the numbers in a list.
3. Determine the minimum and maximum values from the list.
4. Display the results in the format provided.

---

## Exercise L5.E2: Sentence Generator

**Objective:**  
Develop a program to read the names of two sports that you and your friends love to play and watch. Then generate all possible sentences where the subject is in ["I", "We"], the verb is in ["play", "watch"], and the object is in the two sports. 

**Input/Output:**  
The program should output all possible combinations of the sentences.

**Example:**

| Input             | Result                        |
|-------------------|-------------------------------|
| cricket football  | I play cricket.               |
|                   | I play football.              |
|                   | I watch cricket.              |
|                   | I watch football.             |
|                   | We play cricket.              |
|                   | We play football.             |
|                   | We watch cricket.             |
|                   | We watch football.            |

**Instructions:**

1. Read the names of two sports from the input.
2. Use lists to store subjects, verbs, and objects (the two sports).
3. Generate and print all possible sentences using nested loops.

---

## Exercise L5.E3: Student Marks Calculation

**Objective:**  
Suppose there are 4 students, each having marks for 3 subjects. Develop a program to read the marks from the keyboard and calculate and display the total marks and average mark (rounded to one decimal point) for each student.

**Input/Output:**  
The program should output the total and average marks for each student.

**Example:**

| Input              | Result                   |
|--------------------|--------------------------|
| 50 60 80           | Total: 190 Average: 63.3 |
| 60 75 90           | Total: 225 Average: 75.0 |
| 30 49 99           | Total: 178 Average: 59.3 |
| 66 58 67           | Total: 191 Average: 63.7 |

**Instructions:**

1. Read the marks for 4 students, each having 3 subjects.
2. Store the marks in a 2D list.
3. Calculate the total and average marks for each student.
4. Print the total and average marks as shown in the example.

---

## Exercise L5.E4: Matrix Transpose

**Objective:**  
Develop a program to input a matrix with any dimension and output the transpose of that matrix. Stop accepting rows when `-1` is entered as the input. Handle exceptions such as invalid rows with inconsistent numbers of elements.

**Input/Output:**  
The program should output the transpose of the entered matrix or an error message if the matrix is invalid.

**Example:**

| Input                                | Result                     |
|--------------------------------------|----------------------------|
| 1 2 3 4 5 6                          | 1 2 3 4                    |
| 2 3 4 5 6 7                          | 2 3 4 5                    |
| 3 4 5 6 7 8                          | 3 4 5 6                    |
| 4 5 6 7 8 9                          | 4 5 6 7                    |
| -1                                   | 5 6 7 8                    |
|                                      | 6 7 8 9                    |

**Instructions:**

1. Continuously read rows of the matrix until `-1` is entered.
2. Store the matrix in a 2D list.
3. Check for invalid rows (inconsistent number of elements) and output "Invalid Matrix" if found.
4. Handle other exceptions by outputting "Error".
5. If the matrix is valid, calculate and print the transpose of the matrix.
