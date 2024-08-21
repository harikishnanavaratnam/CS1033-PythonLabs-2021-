class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def get_output(self):
        '''
        Print the output depending on the evaluated value.
        If the 0 <= value <= 999 the value is printed.
        If the value < 0, UNDERFLOW is printed.
        If the value > 999, OVERFLOW is printed.

        :return: None
        '''
        value = self.evaluate()
        if value > 999:
            print('OVERFLOW')
        elif value < 0:
            print('UNDERFLOW')
        else:
            print(value)

    #####################################################################
    ######### Your task is to implement the following methods. ##########
    #####################################################################
    
    def insert(self, data, bracketed):
        '''
        Insert operators and operands into the binary tree.

        :param data: Operator or operand as a tuple. E.g.: ('OPERAND', 34), ('OPERATOR', ‘+’)
        :param bracketed: denote whether an operator is inside brackets or not. If the operator is inside brackets,
        we set bracketed as True.
        :return: self
        '''
        
        #Include your code here
        if data[0] == 'OPERATOR': #If operator
            if bracketed:
                in_bracket = Node(data)
                in_bracket.insert(self.right.data, False) 
                self.right = in_bracket  #Self reasssignment
            else:
                no_bracket = Node(data)
                no_bracket.left = self
                self = no_bracket #Self reasssignment
        
        else: #If operand
            if not self.left:
                self.left = Node(data)
            elif not self.right:
                self.right = Node(data)
            elif not self.right.right :
                self.right.insert(data, False)
        
        return self

    def evaluate(self):
        '''
        Process the expression stored in the binary tree and compute the final result.
        To do that, the function should be able to traverse the binary tree.

        Note that the evaluate function does not check for overflow or underflow.

        :return: the evaluated value
        '''
        
        #Include your code here
        if not self.right and not self.left:
            return self.data[1]
        else:
            evl_str = str(self.left.evaluate()) + self.data[1].replace("^", "**") + str(self.right.evaluate())
            value = int(eval(evl_str)) #Calculation
            return value