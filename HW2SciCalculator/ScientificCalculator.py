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


def sin(num1):
    """Naturally uses degrees, have to convert if want radians"""
    return math.sin(num1)


def cos(num1):
    return math.cos(num1)


def tan(num1):
    return math.tan(num1)


def log(num1, Base):
    return math.log(num1, Base)


def power(num1, exponent):
    return math.pow(num1, exponent)


def square_root(num1):
    return math.sqrt(num1)


def factorial(num1):
    return math.factorial(num1)


def main():
    """Main continously accepts user input on the numbers and function desired with exception handling until user is done"""
    while True:
        try:
            user_choice = int(input(
                "Please enter '1' to add two numbers, enter '2' to subtract two numbers, enter '3' to multiply two numbers, enter '4' to divide two numbers, and enter '5' to end program: "))
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
            print("Goodbye.")
            break
        else:
            print("Not valid input. Please try again.")
            continue


if __name__ == "__main__":
    main()
