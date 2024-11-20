'''
Write a loop that prompts the user to enter a series of pizza toppings until they enter a
'quit' value. As they enter each topping,
Print a message saying you’ll add that topping to their pizza.
'''
while True:
    topping = input("What would you like to add on your pizza? Enter 'Quit' if you are done.: ")
    if topping == "Quit":
        break
    else:
        print (f"{topping} will be added to your pizza")
        