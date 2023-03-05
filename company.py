#If the time taken by the worker is input through the keyboard,find the
#efficiency of the worker of given data

time_taken = float(input("input the time taken for the company"))

if(time_taken>=2 and time_taken<=3):
    print("Worker is effiecient")
if(time_taken>3 and time_taken<=4):
    print("improve speed")
if(time_taken>4 and time_taken<=5):
    print("you need training")
if(time_taken>5):
    print("please leave")