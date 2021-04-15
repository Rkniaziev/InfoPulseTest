x = input("Enter first number: ")
y = input("Enter second number: ")
try:
    x = int(x)
    y = int(y)
    print(x + y)
except ValueError:
    x = str(x)
    y = str(y)
    print(x + y)
