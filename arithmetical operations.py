# Python Program to Perform Arithmetic Operations

num1 = float(input(" Please Enter the First Value Number 1: "))
num2 = float(input(" Please Enter the Second Value Number 2: "))

# Add Two Numbers
add = num1 + num2

# Subtracting num2 from num1
sub = num1 - num2

# Multiply num1 with num2
multi = num1 * num2

# Divide num1 by num2
div = num1 / num2

# Modulus of num1 and num2
mod = num1 % num2

# Exponent of num1 and num2
expo = num1 ** num2

print("The Sum of {0} and {1} = {2}".format(num1, num2, add))
print("The Subtraction of {0} from {1} = {2}".format(num2, num1, sub))
print("The Multiplication of {0} and {1} = {2}".format(num1, num2, multi))
print("The Division of {0} and {1} = {2}".format(num1, num2, div))
print("The Modulus of {0} and {1} = {2}".format(num1, num2, mod))
print("The Exponent Value of {0} and {1} = {2}".format(num1, num2, expo))
