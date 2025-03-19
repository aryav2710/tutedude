'''Task 1: Read a File and Handle Errors
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.'''

file_name='sample.txt'
try:
    with open(file_name,'r') as file1:
        reading_file = file1.readlines()
    print("Reading file content:")
    for i,reading_file in enumerate(reading_file,1):
        print(f'Line {i}: {reading_file.strip()}')
except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")


'''Task 2: Write and Append Data to a File

Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.'''

file_name='output.txt'
try:
    with open(file_name,'w') as write_file:
        user_input=input('Enter text to write to the file: ')
        write_file.write(user_input)
        print(f'Data successfully written to {file_name}.\n')
    with open(file_name,'a') as append_file:
        user_input=input('Enter additional text to append: ')
        append_file.write(f'\n{user_input}')
        print('Data successfully appended.\n')
    with open(file_name,'r') as r_file:
        read_file=r_file.readlines()
    print(f'Final content of {file_name}:')
    for i in read_file:
        print(i.strip())
except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
