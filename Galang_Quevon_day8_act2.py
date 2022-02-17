class Employee:
    def __init__(self, name , email, mobile_number):
        self.myname = name
        self.myemail = email
        self.mynumber = mobile_number
emp = Employee("quevon", "quevon@gmail.com" , '09304893560')
print("Name: ",emp.myname )
print('Email: ',emp.myemail)
print('Mobile Number: ',emp.mynumber)

emp = Employee("josh", "josh@gmail.com" , '09284789567')

print("\nName: ", emp.myname)
print('Email: ', emp.myemail)
print('Mobile Number: ', emp.mynumber)


