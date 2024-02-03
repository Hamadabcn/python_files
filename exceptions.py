# sys library functions and variables used to manipulate different parts of the Python Runtime Environment
import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
# ValueError is an exception, when a function receives an argument of the correct data type but an inappropriate value.
except ValueError:
    print("Error: Invalid input value")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
# sys.exit(1) means exit the program with a status code of 1, something has gone wrong
    sys.exit(1)
print(f"{x} / {y} = {result}")