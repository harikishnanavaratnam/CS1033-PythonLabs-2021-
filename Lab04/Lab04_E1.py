while True:
   num=int(input())
   if num<0:
       quit()
   if num==1 or 0 :
     print("non-prime")
   if num > 1:
     for i in range(2,num):
        if (num%i)==0 :
            print("non-prime")
            break
     else:
        print("prime")