a=int(input("Enter a :")) 
b=int(input("Enter b :")) 
c=int(input("Enter c :")) 
if (b**2-4*a*c)>=0 :
    G=(b**2-4*a*c)**(1/2)
    X=(-b+G)/(2*a) 
    Y=(-b-G)/(2*a) 
    print("Roots are:  "+str(Y)+" "+str(X)) 