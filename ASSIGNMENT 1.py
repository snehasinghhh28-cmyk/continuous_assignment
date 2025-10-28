#Giving options for arithmetic operations
print ("Option 1 : Addition" \
"\nOption 2 : Subtraction"
"\nOption 3 : Multiplication" \
"\nOption 4 : Division")
#Taking choice for operations
Ch = input ("what opeartion do you want to perform - ")
#Taking 2 inputs
Num1 = int(input("Enter First number-"))
Num2 = int(input("Enter second number-"))
#Using if-elif-else statements to choose what operation to do based on the choice
if Ch == '1':
    #Adding two numbers and printing value
    Sum = Num1 + Num2 
    print ("Sum = ", Sum)
elif Ch == '2':
    #subtracting two numbers
    Difference = Num1 - Num2
    print ("Difference = ", Difference)
elif Ch == '3':
    #multiplying two numbers
    product = Num1 * Num2 
    print ("product = ", product)
elif Ch == '4':
    # Divinding two numbers and printing values
    quoteint = Num1 / Num2 
    print ("quoteint = ", Quoteint)