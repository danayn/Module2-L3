'''
1. Python List Transformation

Objective:
The aim of this assignment is to practice advanced list operations and transformations.

Problem Statement:
You've been given a list of numerical grades from a class exam. You need to process and analyze these grades.

Task 1: Given the list of grades: *

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
Sort the grades in descending order and display the sorted list.

Task 2: Calculate the average grade and display it. * 

Task 3: Replace any grade below 80 with the value Failed. *


'''

#Task 1 -- Sort the grades in descending order and display the sorted list. (Use the reverse=True in sort())
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort(reverse=True)
print(grades)
print()

#Task 2: Calculate the average grade and display it. 
length = len(grades)
sum = 0
for n in grades:
    sum = sum + n
avg_grade = sum / length
print(avg_grade)
print()

#Task 3: Replace any grade below 80 with the value Failed.
i = 0
while(i < len(grades)):
    if(grades[i] < 80):
        grades[i] = "Failed"
    i = i + 1
print(grades)




