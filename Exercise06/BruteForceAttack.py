'''
## Exercise 6: Brute Force Attack - 30 Marks

Write a program that simulates a password entry system. The correct password is defined as 12345. The program should keep asking the user to enter the password until they provide the correct one.

### Basic Requirements:
1. Define the correct password.
2. Use a while loop to repeatedly ask the user for the password until the correct one is entered.
3. Output an appropriate message when the correct password is entered.

### Optional Requirements:

Modify the program to include a maximum of 5 password attempts. If the user enters the wrong password, inform them of the remaining attempts. If the maximum number of attempts is reached, inform the user that the authorities have been alerted.
'''
password = 12345
while True:
    Code = int(input("Please enter the password: "))
    if Code == 12345:
        print ("That is the correct password!")
    else:
        print ("That is an incorrect password. You gave 4 more tries")
        Code = int(input("Please enter the password: "))
        if Code == 12345:
            print ("That is the correct password!")
        else:
            print ("That is an incorrect password. You have 3 more tries")
            Code = int(input("Please enter the password: "))
            if Code == 12345:
                print ("That is the correct password!")
            else:
                print ("That is an incorrect password. You have 2 more tries")
                Code = int(input("Please enter the password: "))
                if Code == 12345:
                    print ("That is the correct password!")
                else:
                    print ("That is an incorrect password. You have 1 more try")
                    Code = int(input("Please enter the password: "))
                    if Code == 12345:
                        print ("That is the correct password!")
                    else:
                        print ("That is an incorrect password. This has been reported to the authorities.")
                        break