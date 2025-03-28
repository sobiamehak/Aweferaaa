
#  Python Programming Assignment 01
# Question 1: Write a Python program that takes a
#  string as input and prints:
# 1. The string in reverse order.
# 2. The number of vowels in the string.

          # Q1: Reverse string and count vowels

# Taking input string from the user
text = input("Enter something to reverse: \n")

# Defining the set of vowels (both lowercase and 
# uppercase)
vowels = "aeiouAEIOU" 

# Variable to store the count of vowels
vowel_count = 0

# Reversing the string using slicing [::-1]
reversed_text = text[::-1]  

# Looping through each character of the input string
for char in text:
    # Checking if the character is a vowel
    if char in vowels:
        # Incrementing vowel count if the character
        #  is a vowel
        vowel_count += 1

# Printing the reversed string
print(f"Reversed: {reversed_text}")

# Printing the count of vowels
print(f"Vowels: {vowel_count}")


        # Q2: Problem: Create a Python program that:
# ● Takes an input number from the user.
# ● Checks whether the number is even or odd.
# ● Prints the result.

       

# Function to check if a number is even or odd
def check_even_odd():
    try:
        # Taking input from user and converting it to an integer
        num = int(input("Enter a number: \n"))  

        # Checking if the number is even
        if num % 2 == 0:
            print(f"{num} is even")
        else:
            # If the number is not even, it's odd
            print(f"{num} is odd")
    except ValueError:
        # Handling invalid input if it's not a number
        print("Invalid input! Enter a valid number.")

# Calling the function to execute
check_even_odd()  

      # Q3: Problem: Create a Python program that:
# 1. Takes a list of integers as input.
# 2. Creates a new virtual environment called sortenv.
# 3. Installs a package (such as numpy) in the virtual
#  environment.
# 4. Sorts the list using a numpy method (numpy.sort()).
# 5. Prints the sorted list.
      # Sort a list of numbers using NumPy

# Importing numpy for sorting
import numpy as np

# Function to sort a list of numbers
def sort_numbers(arr):
    # Using NumPy's sort function to sort the list in ascending order
    return np.sort(arr)  

# Taking input from the user, asking for numbers separated by spaces
try:
    input_list = input("Enter numbers separated by spaces: ")

    # Converting the input string into a list of integers
    numbers = list(map(int, input_list.split()))  

    # Sorting the list and printing the result
    print("Sorted list:", sort_numbers(numbers))

# Handling invalid input (non-numeric values)
except ValueError:
    print("Invalid input! Enter a list of integers.")
