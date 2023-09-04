a = int(input("Enter the first no.:-"))
b = int(input("Enter the second no.:-"))
c = int(input("Enter the third no.:-"))
abc = a,b,c
cube_root = a**3 + b**3 + c**3
print(a,b,c)
print(cube_root)
if abc == cube_root:
    print("It is an armstrong no.")
else:
    print("It is not an armstrong no.")