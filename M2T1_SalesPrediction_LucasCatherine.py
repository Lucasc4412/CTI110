# CTI-110
# M2T1-Sales Prediction
# Catherine Lucas
# September 9,2017
# This program calculates total projected sales.

# Get the projected total sales.
total_sales = float(input('Enter the projected sales: '))

# Calculate the profit as 23 percent of total sales.
profit = total_sales * 0.23

#Display the profit.
print('The profit is $', format(profit, ',.2f'))
