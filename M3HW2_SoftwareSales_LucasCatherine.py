# CTI-110
# M3HW - Software Sales
# Catherine Lucas
# 10/10/17
# This program calculates bulk discount.


def main():

    # Ask the user to enter in the number of packages purchased.

    package = float(input('Enter the number of packages purchased:'))

    # declare the constant variables. The price will always be $99.00.

    PRICE = 99

    # 10 % off 
    cost = package * PRICE
    discount1 = cost * .10
    total1 = cost - discount1
    save1 = cost - total1

    # 20 % off
    discount2 = cost * .20
    total2 = cost - discount2
    save2 = cost - total2

    #30 % off
    discount3 = cost * .30
    total3 = cost - discount3
    save3 = cost - total3

    #40 % off
    discount4 = cost * .40
    total4 = cost - discount4
    save4 = cost - total4

    
    if package <=0:
        print("ERROR")
    else:
        
        if package <=9:
            print("Purchase 10 or more packages to get a 10%-40% off discount!")
            print('Total: $',format(cost,'.2f'))
        else:                          
        
            if package <=19:
                print('Discount: 10% off')
                print('Total: $',format(total1,'.2f'))
                print('You Saved: $',format(save1,'.2f'))

            else:

                if package <=49:
                    print('Discount: 20% off')
                    print('Total: $',format(total2,'.2f'))
                    print('You Saved: $',format(save2,'.2f'))

                else:

                    if package <=99:
                        print('Discount: 30% off')
                        print('Total: $',format(total3,'.2f'))
                        print('You Saved: $',format(save3,'.2f'))
                    
                    else:

                        if package >= 100:
                            print('Discount: 40% off')
                            print('Total: $',format(total4,'.2f'))
                            print('You Saved: $',format(save3,'.2f'))

                        

main()
main()
main()
main()
main()
main()
                
            

