# CTI-110 
# M6HW1-TestGradingProgram 
# Catherine Lucas 
# 10/05/17
# This program calculates average and letter grade.

def main():
    score = float(input("Enter in a score:"))
    score2 = float(input("Enter in a score:"))
    score3 = float(input("Enter in a score:"))
    score4 = float(input("Enter in a score:"))
    score5 = float(input("Enter in a score:"))
    average = calc_average(score,score2,score3,score4,score5)
    determine_grade(average)
        
def calc_average(score,score2,score3,score4,score5):
    average = (score+score2+score3+score4+score5)/5
    return average

def determine_grade(average):
    # system uses 10-point grading scale
    A_score = 90
    
    B_score = 80

    C_score = 70

    D_score = 60
    
    print("your average is",average)

    if average >= A_score:
        print('Your grade is: A')
   
    elif average >= B_score:
        print('Your grade is: B')

    elif average >= C_score:
        print('Your grade is: C')

    elif average >= D_score:
        print('Your grade is: D')

    else:
        print('Your grade is: F') 

main()

