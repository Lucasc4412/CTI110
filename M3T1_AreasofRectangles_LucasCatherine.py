# CTI-110
# M3T1: Areas of rectangles
# Catherine Lucas
# September 21,2017
# This program calculates the area of a rectangle.


# Get the length and the width of rectangle 1.

length1 = int(input('Enter the length of rectangle 1: '))
width1 = int(input('Enter the width ot rectangle 1: '))

#Get the length and width of rectangle 2.

length2 = int(input('Enter the length of rectangle 2: '))
width2 = int(input('Enter the width of rectangle 2: '))

# Calculate the area of rectangle 1.
area1 = length1 * width1


#Calculate the area of rectangle 2.
area2 = length2 * width2


#Determine which triangle has the greater area.

if area1 > area2:

    print('Rectangle 1 has the greatest area.')

elif area2 > area1:

    print('Rectangle 2 has the greatest area.')

else:
    print('Both rectangles have the same area.')

