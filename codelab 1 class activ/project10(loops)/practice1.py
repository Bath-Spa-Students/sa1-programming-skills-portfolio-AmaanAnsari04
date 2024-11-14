#creating an infinite loop with while
stock = int(input("How much stock is left?:"))
while stock > 0:
    print (f"there are {stock} items left ")
    stock -= 1
    if stock == 0:
        stock +=10

