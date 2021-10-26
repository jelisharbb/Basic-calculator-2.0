operation = int(input("\nSelect one operation. \nType 1 if addition, 2 if subtraction, 3 if multiplication, and 4 if division. \nEnter the number here: "))

if operation == 1:
    print("\nLet's proceed to addition!")

    num1 = float(input("\nEnter a number: "))
    num2 = float(input("Enter another number: "))

    sum = num1+num2
    print(f"{sum} is the sum of {num1} and {num2}. \n ")

if operation == 2:
    print("\nLet's proceed to subtraction!")

    num1 = float(input("\nEnter the minuend: "))
    num2 = float(input("Enter the subtrahend: "))

    difference = num1-num2
    print(f"{difference} is the difference of {num1} and {num2}. \n ")

if operation == 3:
    print("\nLet's proceed to multiplication!")

    num1 = float(input("\nEnter the multiplicand: "))
    num2 = float(input("Enter the multiplier: "))
    
    product = num1*num2
    print(f"{product} is the product of {num1} and {num2}. \n ")

if operation == 4:
     print("\nLet's proceed to division!")

     num1 = float(input("\nEnter the dividend: "))
     num2 = float(input("Enter the divisor: "))
     
     quotient = num1/num2
     print(f"{quotient} is the quotient of {num1} and {num2}. \n ")

if operation > 4:
    print(" \n Sorry, invalid number.")