'''
### Advanced Requirements:
Have the user input their name, hometown, and age instead of hardcoding the values.
Try giving both your first and second name when asked for your name. What happens? How can you handle multiple words in Python?
Test the program by entering a string value for age (e.g., "twenty"). What happens? How can you prevent this issue?
'''

First_Name = (input("What is your First name?: "))
Second_Name = (input("What is your Second name?: "))
Hometown = (input("Where is your home town?: "))
while True:
        Age = (input("What is your age?: "))
        if Age.isdigit():
                Your_info = dict(Name = (First_Name) + " " + (Second_Name), Hometown = (Hometown), Age = (Age))
                print(f"{Your_info.get('Name')}  \n{Your_info.get('Hometown')} \n{Your_info.get('Age')}")
                break
        else:
            print ("Please enter age in numbers")

# Your_info = dict(Name = (First_Name) + " " + (Second_Name), Hometown = (Hometown), Age = (Age))
# print (Your_info)