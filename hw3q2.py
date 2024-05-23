'''
2. Advanced List Methods and Identity Operators

Objective:
The aim of this assignment is to delve deeper into list methods and understand the nuances of identity operators.

Problem Statement:
You have two lists of student names. One list contains the names of students who have submitted their assignments, 
and the other list contains the names of students who attended the last class.

Task 1: Given the two lists: *

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
Find out which students both submitted their assignments and attended the class.

Task 2: Check if the two lists are identical in terms of their content, regardless of order. *

Task 3: Using list methods, remove any student from the attended list who did not submit their assignment. * 

'''

#Task 1: Given the two lists: Find out which students both submitted their assignments and attended the class.
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
sub_att = []

for n in submitted:
    if n in attended:
        sub_att.append(n)
print("The list of students below have both submitted their assignments and also attended the class.")
print(sub_att)
print()

#Task 2: Check if the two lists are identical in terms of their content, regardless of order.
print("It will print True below if identical and False if they are not identical.")
if submitted is attended:
    print(True)
else:
    print(False)
print()

#Task 3: Using list methods, remove any student from the attended list who did not submit their assignment.
for n in attended:
    if n not in submitted:
        attended.remove(n)
print(attended)



