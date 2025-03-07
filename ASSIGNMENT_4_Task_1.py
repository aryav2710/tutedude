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
