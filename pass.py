#The program must prompt the user for a username and password. The program should
#compare the password given by the user to a known password.

password1 = 'UBIT'
password2 = str(input("Enter password please"))
if(password1 == password2):
    print("welcome")
else:
    print("I dont't know you")