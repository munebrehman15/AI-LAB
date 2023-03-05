#a Python script to concatenate following dictionaries to create a new one.

#sample dictonary

dict1={1:10, 2:20}
dict2={3:30, 4:40}
dict3={5:50,6:60}


dict2.update(dict3)
dict1.update(dict2)
print("Total dict :",dict1)