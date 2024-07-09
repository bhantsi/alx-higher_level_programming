#!/usr/bin/python3

# Define the values of a and b
a = 1
b = 2

# Import the add function from add_0.py
from add_0 import add

# Print the result in the specified format
print("{} + {} = {}".format(a, b, add(a, b)))
