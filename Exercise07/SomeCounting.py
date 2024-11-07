'''
## Exercise 7: Some Counting - 20 Marks

Use your newly acquired knowledge of the for loop to complete the following tasks. Print all values to the console
in each case.
* Write a loop that counts up from 0 to 50 in increments of 1.
* Write a loop that counts down from 50 to 0 in decrements of 1.
* Write a loop that counts up from 30 to 50 in increments of 1.
* Write a loop that counts down from 50 to 10 in decrements of 2.
* Write a loop that counts up from 100 to 200 in increments of 5.
*You may include all loops in a single project*
'''
N1 = 0           #variable starts at 0
while N1 <= 50:  #as long as it is under 50, while loop keeps going
    print (N1)
    if N1 == 50:
        break   #breaks loop when it reaches 50
    N1 +=1      #adds 1 after every loop

N2 = 50         #variable starts at 50
while N2 >= 0:  #as long as its over 0, while loop keeps going
    print (N2)
    if N2 == 0:
        break  #loop breaks when it reaches 0
    N2 -=1     #subtracts 1 after every loop

N3 = 30         #variable starts at 30
while N3 <= 50: #as long as it is under 50, while loop keeps going
    print (N3)
    if N3 == 50:
        break #loop breaks when it reaches 50
    N3 +=1    #adds 1 after every loop

N4 = 50         #variable starts at 50  
while N4 >= 10: #as long as it is over 10, while loop keeps going
    print (N4)
    if N4 == 10:
        break   #loop breaks when it reaches 10
    N4 -=2      # subracts 2 after every loop

N5 = 100         #variable starts at 100
while N5 <= 200: #as long as it us under 200, while loop keeps going
    print (N5)
    if N5 == 200:
        break    #breaks loop when it reaches 200
    N5 +=5       #adds 5 after every loop

