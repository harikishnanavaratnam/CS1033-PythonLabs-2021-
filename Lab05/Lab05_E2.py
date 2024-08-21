subject_list=["I","We"]
verb_list=["play","watch"]
sports=input()
object_list=sports.split()
for i in subject_list:
    for j in verb_list:
        for k in object_list:
            print(i,j,k+".")