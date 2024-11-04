'''
### Advanced Requirements:
Ignore Capitalization: Modify your program to accept answers regardless of the capitalization (e.g., "paris", "Paris", and "PaRis" should all be considered correct).
Multiple Question_1s: Extend the program into a quiz that asks for the capitals of 10 European countries. Provide feedback for each Question_1.
'''

Question_1 = str(input("What is the capital of France?: ")) #input for 1st Country
if Question_1.lower() == "paris":  #().lower will turn any capital letters to small letters
    print ("That is the correct answer!")
else:
    print ("That is not the correct answer.")

Question_2 = str(input("What is the capital of Germany?: "))#input for 2nd Country
if Question_2.lower() == "berlin":
    print ("That is the correct answer!")
else:
    print ("That is not the correct answer.")

Question_3 = str(input("What is the capital of United Kingdom?: ")) #input for 3rd Country
if Question_3.lower() == "london":
    print ("That is the correct answer!")
else:
    print ("That is not the correct answer.")

Question_4 = str(input("What is the capital of Italy?: "))#input for 4th Country
if Question_4.lower() == "rome":
    print ("That is the correct answer!")
else:
    print ("That is not the correct answer.")

Question_5 = str(input("What is the capital of Spain?: "))#input for 5th Country
if Question_5.lower() == "madrid":
    print ("That is the correct answer!")
else:
    print ("That is not the correct answer.")

Question_6 = str(input("What is the capital of Poland?: "))#input for 6th Country
if Question_6.lower() == "warsaw":
    print ("That is the correct answer!")
else:
    print ("That is not the correct answer.")

Question_7 = str(input("What is the capital of Sweden?: "))#input for 7th Country
if Question_7.lower() == "stockholm":
    print ("That is the correct answer!")
else:
    print ("That is not the correct answer.")

Question_8 = str(input("What is the capital of Ukraine?: "))#input for 8th Country
if Question_8.lower() == "kyiv":
    print ("That is the correct answer!")
else:
    print ("That is not the correct answer.")

Question_9 = str(input("What is the capital of Greece?: "))#input for 9th Country
if Question_9.lower() == "athens":
    print ("That is the correct answer!")
else:
    print ("That is not the correct answer.")

Question_10 = str(input("What is the capital of Norway?: "))#input for 10th Country
if Question_10.lower() == "oslo":
    print ("That is the correct answer!")
else:
    print ("That is not the correct answer.")