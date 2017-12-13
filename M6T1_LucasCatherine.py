#CTI-110
#M6T1: Kilometer Coverter
#Catherine Lucas
#November 14,2017
#This program converts kilometers to miles.
 
CONVERSION_FACTOR = 0.6214
# The main function gets a distance in kilometers and calls
# the show_miles function to convert it.
def main():
    #Get the distance in kilometers.
    kilometers = float(input('Enter a distance in kilometers:'))

    # Display the distance converted into miles.
    show_miles(kilometers)
#The show_miles function coverts the parameter km from
#kilometers to miles and displays the result.

def show_miles(km):
    # Calculate miles
    miles = km * CONVERSION_FACTOR

    # Display the miles.
    print(km,'Kilometers is equal to', miles,'miles.')

#Call the main function
main()
main()


