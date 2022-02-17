while True:
    print('=============SELECTION=================\n')
    print("Add Record = A")
    print("View Records = B")
    print("Clear All Records = C")
    print("Exit = D")

    Input = input("\nChoose an action: ").upper()

    if Input == 'A':

        Name = str(input('Enter Name: '))
        Email = str(input('Enter Email: '))
        Address = str(input('Enter Address: '))
        myFile = open('info.txt', 'a')
        myFile.write(f'\nName: {Name} \nEmail: {Email} \nAddress: {Address}\n\n')
        myFile.close()
    elif Input == 'B':
        print("\n==============RECORDS================\n")
        myFile = open('info.txt', 'r')
        print(myFile.read())
        myFile.close()
    elif Input == 'C':
        print("\nNo Record found!\n")
        myFile = open('info.txt', 'r+')
        myFile.truncate()
        myFile.close()
    elif Input == 'D':
        print("Thank you")
        break
    else:
        print("\nNot Available in Selection!\n")