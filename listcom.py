#list comprehension which, from a list,
# generates a lowercased version of each string that has length greater than five.

list_total=['AGE','HEIGHT','WEIGHT','GENDER'];

print("Lower case string :", [x.lower() for x in list_total if len(x) > 5])