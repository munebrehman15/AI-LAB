#Make a program that lists the countries in the set below using a while loop.
#clist =
#["Canada","USA","Mexico"]

#Input list
clist =["Mexico","USA","Canada"]

#Creating variable
count = len(clist)-1

while count >= 0:
    #Printing output
    print(clist[count], end=" ")
    count -= 1