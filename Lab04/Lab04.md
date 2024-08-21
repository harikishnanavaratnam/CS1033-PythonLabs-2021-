# L4 Exercises

## Exercise L4.E1: Prime Number Check

**Objective:**  
Develop a program that takes as input a series of positive integers and outputs whether each is a prime. The program should terminate if a negative integer is given as the input. 

**Definition:**  
A prime number is a number that is divisible by only 1 and itself. Note that 1 is not considered a prime number.

**Input/Output:**  
The program should output "prime" if the number is a prime number and "non-prime" otherwise. 

**Example:**

| Input      | Result       |
|------------|--------------|
| 2          | prime        |
| 1          | non-prime    |
| 3          | prime        |
| 10         | non-prime    |
| 11         | prime        |
| 30         | non-prime    |
| 82589933   | prime        |
| -1         | (terminates) |

**Instructions:**

1. Continuously read positive integers from the input.
2. For each integer, check if it is a prime number.
3. Print "prime" for prime numbers and "non-prime" for non-prime numbers.
4. Stop reading inputs and terminate the program if a negative integer is encountered.

---

## Exercise L4.E2: Abundant Number Count

**Objective:**  
Develop a Python program to take as input a positive integer \( n \) greater than 1 and output the number of abundant numbers from 2 to \( n \) inclusive. Output 'Invalid Input' for inputs less than 2.

**Definition:**  
An abundant number is a number for which the sum of its proper divisors is greater than the number itself. 

**Example:**

| Input | Result |
|-------|--------|
| 15    | Number of abundant numbers from 1 to 15 is 1 |
| 1     | Invalid Input |

**Instructions:**

1. Read the integer \( n \) from the input.
2. Check if \( n \) is greater than 1; if not, output "Invalid Input".
3. For each number from 2 to \( n \), determine if it is an abundant number.
4. Count the number of abundant numbers and print the result in the format provided.

---

## Exercise L4.E3: Message Encryption

**Objective:**  
Develop a Python program to encrypt a message based on the following criteria.

**Task:**  
The message will be encrypted using a given base \( b \) (where \( 1 < b \leq 10 \)). Convert the ASCII value of each character of the message into the given base. After converting values of all characters, concatenate these values in the order of characters to form the encrypted message.

**Example:**

For the message "We" with base 2:

1. ASCII values: "W" = 87, "e" = 101.
2. Convert to binary: 87 in base 2 = 1010111, 101 in base 2 = 1100101.
3. Concatenate: "10101111100101".

**Input/Output:**  

| Input               | Result                |
|---------------------|-----------------------|
| Welcome to CSE      | 111312111230120312331231121120013101233200100311031011 |
| Hello world!        | 721011081081113211911111410810033 |

**Instructions:**

1. Read the message and base \( b \) from the input.
2. For each character in the message, obtain its ASCII value and convert it to the specified base.
3. Concatenate all the converted values to produce the encrypted message.
4. Print the encrypted message.
