'''Task 1: Create a Dictionary of Student Marks

Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.'''

result = {'Alice':90,'Vivek':92,'Arya':86}
a=input('Enter the student\'s name: ')
if a in result:
    print('{}\'s marks: {}'.format(a,result[a]))
else:
    print('Student not found.')


'''Task 2: Demonstrate List Slicing
Problem Statement: Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list'''

olist = list(range(1,11))
print(f'Original list: {olist}')
fflist = olist[:5]
print(f'Extracted first five elements: {fflist}')
rlist = fflist[::-1]
print(f'Reversed extracted elements: {rlist}')



