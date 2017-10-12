# CTI-110 
# M3HW1 - Age Classifier 
# Catherine Lucas 
# 10/05/17
# This program determines whether the person is an infant, a child, a teenager, or an adult.


def main():

    age = float(input("Enter a person's age: "))

    if age <= 1:
        print('This person is an infant')
    else:

        if age <= 12:
            print('This person is a child')
        else:

            if age < 20:
                print('This peron is a teenager')
            else:
               
                if age < 55:
                   print('This person is an adult')
                else:

                    if age >= 55:
                       print('This person is old')
          

               
main()
main()
main()
main()
main()
