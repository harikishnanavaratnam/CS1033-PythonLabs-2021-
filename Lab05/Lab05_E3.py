a=[] 
for i in range(0,4):   
   a.append([int(j) for j in input().split()])
x=0
while x<4:
 total=0
 for i in a[x]:
     total+=int(i)
     average="{:.1f}".format(total/3)
 print(f"Total: {total} Average: {average}")
 x+=1
 