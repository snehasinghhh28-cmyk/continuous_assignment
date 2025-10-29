#Accept two integres from the user 
a = int(input("Enter first integre:"))
b = int(input ("Enter second integer"))
print("\n---Basic Artithmeti Operations---")
print(f"Addition: {a} + {b} = {a+b}")
print(f"Subtration: {a} - {b} = {a-b}")
print (f"Multiplication: {a} * {b} = {a*b}")
print (f"Floor Division: {a} // {b} =  {a/b}")
print (f"exponentiation: {a} ** {b} = {a ** b}")
# Demonstrating increment / decrement 
a += 1
b -= 1
print (f"After incrementing first number: a = {a}")
print (f" After decrementing second number: b = {b}")