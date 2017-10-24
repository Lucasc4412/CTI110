#CTI-110
#M5HW1-distance traveled
#Catherine Lucas
#October 24,2017
#This program calculate the total distance traveled.

def dist():
    speed = int(input("What is the speed of the vehicle in mph?:"))

    time = int(input("How many hours has it traveled?:"))
    print("Hour" ,'\t', "Distance Traveled")
    print("--------------------------------")
    for currentTime in range(1,time+1):
        distance = speed*currentTime
        print(currentTime,'\t',distance)

dist()
dist()

    
