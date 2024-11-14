#create a nested if-else code

salary = int(input("what is your salary per year?"))       
Experience = float(input("What is your work experience?")) #experience better to be float than int

if salary >= 30000:
    if Experience >= 2:
        print ("Eligible for loan")
    else:
        print ("Sorry your work experience is not enough")
else:
    print ("Sorry your Salary is too low")

