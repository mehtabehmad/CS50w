import sys

try:
    x = int(input('x: '))
    y = int(input('y: '))
except ValueError:
    print("Error: Invalid Input")
    sys.exit(1)

try:
    result = x/y
except ZeroDivisionError:
    print("Error: Cannot divide by Zero")
    sys.exit(1) # 1 here shows that something went wrong

print(f'{x}/{y} = {result}')
