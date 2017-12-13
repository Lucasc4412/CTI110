#This program converts Feet to Inches.
#November 16,2017
#CTI-110 M6T2_FeetToInches
#Catherine Lucas

# constant variable one foot equals twelve inches.
INCHES_PER_FOOT = 12

# main function displays the answer.
def main():
    feet = int(input('Enter in a number of feet:'))

    print(feet,'ft. is equal to',feet_to_inches(feet), 'inches.')

# feet_to_inches function converts feet to inches.
def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT

# call the main function

main()
main()





  
