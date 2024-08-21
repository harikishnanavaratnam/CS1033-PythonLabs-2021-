# L2 Exercises

## Exercise L2.E1: Triangle Type Determination

**Objective:**  
Develop a program to input three angles of a triangle and output the type of the triangle.

**Task:**  
- First, check whether the given angles form a triangle or not.
- If they do form a triangle, then output the type of the triangle as "Right-angled", "Obtuse-angled", or "Acute-angled".
- If the angles do not form a triangle, output "Angles do not form a triangle".

**Input:**  
Three integers representing the angles of a triangle.

**Output:**  
The type of triangle or a message indicating that the angles do not form a triangle.

**Example:**

| Input    | Result                                          |
|----------|-------------------------------------------------|
| 10       | Enter angle 1: Enter angle 2: Enter angle 3:    |
| 15       | Angles do not form a triangle                   |
| 20       |                                                 |
| 90       | Enter angle 1: Enter angle 2: Enter angle 3:    |
| 45       | Right-angled                                    |
| 45       |                                                 |

**Instructions:**

1. Take integer inputs for the three angles.
2. Verify if the sum of the angles is equal to 180 degrees.
3. Determine the type of the triangle:
   - **Right-angled:** One angle is 90 degrees.
   - **Obtuse-angled:** One angle is greater than 90 degrees.
   - **Acute-angled:** All angles are less than 90 degrees.
4. Display the appropriate message based on the angles.

---

## Exercise L2.E2: Day of the Week Calculation

**Objective:**  
Develop a program that reads a date as three numbers separated by white spaces and outputs the corresponding day of the week.

**Task:**  
Given a date as a triplet of numbers \(y\), \(m\), and \(d\) (where \(y\) is the year, \(m\) is the month, and \(d\) is the day), calculate the corresponding day of the week \(f\) using the following steps:

1. If \(m < 3\), set \(m = m + 12\) and \(y = y - 1\).
2. Calculate:
   \[
   a = {2m + 6(m + 1)}/{10}
   \]
3. Calculate:
   \[
   b = y + \frac{y}{4} - \frac{y}{100} + \frac{y}{400}
   \]
4. Calculate:
   \[
   f1 = d + a + b + 1
   \]
5. Finally, calculate:
   \[
   f = f1 \mod 7
   \]
   where \(f = 0\) corresponds to Sunday, \(f = 1\) corresponds to Monday, etc.

**Input:**  
Three integers representing the year, month, and day of the date.

**Output:**  
An integer corresponding to the day of the week, where:
- \(0\) = Sunday
- \(1\) = Monday
- \(2\) = Tuesday
- \(3\) = Wednesday
- \(4\) = Thursday
- \(5\) = Friday
- \(6\) = Saturday

**Example:**

| Input    | Result |
|----------|--------|
| 2021 6 24 | 4      |

**Instructions:**

1. Read the year \(y\), month \(m\), and day \(d\) as input.
2. Follow the steps outlined above to calculate the day of the week.
3. Output the corresponding integer \(f\) that represents the day of the week.

---

## Exercise L2.E3: Electricity Bill Calculation

**Objective:**  
Develop a program to input the units of electricity (number of kWh) consumed monthly and output the calculated electricity bill for that month. The charges differ according to the domestic purpose plan from the Ceylon Electricity Board.

**Task:**  
Calculate the monthly electricity bill based on the units consumed using the following tariff structure:

**Tariff Structure:**

1. **For consumption between 0-60 kWh per month:**
    - **0-30 kWh:** 
        - Unit Charge: Rs 2.50 per kWh
        - Fixed Charge: Rs 30.00 per month
    - **31-60 kWh:** 
        - Unit Charge: Rs 4.85 per kWh
        - Fixed Charge: Rs 60.00 per month

2. **For consumption above 60 kWh per month:**
    - **0-60 kWh:**
        - Unit Charge: Rs 7.85 per kWh
    - **61-90 kWh:**
        - Unit Charge: Rs 10.00 per kWh
        - Fixed Charge: Rs 90.00 per month
    - **91-120 kWh:**
        - Unit Charge: Rs 27.75 per kWh
        - Fixed Charge: Rs 480.00 per month
    - **121-180 kWh:**
        - Unit Charge: Rs 32.00 per kWh
        - Fixed Charge: Rs 480.00 per month
    - **Above 180 kWh:**
        - Unit Charge: Rs 45.00 per kWh
        - Fixed Charge: Rs 540.00 per month

**Example Calculation:**

If the consumption is 45 kWh, the bill calculation would be:

\[
\text{Monthly Bill} = 30 \times 2.5 + (45 - 30) \times 4.85 + 60 = Rs 207.75
\]

**Input:**  
A single integer representing the number of kWh consumed in a month.

**Output:**  
A floating-point number representing the calculated electricity bill for that month in Rs.

**Example:**

| Input | Result |
|-------|--------|
| 45    | 207.75 |
| 65    | 611.00 |

**Instructions:**

1. Input the number of kWh consumed in a month.
2. Use the given tariff structure to calculate the total electricity bill.
3. Output the calculated bill as a floating-point number.
