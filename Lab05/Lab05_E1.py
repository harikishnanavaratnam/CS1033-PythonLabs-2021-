numbers=input()
num_list=numbers.split()
maximum=num_list[0]
minimum=num_list[0]
for i in num_list:
 checking=float(i)
 if checking>float(maximum):
     maximum=i
 if checking<float(minimum):
     minimum=i

print(f"Minimum = {minimum}")
print(f"Maximum = {maximum}")