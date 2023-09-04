x = int(input("Enter the three digit number:-"))
first_digit= int(int(x)[0])
tenth_digit = int(int(x)[1])
hunderth_digit = int(int(x)[2])
sum  = first_digit + tenth_digit+ hunderth_digit
print(sum)
if sum%3 == 0:
    print ("The number is divisible by 3" , sum)
else:
    print("The number is not divisible by 3" , sum)