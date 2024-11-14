print ("Do not add more than 5 apples")
apples = int(input("How many apples are there in the basket: "))
if apples > 5:
    cost = (int(apples) - 5)
    print(f"remove {cost} ")
else:
    print("You can add more apples")
