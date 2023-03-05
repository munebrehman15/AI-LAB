#You have collected information about cities in your province. You decide to store each city’s
#name, population, and mayor in a file. Write a python program to accept the data for a number
#of
#cities from the keyboard and store the data in a file in the order in which they’re entered.
f = open("cityfile.txt", "w+")
userinputc=str(input("Enter city's name"))
userinputp=str(input("Enter population"))
userinputm=str(input("Enter mayor"))
f.write(userinputc)
f.write(userinputp)
f.write(userinputm)
f.close()
