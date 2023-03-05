#a Python program to print a specified list after removing the 0th, 4th and 5th elements

#SAMPLE LIST

list_tot= ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow', 'Teapink']

list_tot.remove('Red')
list_tot.remove('Pink')
list_tot.remove('Yellow')
list_tot.remove('Teapink')

print("Final Sample list is : ")
print(list_tot)