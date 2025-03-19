'''Task 1: Perform Basic Mathematical Operations
Problem Statement: Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
o	Addition
o	Subtraction
o	Multiplication
o	Division
3.  Displays the results of each operation on the screen.'''


num1 = float(input('Enter first number: '))
num2 = float(input('Enter the second number: '))
print('Addition: ',num1+num2)
print('Subtraction: ',num1-num2)
print('Multiplication: ',num1*num2)
print('Division: ',num1/num2)


'''Task 2: Create a Personalized Greeting
Problem Statement: Write a Python program that:
1.  Takes a user's first name and last name as input.
2.  Concatenates the first name and last name into a full name.
3.  Prints a personalized greeting message using the full name.'''

first_name=input('Enter your first name: ')
last_name=input('Enter your last name: ')
full_name= first_name+' '+last_name
print(f'Hello, {full_name}! Welcome to the Python program.')