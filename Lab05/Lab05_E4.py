
a=[]
for i in range(0,100):
    try:
      a.append([j for j in input().split()])
    except EOFError:
      pass
a.pop()
try:
 result = [[a[l][k] for l in range(len(a))] for k in range(len(a[0]))]
except IndexError:
 print("Invalid Matrix") 
else:
 for row in result:
    line=' '.join(row)
    print(line)