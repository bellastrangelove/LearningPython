#this is question one lesson one

#get the weight in pounds
pounds = float(input("Enter the weight in pounds: "))

#name the variable pounds equivalent
pound_eq = 0.454
Convert_to_kg = format(pounds/pound_eq, '.2f')

print('The weight of your item in kilograms is: ',Convert_to_kg)

#this is question two of lesson one

#get the temperature in celcius
Temp_c = float(input("Enter the temperature in degrees Celcius: "))

#name the farenheit conversion variable
F = ((9/5)*Temp_c +32)

print("Your temperature in Farenheit is: ", F)


#question three lesson one

Shares = 500
Bought = 25.04
Bought_Comm = 0.023
ShareCost = (Shares * Bought)
Comm_Paid = (ShareCost*Bought_Comm)
Sold = 36.06
sold_comm = 0.021
ShareSale = (Shares*Sold)
Comm_Sold = (ShareSale*sold_comm)

print("XYZ paid ", ShareCost, "for the shares")
print("XYZ paid ", Comm_Paid, "on the shares they bought")
print("XYZ sold the stock for ", ShareSale)
print("XYZ paid ", Comm_Sold, "commission to the broker who sold the shares")
print("XYZ made ", format((ShareSale - Comm_Sold)-(ShareCost - Comm_Paid), '.2f'), "in stock business")


