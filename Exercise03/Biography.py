'''
## Exercise 3: Biography - 25 Marks

In this exercise, you'll create a program that stores and prints your name, hometown, and age to the console using a Python dictionary.

### Steps:
1. Store the information (name, hometown, and age) as key-value pairs in a dictionary.
2. Print the values on separate lines using a single `print()` statement.
3. Use variables with appropriate data types for each piece of information.
'''

Your_info = {"Name": "Amaan Ansari",   #creating a dictionary
            "Hometown": "Karachi",
            "Age": 20}
print(f"{Your_info.get('Name')}  \n{Your_info.get('Hometown')} \n{Your_info.get('Age')}") #using the /n function to print them on different lines