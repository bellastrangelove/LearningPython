#this is the lesson two set

#Question One
Integer = float(input("Enter an integer: "))

if Integer < 0:
    print("Negative")
elif Integer > 0:
    print("Positive")
else:
    print("Zero")

if (Integer % 2) == 0:
    print("{0} is Even".format(Integer))
else:
    print ("{0} is Odd".format(Integer))

#Question Two
JobSize = float(input("Enter number of words to be typed: "))
#Calculate Words per hour
WPH = 1800

#rates of pay
Under8 = 21.75
Over8 = 25

#Calculate the number of hours for the job
print("The job will take ", format((JobSize / WPH), '.2f')," hours")

#determine rate for job to be paid at
if JobSize % WPH < 8:
    print ("The job will cost ", '${:,.2f}' .format((JobSize / WPH) * Under8))

else:
    print ("The job will cost ", '${:,.2f}' .format((JobSize / WPH) * Over8))


#Question three
#define values
ClassA = 50
ClassB = 30
ClassC = 15

UserTix = input("Enter the class of the ticket: ")

if UserTix == "A":
    print("Your ticket Costs ",'${:,.2f}' .format(ClassA))
elif UserTix == "B":
    print("Your ticket Costs ", '${:,.2f}'.format(ClassB))
elif UserTix == "C":
    print("Your ticket Costs ", '${:,.2f}'.format(ClassC))
else:
    print("You have entered an invalid class. Please enter A, B or C.")

#Question Four
totalSales = round(float(input("Enter the customers total sales: ")))

if totalSales > 0 and totalSales <= 100:
    print("The customer has 10 points!")
elif totalSales > 100 and totalSales <= 500:
    print("The customer has 20 points!")
elif totalSales > 500:
    print("The customer has 50 points!")
else:
    print("you have entered an invalid sales total.")

#Question five
A = round(float(input("Enter your first number: ")))
B = round(float(input("Enter your second number: ")))
C = round(float(input("Enter your third number: ")))

if A <= B <= C or C <= B <= A:
    print("The middle number is ", B)
elif B <= A <= C or C <= A <= B:
    print("The middle number is ", A)
else:
    print("The middle number is ", C)




