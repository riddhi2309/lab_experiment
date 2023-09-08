x = int(input("Enter the three digit number:-"))
a=0
b=0
while x!=0:
    a=x%10
    b=b+a
    x=x//10
print(b)
