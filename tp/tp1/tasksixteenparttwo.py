person_info = ("Alice", 30, "New York")

#Unpack person_info into three variables: name, age, city. Print each variable.
name, age, city = person_info
print(f"name: {name}, age:{age}, city: {city}")

#Create a function get_min_max(numbers) that takes a list of numbers and returns a tuple containing the minimum and maximum values. Test it with [5, 1, 9, 2, 7].
def get_min_max(numbers):
    return (min(numbers), max(numbers))

print(get_min_max([1, 2, 3]))
