A=int(input("Enter angle 1: "))
B=int(input("Enter angle 2: "))
C=int(input("Enter angle 3: "))
Total_Angle=A+B+C
Min= min(A, B, C)
Max= max(A, B, C)

if (Total_Angle==180)and(A and B and C)!=0:
    if Max ==90 :
       print("Right angled")
    elif Max<=90 :
       print("Acute angled")
    else :
       print("Obtuse angled")
else :
    print("Angles do not form a triangle")