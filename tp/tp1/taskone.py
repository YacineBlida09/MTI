#Print "Hello, World !"

print ("Hello, World !")

#Define variables: name, age, job, weight, height

name = ""
age = None
job = ""
weight,height = None, None

#Assign values to variables: name, age, job, weight, height

name, job = "Spiderman", "Superhero"
age, weight, height = 22, 65, 150

#Print the defined variables
print(f"name: {name}, job: {job}, age: {age}, weight: {weight}, height: {height} ")

#Rewrite the same code using : input() function to introduce variable’s values, and print() to display them

name, job, age, weight, height = input("Donner: name, job, age, weight, height en cet ordre separes par ',':\n").split(',')

age, weight, height = int(age), float(weight), float(height)

print(f"name: {name}, job: {job}, age: {age}, weight: {weight}, height: {height} ")
