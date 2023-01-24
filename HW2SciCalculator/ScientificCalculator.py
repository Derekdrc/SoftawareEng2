"""
name: Derek D'Arcy
Description: This program simulates a scientific calculator
"""

import math


def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


def division(num1, num2):
    return num1 / num2


def sin(num):
    """Naturally uses degrees, have to convert if want radians"""
    return math.sin(num)


def cos(num):
    return math.cos(num)


def tan(num):
    return math.tan(num)


def log(num, base):
    return math.log(num, base)


def power(num, exponent):
    return math.pow(num, exponent)


def square_root(num):
    return math.sqrt(num)


def factorial(num):
    return math.factorial(num)


def main():
    """Main continously accepts user input on the numbers and function desired with exception handling until user is done"""
    while True:
        try:
            user_choice = int(input(
                '''Enter '1' to add two numbers \n 
                Enter '2' to subtract two numbers \n
                Enter '3' to multiply two numbers \n 
                Enter '4' to divide two numbers \n
                Enter '5' to find sin of a number \n
                Enter '6' to find cos of a number \n
                Enter '7' to find tan of a number \n
                Enter '8' to find log of a number \n
                Enter '9' to calculate a number to a given power\n
                Enter '10' to find square root of a number \n
                Enter '11' to find the factorial of a number \n
                Enter '12' to end program: '''))
        except ValueError:
            print("Not valid input. Please try again.")
            continue
        if user_choice == 1:
            num1 = float(input("Please enter the first number you wish to add: "))
            num2 = float(input("Please enter the second number you wish to add: "))
            print(f" {num1} + {num2} is {addition(num1, num2)}")
        elif user_choice == 2:
            num1 = float(input("Please enter the first number you wish to subtract: "))
            num2 = float(input("Please enter the second number you wish to subtract: "))
            print(f" {num1} - {num2} is {subtraction(num1, num2)}")
        elif user_choice == 3:
            num1 = float(input("Please enter the first number you wish to multiply: "))
            num2 = float(input("Please enter the second number you wish to multiply: "))
            print(f" {num1} * {num2} is {multiplication(num1, num2)}")
        elif user_choice == 4:
            num1 = float(input("Please enter the first number you wish to divide: "))
            num2 = float(input("Please enter the second number you wish to divide: "))
            while num2 == 0:
                num2 = float(input("The denominator can not be 0. Please enter the second number you wish to divide: "))
            print(f" {num1} / {num2} is {division(num1, num2)}")
        elif user_choice == 5:
            num = float(input("Please enter the number you wish to find the sin of: "))
            degrees = int(input("If this number is in degrees press '1', if it is in radians press '2': "))
            if (degrees == 1):
                print(f"The sin of {num} is {sin(num)}")
            elif (degrees == 2):
                print(f"The sin of {num} is {sin(math.radians(num))}")
            else:
                print("Not a valid input. Please try again")
        elif user_choice == 6:
            num = float(input("Please enter the number you wish to find the cos of: "))
            degrees = int(input("If this number is in degrees press '1', if it is in radians press '2': "))
            if (degrees == 1):
                print(f"The cos of {num} is {cos(num)}")
            elif (degrees == 2):
                print(f"The cos of {num} is {cos(math.radians(num))}")
            else:
                print("Not a valid input. Please try again")
        elif user_choice == 7:
            num = float(input("Please enter the number you wish to find the tan of: "))
            degrees = int(input("If this number is in degrees press '1', if it is in radians press '2': "))
            if (degrees == 1):
                print(f"The tan of {num} is {tan(num)}")
            elif (degrees == 2):
                print(f"The tan of {num} is {tan(math.radians(num))}")
            else:
                print("Not a valid input. Please try again")
        elif user_choice == 8:
            num = float(input("Please enter the number you wish to calculate the log of: "))
            base = float(input("Please enter the log base you wish to use: "))
            print(f"The log of {num} with base {base} is {log(num,base)}")
        elif user_choice == 9:
            num = float(input("Please enter the number you wish to raise to a power: "))
            exponent = float(input("Please enter the exponent you wish to use: "))
            print(f"{num} to the power of {exponent} is {power(num,exponent)}")
        elif user_choice == 10:
            num = float(input("Please enter the number you wish to take the square root of: "))
            print(f"The square root of {num} is {square_root(num)}")
        elif user_choice == 11:
            num = float(input("Please enter the number you wish to find the factorial of: "))
            print(f"{num} factorial is {factorial(num)}")
        elif user_choice == 12:
            print("Goodbye.")
            break
        else:
            print("Not valid input. Please try again.")
            continue


if __name__ == "__main__":
    main()
