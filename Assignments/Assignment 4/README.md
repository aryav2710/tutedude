# Python Programs for File Handling

## Description
This repository contains two Python programs:

### 1. Read a File and Handle Errors
This program performs the following tasks:
- Opens and reads a text file named `sample.txt`.
- Prints its content line by line.
- Handles errors gracefully if the file does not exist.

### 2. Write and Append Data to a File
This program:
- Takes user input and writes it to a file named `output.txt`.
- Appends additional data to the same file.
- Reads and displays the final content of the file.

## How to Run the Programs
1. Ensure you have Python installed on your system (Python 3 recommended).
2. Create a text file named `sample.txt` (for Task 1) and add some content to it.
3. Open a terminal or command prompt.
4. Run the script using the following command:
   ```sh
   python filename.py
   ```
5. Follow the prompts to enter the required inputs.
6. The program will display the respective outputs.

## Example Usage
### Read a File and Handle Errors
```
Reading file content:
Line 1: This is the first line.
Line 2: This is the second line.
```
```
Error: The file 'sample.txt' was not found.
```

### Write and Append Data to a File
```
Enter text to write to the file: Hello, World!
Data successfully written to output.txt.

Enter additional text to append: Welcome to file handling in Python.
Data successfully appended.

Final content of output.txt:
Hello, World!
Welcome to file handling in Python.
```
