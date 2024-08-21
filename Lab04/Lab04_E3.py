mess=input("Enter message: ")
base=int(input("Enter base: "))
encode=""
for i in mess:
      ascii_value=ord(i)
      value_down=""
      while ascii_value>=base:
        ex=ascii_value%base
        value_down+=str(ex)
        ascii_value=ascii_value//base
      value_up=value_down[-1::-1]
      encode=encode+str(ascii_value)+value_up
print(encode)   
