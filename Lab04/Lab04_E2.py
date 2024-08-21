num=int(input('Input number: '))
abun_num=0
sum=0
if not num<2:
    for i in  range (2,num+1):
        for j in range(1,i):
            if (i%j)==0:
               sum+=j
        if sum>i:
          abun_num+=1
        sum=0   
               
    print("Number of abundant numbers from 1 to",num,"is",abun_num)
else:
    print("Invalid Input")
        