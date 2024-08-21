Date=input() 
y,m,d=Date.split()
y=int(y)
m=int(m)
d=int(d)
def Dayofweek(y,m,d):
   if m<3 :
       m+=12
       y-=1
   a= 2*m + 6*(m + 1) / 10
   b=y + int(y/4) -int(y/100) +int(y/400) 
   f1=d+(a)+(b)+1
   f=f1%7
   return int(f)
Day=Dayofweek(y, m, d)
print(Day) 