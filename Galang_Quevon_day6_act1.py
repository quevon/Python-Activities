my_dict = {
    'firstname':'',
    'middlename':'',
    'lastname':''
}

add = "A"
delete = "D"

print("Add Record - A")
print("Delete Record - D")
print("End Program - Any letters")

Selection = str(input("\nChoose letter from the menu: ")).upper()

while Selection  == add or Selection  == delete:
    if Selection  == add:
        key = input("\nEnter key: ").lower()
        if key == 'firstname':
            my_dict['firstname'] = str(input("Enter value: "))
            print("\nFirst Name [firstname]: ", my_dict['firstname'])
            print("Middle Name [middlename]: ", my_dict['middlename'])
            print("Last Name [lastname]: ", my_dict['lastname'])
            Selection  = str(input("\nChoose letter from the menu: ")).upper()
        if key == 'middlename':
            my_dict['middlename'] = str(input("Enter value: "))
            print("\nFirst Name [firstname]: ", my_dict['firstname'])
            print("Middle Name [middlename]: ", my_dict['middlename'])
            print("Last Name [lastname]: ", my_dict['lastname'])
            Selection = str(input("\nChoose letter from the menu: ")).upper()
        if key == 'lastname':
            my_dict['lastname'] = str(input("Enter value: "))
            print("\nFirst Name [firstname]: ", my_dict['firstname'])
            print("Middle Name [middlename]: ", my_dict['middlename'])
            print("Last Name [lastname]: ", my_dict['lastname'])
            Selection = str(input("\nChoose letter from the menu: ")).upper()
        else:
            continue
    if Selection == delete:
        key = input("\nEnter key: ").lower()
        if key == 'firstname':
            my_dict['firstname'] = ''
            print("\nFirst Name [firstname]: ", my_dict['firstname'])
            print("Middle Name [middlename]: ", my_dict['middlename'])
            print("Last Name [lastname]: ", my_dict['lastname'])
            Selection = str(input("\nChoose letter from the menu: ")).upper()
            pass
        if key == 'middlename':
            my_dict['middlename'] = ''
            print("\nFirst Name [firstname]: ", my_dict['firstname'])
            print("Middle Name [middlename]: ", my_dict['middlename'])
            print("Last Name [lastname]: ", my_dict['lastname'])
            Selection = str(input("\nChoose letter from the menu: ")).upper()
            pass
        if key == 'lastname':
            my_dict['lastname'] = ''
            print("\nFirst Name [firstname]: ",  my_dict['firstname'])
            print("Middle Name [middlename]: ",  my_dict['middlename'])
            print("Last Name [lastname]: ",  my_dict['lastname'])
            Selection = str(input("\nChoose letter from the menu: ")).upper()
            pass
        else:
            pass
print("Thank you!")
