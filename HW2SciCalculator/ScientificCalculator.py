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
    """Naturally uses degrees, have to convert if want radians"""
    return math.cos(num)


def tan(num):
    """Naturally uses degrees, have to convert if want radians"""
    return math.tan(num)


def log(num, base):
    """Uses math.py log function"""
    return math.log(num, base)


def power(num, exponent):
    """Uses math.py power function"""
    return math.pow(num, exponent)


def square_root(num):
    """Uses math.py square root function"""
    return math.sqrt(num)


def factorial(num):
    """Uses math.py factorial function"""
    return math.factorial(num)


def main():
    """Main continously accepts user input on the numbers and function desired with exception handling until user is done"""
    while True:
        try:
            user_choice = int(input(
                '''\n
                Enter '1' to add two numbers 
                Enter '2' to subtract two numbers 
                Enter '3' to multiply two numbers 
                Enter '4' to divide two numbers 
                Enter '5' to find sin of a number 
                Enter '6' to find cos of a number 
                Enter '7' to find tan of a number 
                Enter '8' to find log of a number 
                Enter '9' to calculate a number to a given power
                Enter '10' to find square root of a number 
                Enter '11' to find the factorial of a number 
                Enter '12' to end program: '''))
        except ValueError:
            """Catches menu choice error that was not an integer character"""
            print("Not valid input. Please try again.")
            continue
        if user_choice == 1:
            """Calls addition with given numbers"""
            num1 = float(input("Please enter the first number you wish to add: "))
            num2 = float(input("Please enter the second number you wish to add: "))
            print(f" {num1} + {num2} is {addition(num1, num2)}")
        elif user_choice == 2:
            """Calls Subtraction with given numbers"""
            num1 = float(input("Please enter the first number you wish to subtract: "))
            num2 = float(input("Please enter the second number you wish to subtract: "))
            print(f" {num1} - {num2} is {subtraction(num1, num2)}")
        elif user_choice == 3:
            """Calls multiplication with given numbers"""
            num1 = float(input("Please enter the first number you wish to multiply: "))
            num2 = float(input("Please enter the second number you wish to multiply: "))
            print(f" {num1} * {num2} is {multiplication(num1, num2)}")
        elif user_choice == 4:
            """Calls division with given numbers, checks 0 us not denominator"""
            num1 = float(input("Please enter the first number you wish to divide: "))
            num2 = float(input("Please enter the second number you wish to divide: "))
            while num2 == 0:
                num2 = float(input("The denominator can not be 0. Please enter the second number you wish to divide: "))
            print(f" {num1} / {num2} is {division(num1, num2)}")
        elif user_choice == 5:
            """Calls sin with given numbers, checks for degrees or radians and converts"""
            num = float(input("Please enter the number you wish to find the sin of: "))
            degrees = int(input("If this number is in degrees press '1', if it is in radians press '2': "))
            if (degrees == 1):
                print(f"The sin of {num} is {sin(math.radians(num))}")
            elif (degrees == 2):
                print(f"The sin of {num} is {sin(num)}")
            else:
                print("Not a valid input. Please try again")
        elif user_choice == 6:
            """Calls cos with given numbers, checks for degrees or radians and converts"""
            num = float(input("Please enter the number you wish to find the cos of: "))
            degrees = int(input("If this number is in degrees press '1', if it is in radians press '2': "))
            if (degrees == 1):
                print(f"The cos of {num} is {cos(math.radians(num))}")
            elif (degrees == 2):
                print(f"The cos of {num} is {cos(num)}")
            else:
                print("Not a valid input. Please try again")
        elif user_choice == 7:
            """Calls tan with given numbers, checks for degrees or radians and converts"""
            num = float(input("Please enter the number you wish to find the tan of: "))
            degrees = int(input("If this number is in degrees press '1', if it is in radians press '2': "))
            if (degrees == 1):
                print(f"The tan of {num} is {tan(math.radians(num))}")
            elif (degrees == 2):
                print(f"The tan of {num} is {tan(num)}")
            else:
                print("Not a valid input. Please try again")
        elif user_choice == 8:
            """Calls log function with given number and base"""
            num = float(input("Please enter the number you wish to calculate the log of: "))
            base = float(input("Please enter the log base you wish to use: "))
            print(f"The log of {num} with base {base} is {log(num,base)}")
        elif user_choice == 9:
            """Calls exponent function with given base and power"""
            num = float(input("Please enter the number you wish to raise to a power: "))
            exponent = float(input("Please enter the exponent you wish to use: "))
            print(f"{num} to the power of {exponent} is {power(num,exponent)}")
        elif user_choice == 10:
            """Calls square root function with given number"""
            num = float(input("Please enter the number you wish to take the square root of: "))
            print(f"The square root of {num} is {square_root(num)}")
        elif user_choice == 11:
            """Calls factorial function with given integer"""
            num = int(input("Please enter the number you wish to find the factorial of: "))
            print(f"{num} factorial is {factorial(num)}")
        elif user_choice == 12:
            """Exits"""
            print("Goodbye.")
            break
        else:
            """Catches menu choice of an integer that was not an option"""
            print("Not valid input. Please try again.")
            continue


if __name__ == "__main__":
    main()
