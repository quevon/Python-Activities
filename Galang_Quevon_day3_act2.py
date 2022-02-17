#Quevon M. Galang


while True:
    try:
        Years = int(input("Years in Service: "))
        break
    except:
        print("Please input a number!")

Information_Technology = 'IT'
Acct = "ACCT"
HR = "HR"

Office = input("Office: ")
Office1 = Office.upper()

if int(Years) >= 10 and Information_Technology == Office1:
    print("You have 10,000 bunos!")
elif int(Years) < 10 and Information_Technology == Office1:
    print("You only have 5,000 bunos!")
elif int(Years) >= 10 and Acct == Office1:
    print("You have 12,000 bunos!")
elif int(Years) < 10 and Acct == Office1:
    print("You only have 6,000 bunos!")
elif int(Years) >= 10 and HR == Office1:
    print("You have 15,000 bunos!")
elif int(Years) < 10 and HR == Office1:
    print("You only have 7,500 bunos!")
else:
    print(f"No {Office1} Office!")


