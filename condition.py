#Make a program that takes
#inputs like height, width and depth from user and then calculate volume of the cube:
#After calculating volume of cube, compare it with ranges

height=int(input("Enter height"))
width=int(input("Enter width"))
depth=int(input("Enter depth"))

volume = height * width * depth
print("volume is ", volume)

if(volume >= 1 and volume<=10 ):
    print("Extra small")
if (volume >= 11 and volume <= 25):
        print("small")
if(volume >= 26 and volume<=75 ):
    print("Medium")
if(volume >= 76 and volume<=100 ):
    print("Large")
if(volume >= 101 and volume<=250 ):
    print("Extra large")
if(volume>=251):
    print("Extra Extra large")