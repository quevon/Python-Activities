#Quevon M. Galang


Rate_Per_Hour = int(500.00)
Taxpercent = float(0.12)

Employee_Name = input("Name: ").title()

while True:
    try:
        Enter_Number = int(input("Enter Number of Hours: "))
        break
    except:
        print("Please input a number!")
while True:
    try:
        Loan = float(input("Loan: "))
        break
    except:
        print("Please input a number!")
while True:
    try:
        Health_Insurance = float(input("Health Insurance: "))
        break
    except:
        print ("Please input a number!")

from GrossSalary import *
from SalaryDeductions import *
from NetSalary import *

print("=========================OUTPUT========================")
print("Name: " + Employee_Name)
print("Hours: " + str(Enter_Number))

print("\nGross Salary: " ,Result(Enter_Number, Rate_Per_Hour))
Gross_Salary = Result(Enter_Number, Rate_Per_Hour)

print("\nTax: " ,Result1(Gross_Salary,Taxpercent))
print("Loan: " + str(Loan))
print("Insurance: " + str(Health_Insurance))

TotalGross = Result1(Gross_Salary,Taxpercent)
print("\nTotal Deductions: " ,result2(Loan,Health_Insurance,TotalGross))
Deductions = result2(Loan,Health_Insurance, TotalGross)
print("\nNet Salary: " ,Result3(Gross_Salary, Deductions))







