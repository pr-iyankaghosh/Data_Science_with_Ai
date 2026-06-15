import math
a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))

d=b**2-4*a*c

root1=(-b+math.sqrt(d))/(2*a)
root2=(-b-math.sqrt(d))/(2*a)

print("root_1",root1)
print("root 2",root2)