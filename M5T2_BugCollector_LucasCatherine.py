#CTI-110
#M5T2-bug collector
#Catherine Lucas
#October 24,2017
#this program calculates the total amount of bugs collected every 7 days.


total = 0

# Enter in the bugs collected for each day.
for day in range (1, 8):
    print("Enter in the amount of bugs collected on day", day)
    bugs = int(input())
    total += bugs

# display the total amount of bugs collected.
print("You've collected a total amount of" , total , "bugs this week.")

