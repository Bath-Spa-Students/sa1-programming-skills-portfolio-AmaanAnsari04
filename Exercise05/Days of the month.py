'''
## Exercise 5: Days of the Month - 30 Marks

Write a program that tells a user how many days there are in a specific month. Use a dictionary to map the month numbers (1-12) to the number of days in each month.

### Instructions:
1. Create a Dictionary: Define a dictionary where the keys are month numbers and the values are the number of days in those months.
2. Input Handling: Ask the user to input the month number.
3. Check and Output: Use an if-else statement to check if the input is valid and print the number of days in the corresponding month.
'''
Days = {"1":"31",    #assigning days in the month to the month number
          "2":"28",
          "3":"31",
          "4":"30",
          "5":"31",
          "6":"30",
          "7":"31",
          "8":"31",
          "9":"30",
          "10":"31",
          "11":"30",
          "12":"31"}

Months = {"1":"January",  #assigning the names of the month to the month number
          "2":"Feburary", 
          "3":"March",
          "4":"April",
          "5":"May",
          "6":"June",
          "7":"July",
          "8":"August",
          "9":"September",
          "10":"October",
          "11":"November",
          "12":"December"}


try:
    Month = int(input("Enter the Month number (1-12): "))  #asking for input for month number
    if 1 <= Month <= 12:  #check for if the month is between the integers 1 and 12
        print (f"{Months.get(str(Month))} has {Days.get(str(Month))} days in it!") #print statement if input is correct
    else:
        print ("Please enter a valid month number only") #print statment if input is not correct
except ValueError:
    print ("Please enter a Valid month number only (integers 1-12)")
