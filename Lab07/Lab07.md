# L7 Exercises

## Exercise L7.E1: Generating National Identity Card (NIC) Numbers

**Objective:**  
Develop a program to read the name, birthday, and gender of a person from a file and output the ten-digit national identity card (NIC) number. The only input to the program is the name of the file.

**NIC Number Format:**
- The first four digits represent the birth year.
- The next three digits represent the number of days from January 1st to the birth date.
  - For example:
    - January 1st -> 001
    - January 2nd -> 002
    - February 1st -> 032
- If the person is female, 500 is added to the day count.
- The final three digits are assigned in the order of submission for a particular birth year.

**Input:**  
A file containing records where each record consists of the person's name, birthday, and gender, separated by spaces.

**Output:**  
For each record, output the person's name followed by their corresponding NIC number.

**Example:**

### Input File:

| Name    | Birthday   | Gender |
|---------|------------|--------|
| Saman   | 1990-05-03 | M      |
| Aruni   | 1990-04-06 | F      |
| Kumaran | 1988-03-05 | M      |
| Nazar   | 1997-09-24 | M      |

### Expected Output:

| Name    | NIC Number   |
|---------|--------------|
| Saman   | 1990123001   |
| Aruni   | 1990596002   |
| Kumaran | 1988065001   |
| Nazar   | 1997267001   |

**Instructions:**
1. **File Reading:**
   - The program should read the input file containing the name, birthday, and gender of individuals.
   
2. **Date Processing:**
   - Calculate the day of the year corresponding to the birth date.
   - If the individual is female, add 500 to the day count.
   
3. **NIC Generation:**
   - Generate the NIC number using the birth year, modified day count, and order of submission.
   
4. **Error Handling:**
   - Ensure the program handles any possible errors, such as incorrect file formats or data inconsistencies.
