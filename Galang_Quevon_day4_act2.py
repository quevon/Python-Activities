#Quevon M. Galang
firstnum = input("Enter first number: ")
secondnum = input("Enter second numer: ")
Total = int(firstnum) + int(secondnum)

print("First Number: " + str(firstnum))
print("Second Number: " + str(secondnum))
print("Total: " + str(Total))

yesChoice = 'yes'
noChoice = 'no'
while True:
    question = input("Do you want to try again? yes/no :").lower()
    if question == yesChoice :
        firstnum = input("Enter first number: ")
        secondnum = input("Enter second number: ")
        Total = int(firstnum) + int(secondnum)
        print("Total: " + str(Total))
        continue
    elif question == noChoice :
        print("Thank you!")
        break
    else:
        print ('Enter either yes/no')







