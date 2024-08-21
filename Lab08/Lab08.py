#Get file to read
file=input() 

#Function for Read file name to get n
def getNum(name):
    file=open(name,'r')
    n=int(file.read()) 
    file.close()
    return n

n = getNum(file)

#Function for calculating n th Fibonacci
def fibonacci(n):
    #fib_seq=fibonacci sequence 
    fib_seq=[0,1]
    if n<=1:
        F_n=fib_seq[n] 
    else:
        for i in range(2,n+1):
            fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
        F_n=fib_seq[n]
    return F_n

#Function to show F(n) 
def show(n):
    if (n<0) or (n>20):
        result='Invalid input.'
    else:
        fn=fibonacci(n)
        result=f'Fibonacci({n}) = {fn}'
    return result

answer=show(n)
print(answer)

#Function to write what was displayed to a text file named result.txt. 
def saveFile(name, text):
    result_file=open(name, 'w')
    result_file.write(text)
    result_file.close()

saveFile('result.txt',answer) 