basic_salary = int(input("Enter the salary of the person:-"))
HRA = (int(20*basic_salary)/100)
TA = (int(5*basic_salary)/100)
DA = (int(10*basic_salary)/100)
gross_salary = basic_salary + HRA + TA + DA 
print(gross_salary)
if gross_salary < 300000:
    print("Income tax is 0% of gross value")
elif gross_salary < 1000000:
    print("Income tax is 10% of gross value")
elif gross_salary < 2500000:
    print("Income tax is 20% of gross value ")
else:
    print("Income tax is 30% of the gross value")