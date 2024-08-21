#Using try,except to overcome Erorr
try:
  #Getting dimensions as n,m
  n,m=input("Enter the dimension: ").split(",")
  
  def matrix(x):
    matrix=[]
    print(f"Enter Matrix {x}: ")
    for rows in range(int(n)):
        row=input().split() 
        #Stop programme when get matrix with wrong dimension
        if  len(row)!=int(m):
            print("Invalid Matrix")
            exit()

        else:
            matrix.append(row) 
    return matrix
  matrix_A=matrix("A")
  matrix_B=matrix("B")
  #Calculate transpose of Matrix B
  def transpose_matrix(matrix): 
    matrix_T = [[matrix[no_of_row][no_of_column] for no_of_row in range(len(matrix))]for no_of_column in range(len(matrix[0]))]
    return matrix_T
  matrix_BT=transpose_matrix(matrix_B)
  
  #Calculate multiplication of Matrix A ,Transpose of Matrix B
  def multiplication_of_matrix(matrix_1,matrix_2):
    result = [[sum(int(a) * int(b) for a, b in zip(A_row, B_column))
                        for B_column in zip(*matrix_2)]
                                for A_row in matrix_1]
    return result
  result=multiplication_of_matrix(matrix_A,matrix_BT)
  #Printing Result matrix
  def disply(matrix):
   for row in range(len(matrix)):
    for coloumn in range(len(result[0])):
        print(matrix[row][coloumn],end=" ")
    print()
  disply(result)
except Exception :
    print('Error')