
addition = '+'
subtraction = '-'
division = '/'
multiplication = '*'
y ='y'
n ='n'


while True:
    try:
        num1 = int(input('Enter first number: '))
        num2 = int(input('Enter second number: '))
    except:
        print("Enter a number!")
        continue
    operator = input('Choose an operator: +,-,/,*: ')
    if operator == addition:
        answer = int(num1) + int(num2)
        print(answer)
        Input = input('Do you want to try again? y/n: ').lower()
        if Input == y:
            continue
        elif Input == n:
            print("Thank you")
            break

    elif operator == subtraction:
        answer = int(num1) - int(num2)
        print(answer)
        Input = input('Do you want to try again? y/n: ').lower()
        if Input == y:
            continue
        elif Input == n:
            print("Thank you")
            break
    elif operator == division:
        try:
            answer = int(num1) / int(num2)
            print(answer)
            Input = input('Do you want to try again? y/n: ')
            if Input == y:
                continue
            elif Input == n:
                print("Thank you")
                break
        except ZeroDivisionError:
            print("Division by zero is error")
            Input = input('Do you want to try again? y/n: ').lower()
            if Input == y:
                continue
            elif Input == n:
                print("Thank you")
            break
    elif operator == multiplication:
        answer = int(num1) * int(num2)
        print(answer)
        Input = input('Do you want to try again? y/n: ').lower()
        if Input == y:
            continue
        elif Input == n:
            print("Thank you")
            break

    else:
        print("Invalid Operator!")
        Input = input('Do you want to try again? y/n: ').lower()
        if Input == y:
            continue
        elif Input == n:
            print("Thank you")
        break







