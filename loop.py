#1. Create a loop that counts from 0 to 100
#2. Make a multiplication table using a loop
#3. Output the numbers 1 to 10 backwards using a loop
#4. Create a loop that counts all even numbers to 10
#5. Create a loop that sums the numbers from 100 to 200

#1
for x in range(0, 11, 1):
    print(x)
#2
num = int(input("Display multiplication table of? "))

# Iterate 10 times from i = 1 to 10
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)

#3
num1=10
for num1 in reversed(range(num1 + 1)) :
    print (num1)

#4
for x in range(0, 11, 2):
     print(x)
#5
sum=0
for x in range(100, 201, 1):
    sum=sum+x
print(sum)