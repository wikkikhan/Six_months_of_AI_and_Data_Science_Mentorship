# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# Functions can return data as a result.
# In Python, a function is defined using the def keyword.

# lets define a function
def greet_user():
    print("Hello User!")

# greet_user()

def aoa():
    print("Assalam o Alykum, All the way from Lodon.")

# aoa()

def aoa(name):
    print(f"Assalam o Alykum, {name}!")

# aoa("Waqar")

def aoa(name="khuda k bandy"):
    print(f"Assalam o alykum, {name}!, Kaifa Haluk")

# aoa('Waqar')




# Return values
def square(number):
    return number * number

# print(square(2))


# Recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# print(factorial(5))

# lambda function
x = lambda a: a / 10
# print(x(5))

x = lambda a, b: a*b
print(x(2,8))