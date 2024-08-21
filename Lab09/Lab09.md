# L9 Exercises

## Exercise L9.E1: Symbolic Equation Solver

**Objective:**  
Implement a simple symbolic equation solver using a binary tree. Each operand or operator in the equation should be stored as a tuple in the binary tree, with the following format:

- **Operand:** `(OPERAND, VALUE)` where `VALUE` is a number.
- **Operator:** `(OPERATOR, VALUE)` where `VALUE` is one of the following: `+`, `-`, `*`, `^`.

**Operators Supported:**  
- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)
- Exponentiation (`^`)

**Task Instructions:**

1. **Binary Tree Representation:**
   - Each node in the binary tree should be a tuple of the form `(TYPE, VALUE)`.
     - **Example Tuples:** 
       - `(OPERAND, 5)`
       - `(OPERATOR, '+')`

2. **Function Development:**
   - **Function 1: `insert`**
     - Insert nodes into the binary tree according to the structure of the symbolic equation.
   - **Function 2: `evaluate`**
     - Compute the result of the equation stored in the binary tree.

**Skeleton Code:**

The skeleton for this lab exercise is provided below. Complete the bodies of the `insert` and `evaluate` methods. Do not modify any code outside of these methods.

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    '''
    Inserts a value into the binary tree.
    You need to complete this function.
    '''
    pass

def evaluate(root):
    '''
    Evaluates the expression represented by the binary tree.
    You need to complete this function.
    '''
    pass
