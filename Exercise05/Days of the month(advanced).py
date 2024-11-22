'''
### Advanced Requirement:
Leap Year Adjustment: Modify the program to account for leap years. For February, ask the user if the year is a leap year and adjust the number of days accordingly.
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
          "2":"February", 
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
        if Month == 2:
            leap_year = input("Is it a leap year (yes/no): ") #if input is 2, it asks if its a leap year
            if leap_year == "yes": 
                print (f"{Months.get(str(Month))} has 29 days in it!") #print statment if yes
            elif leap_year == "no":
                print (f"{Months.get(str(Month))} has {Days.get(str(Month))} days in it!") #print statement if no
            else:
                print ("Please Enter yes/no only!") #print statemtn if input is something other than yes or no
    else:
        print ("Please enter a valid month number only") #print statment if input is not correct
except ValueError:
    print ("Please enter a Valid month number only (integers 1-12)") 