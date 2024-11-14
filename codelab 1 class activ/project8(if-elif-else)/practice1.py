#You can replace multiple if-else statements with just an elif statment

choice1 = int(input("Choose a numner 1 to 10: "))        #takes input for variable1
choice2 = int(input("Choose another number 1 to 10: "))  #takes input for variable2

if (choice1 > 10) and (choice2 > 10):                    #making sure the numbers first fit into the given criteria 
    print ("Both numbers are too big")
elif (choice1 < 1) and (choice2 < 1):
    print ("Both numbers are too small")
elif choice1 > 10:                            
    print ("First number was too big")
elif choice1 < 1:
    print ("First number was too small")
elif choice2 > 10:
    print ("Second number was too big")
elif choice2 < 1:
    print ("Second number was too small")
elif choice1 > choice2:                                #if numbers are correct, print out a comparison of the two numbers
    print ("First number was greater than the second")
elif choice1 == choice2:
    print ("Both numbers are equal")
elif choice1 < choice2:
    print ("Second number is greater")