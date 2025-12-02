#Create a list called fruits containing "apple", "banana", "cherry", "date", "orange", "mango", "pears".
fruits = ["apple", "banana", "cherry", "date", "orange", "mango", "pears"]

#Print the entire fruits list.
for fruit in fruits:
    print(fruit, end = ', \n')

#Access and print the first element.
print(fruits[0])

#Access and print the last element.
print(fruits[-1])

#Access and print "orange" using its index.
print(fruits[4])

#Try to access an element at an invalid index and observe the error
print(fruits[100])