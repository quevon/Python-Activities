#Quevon M. Galang
print(" ====================SALARY=======================\n")

Employee_Name = input(" Employee Name: ").title()

while True:
    try:
        Enter_Number = float(input(" Enter Number of Hours: "))
        break
    except:
        print(" Please input a number!")
while True:
    try:
        SSS_contribution = float(input(" SSS Contribution: "))
        break
    except:
        print(" Please input a number!")
while True:
    try:
        Phil_Health = float(input(" Phil Health: "))
        break
    except:
        print (" Please input a number!")
while True:
    try:
        Housing_loan = float(input(" Housing Loan: "))
        break
    except:
        print(" Please input a number!")
Rate_Per_Hour = int(500.00)
Gross_Salary = float(Enter_Number) * float(Rate_Per_Hour)
Result = float(Gross_Salary)
Tax = float(Result) * 0.1
TotalTax = float(Tax)
Deductions = float(SSS_contribution) + float(Phil_Health) + float(Housing_loan)+float(TotalTax)
Total_Salary = float(Result) - float(Deductions)

print(" \n===================PAYSLIP===============================\n")
print("=================EMPLOYEE INFORMATION=======================\n")

print(" Employee Name: " + Employee_Name)
print(" Rendered Hours: " + str(Enter_Number))
print(" Rate per Hour: " + str(Rate_Per_Hour))
print(" Gross Salary: " + str(Result))

print(" \n==============DEDUCTIONS================================\n")

print(" SSS: " + str(SSS_contribution))
print(" PhilHealth: " + str(Phil_Health))
print(" Other Loan: " + str(Housing_loan))
print(" Tax: " + str(TotalTax))
print(" Total Deductions: " + str(Deductions))
print("\n")
print(" Net Salary: " + str((round(Total_Salary, 2))))







