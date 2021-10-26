operation = int(input("\n Select one operation. \n Type 1 if addition, 2 if subtraction, 3 if multiplication, and 4 if division. \n Enter the number here: "))

if operation == 1:
    print(" \n Let's proceed to addition!")

    num1 = float(input("\n Enter a number: "))
    num2 = float(input("Enter another number: "))

    sum = num1+num2
    print(f"{sum} is the sum of {num1} and {num2}.")

if operation == 2:
    print(" \n Let's proceed to subtraction!")

    num1 = float(input("\n Enter the minuend: "))
    num2 = float(input("Enter the subtrahend: "))

    difference = num1-num2
    print(f"{difference} is the difference of {num1} and {num2}.")

if operation == 3:
    print(" \n Let's proceed to multiplication!")
    
    num1 = float(input("Enter the multiplicand: "))
    num2 = float(input("Enter the multiplier: "))
    
    product = num1*num2
    print(f"{product} is the product of {num1} and {num2}.")

if operation == 4:
     print(" \n Let's proceed to division!")

if operation > 4:
    print(" \n Sorry, invalid number.")