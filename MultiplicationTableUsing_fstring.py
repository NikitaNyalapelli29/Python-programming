num = int(input("Enter the number: "))
print("Table of ",num)
for i in range(1, 11):
   print(str(num) + " * "+str(i) + " = " + str(num*i))
#using f string
    print(f"{num}*{i} ={num*i} ")
