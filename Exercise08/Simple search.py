'''
## Exercise 8: Simple Search - 30 Marks

Write a program that searches for a specific string within a list of strings. The list is initialized with specific names ("Jake" "Zac", "Ian", "Ron", "Sam", "Dave"). , and your task is to search for "Sam".

### Optional Requirements:
1. Allow the user to input the search term instead of using a predefined value.
2. Implement the search functionality based on user input.
'''

Names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"] #creating a list with all the names
Student_number = int(input("input studen number(0 to 5):")) #take input from user for which student to search for
print (Names[Student_number])

