# Assignment 02...

# Problem: Write a Python program that:
# 1. Accepts a string, an integer, a float, and a boolean from the user.
# 2. Initializes variables for each type, and prints them out.
# 3. Convert the string to uppercase and print it.
# 4. Check if the integer is even or odd and print the result.
# 5. Multiply the float by 2 and print the result.
# Get string input from the user and convert it to uppercase

input_string = str(input("Enter a string: ")).upper()

# Get a floating point number from the user and multiply it by 2
input_float = float(input("Enter a floating point number: "))
result = input_float * 2

# Get a boolean value from the user
input_boolean = bool(input("Enter a boolean value (True/False): "))

# Print the results
print("String in uppercase:", input_string)
print("Result of float multiplication by 2:", result)
print("Boolean value:", input_boolean)

# # Function to check if a number is even or odd

def even_or_odd(number):
    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
      
# Try block for handling errors...
try:
    # Get an integer input from the user 
    user_input = int(input("Enter an integer:"))
    even_or_odd(user_input) 
except ValueError: 
# Handle invalid input... 
    print("Please enter a valid integer only.")
    
# Question number 2
# Write a Python program that:
# 1. Accepts two numbers as input from the user.
# 2. Performs and prints the result of all arithmetic operations (addition, subtraction, multiplication, division,
# modulus, floor division) between these two numbers.
# 3. Uses comparison operators to check if the first number is greater than the second, and if they are equal.
# 4. Uses logical operators to combine two conditions (e.g., the first number is greater than the second, and the
# second number is less than 10).
# # calculating sum

def calculator():
    # Get user input for the first number and convert it to float
    num1 = float(input("Enter the first number: "))
    
    # Get user input for the second number and convert it to float
    num2 = float(input("Enter the second number: "))
    
    # Get user input for the operator (+, -, *, /)
    operator = input("Enter an operator (+, -, *, /): ")

    # Perform the calculation based on the operator
    if operator == "+":
        # If the operator is '+', add the two numbers and print the result
        print(num1 + num2)
    elif operator == "-":
        # If the operator is '-', subtract the second number 
        # from the first and print the result
        print(num1 - num2)
    elif operator == "*":
        # If the operator is '*', multiply the two numbers and print the
        #  result
        print(num1 * num2)
    elif operator == "%":
        print(num1 % num2) 
    elif operator == "//":
        print(num1 // num2)        
    elif operator == "/":

        # If the operator is '/', check if the second number is not zero (to avoid division by zero error)
        if num2 != 0:
            print(num1 / num2)
        else:
            # If the second number is zero, print an error message
            print("Error: Cannot divide by zero.")
    else:
        # If the operator is invalid, print a message telling the user to use a valid operator
        print("Invalid operator. Please use one of +, -, *, /.")

# Call the calculator function to start the program
calculator()

def calculator():
    # Accepting two numbers from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Performing and printing the result of all arithmetic operations
    addition = num1 + num2  #addition
    subtraction = num1 - num2 #subtraction
    multiplication = num1 * num2 #multiplication
    # Perform division, ensuring no division by zero
    division = num1 / num2 if num2 != 0 else "Undefined (cannot divide by zero)"
    # Calculate modulus, avoiding division by zero
    modulus = num1 % num2 if num2 != 0 else "Undefined (cannot divide by zero)"
    # Perform floor division safely
    floor_division = num1 // num2 if num2 != 0 else "Undefined (cannot divide by zero)"
    #printing result of all arithmetic operations
    print(f"Addition: {addition}") 
    print(f"Subtraction: {subtraction}")
    print(f"Multiplication: {multiplication}")
    print(f"Division: {division}")
    print(f"Modulus: {modulus}")
    print(f"Floor Division: {floor_division}")

    # Using comparison operators
    is_greater = num1 > num2
    is_equal = num1 == num2

    print(f"First number is greater than second: {is_greater}")
    print(f"First number is equal to second: {is_equal}")

    # Using logical operators to combine two conditions
    both_conditions = (num1 > num2) and (num2 < 10)

    print(f"Both conditions are true: {both_conditions}")

# Calling the calculator function
calculator()
    
# Question number 03: Loops
# Write a Python program that:
# 1. Accepts a list of integers from the user.
# 2. Loops through the list and prints out each number.
# 3. If a number is greater than 10, skips it using the continue statement.
# 4. Stops the loop if the number is 20 using the break statement.
# 5. After the loop ends, prints a message that the loop ended naturally.
# Accept a list of integers from the user
user_input = input("Enter a list of numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))

# Loop through the list and print each number
for num in numbers:
    if num == 20:
        print(f"Breaking at {num}")
        break  # Stop the loop if the number is 20
    if num > 10:
        print(f"Skipping {num}")
        continue  # Skip the number if it's greater than 10
    print(num)

# After the loop ends, print the message
print("Loop ended naturally")
