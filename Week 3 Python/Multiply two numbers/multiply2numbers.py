"""
Program: multiply two numbers
--------------------
This program asks the user for two
integers and prints the value of the first number
multiplied with the second
"""

def main():
    print("This program multiplies two numbers.")
    
    #simultenously pick value from user and convert to integr
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    value = num1 * num2 #multiplying

    print(value)



# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()