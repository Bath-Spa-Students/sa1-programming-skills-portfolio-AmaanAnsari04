'''
## Exercise 10: Is it even? - 35 Marks

Write a program that tests if a value is even or odd. Follow the instructions outlined below:

### Instructions:
* The program should ask the user for a number from within the main function.
* The entered number should be passed to a function that determines if the value is even or odd.
* The function should return a message indicating whether the number is even or odd.
* The message returned by the function should be printed from within the main function.
'''
def Number(Input): #defines the number func 
    Checker = Input % 2 #calculation operator which will return the remainder of the division of 2 numbers
    if Checker == 0: 
        return(f"{Input} is an even number") #output if number is even
    else:
        return(f"{Input} is an odd number") #output if number is off
    

def main(): #defines main function
    try: 
        Input = int(input("Enter a Number: ")) #asks for input
        Result = Number(Input) #runs number function and saves output in the Result variable
        print (Result)
    except ValueError: #incase of input not being an integer
        print ("Please input whole numbers only")

main()