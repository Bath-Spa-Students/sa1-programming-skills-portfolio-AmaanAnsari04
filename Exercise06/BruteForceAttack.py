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
password = 12345 #this is the correct password needed
while True:
    Code = int(input("Please enter the password: ")) #ask for password input
    if Code == 12345:   
        print ("That is the correct password!") #print statement if correct
    else:
        print ("That is an incorrect password. You gave 4 more tries") #print statment if incorrect and let them know how my tries they have left
        Code = int(input("Please enter the password: "))
        if Code == 12345:
            print ("That is the correct password!")
        else:
            print ("That is an incorrect password. You have 3 more tries") #print statment if incorrect and let them know how my tries they have left
            Code = int(input("Please enter the password: "))
            if Code == 12345:
                print ("That is the correct password!")
            else:
                print ("That is an incorrect password. You have 2 more tries") #print statment if incorrect and let them know how my tries they have left
                Code = int(input("Please enter the password: "))
                if Code == 12345:
                    print ("That is the correct password!")
                else:
                    print ("That is an incorrect password. You have 1 more try") #print statment if incorrect and let them know how my tries they have left
                    Code = int(input("Please enter the password: "))
                    if Code == 12345:
                        print ("That is the correct password!")
                    else:
                        print ("That is an incorrect password. This has been reported to the authorities.") #print statment if incorrect and let them know they've been reported to the authorities
                        break