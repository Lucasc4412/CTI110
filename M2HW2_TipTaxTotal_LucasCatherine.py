 #CTI-110
 #M2HW2-Tip Tax Total
 #Catherine Lucas
 #September 19,2017
 #This program calculates the total cost of a meal purchased at a restaurant.

 #Declare the variables.

foodCost = float(input('Enter the charge for the food: $'))
tipAmount = foodCost * 0.18
salesTax = foodCost * 0.07
totalCost = foodCost + tipAmount + salesTax

 #Display total tip amount.
 
print('Tip: $',format(tipAmount,',.2f'))

 #Display total sales tax.

print('Tax: $',format(salesTax,',.2f'))

 #Display total cost of restaurant bill.

print('Total: $',format(totalCost,',.2f'))
