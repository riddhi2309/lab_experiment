a= int(input("Enter the no:-"))
b= int(input("Enter the no:-"))
c= int(input("Enter the no:-"))
d= int(input("Enter the no:-"))
e= int(input("Enter the no:-"))
f = (str)(a)+(str)(b)+(str)(c)+(str)(d)+(str)(e)
print(f)
g= (str)(e)+(str)(d)+(str)(c)+(str)(b)+(str)(a)
print(g)
if f==g:
    print("It is a palindrome")
else:
    print("It is not a palindrome")