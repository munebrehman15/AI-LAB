#Write a python program to create a data file student.txt and append the message “Now we are
#AI students”s
f = open("student.txt", "a")
f.write("Now we are AI students")
f.close()