basic_salary = int(input("Enter the salary of the person:-"))
HRA = (int(20*basic_salary)/100)
TA = (int(5*basic_salary)/100)
DA = (int(10*basic_salary)/100)
gross_salary = basic_salary + HRA + TA + DA 
print(gross_salary)