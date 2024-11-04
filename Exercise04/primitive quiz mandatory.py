'''
## Exercise 4: Primitive Quiz - 30 Marks

In this exercise, you'll create a simple program that asks the user a question, evaluates their answer, and provides feedback.

### Steps:
1. Write a program that asks the user "What is the capital of France?" and waits for their response.
2. If the user's answer is correct (i.e., "Paris"), the program should print a message saying the answer is correct.
3. If the answer is incorrect, the program should print a message saying the answer is wrong.
'''

Question = str(input("What is the capital of France?: ")) #asking the user for an input
if Question == "Paris":
    print (f"{Question} is the right answer!") #if they answer correctly with correct spelling and capitalization
else:
    print (f"{Question} is not the right answer.") #if they do not answer correctly with correct spelling and capitalization