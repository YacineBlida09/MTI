small_numbers = [10, 20, 30, 40, 50]

#Change the value of the second element to 25.
small_numbers[1] = 25
print(small_numbers)

#Add 60 to the end of the list.
small_numbers += [60] #small_numbers.append(60)
print(small_numbers)

#Insert 5 at the beginning of the list.
small_numbers.insert(0, 5)
print(small_numbers)

#Remove 30 from the list.
small_numbers.remove(30)
print(small_numbers)

large_numbers = [100, 200, 300, 400, 500]

#Concatenate small_numbers and large_numbers into a new list combined_list. Print it.
combined_list = small_numbers + large_numbers
print(combined_list)

#Check if 30 is present in combined_list. Print the boolean result.
for num in combined_list:
    if num == 30:
        print("Existe")
        break
else: 
    print("N'existe pas")

#Find the length of combined_list.
print(len(combined_list))

#Sort combined_list in descending order. Print it.
#combined_list.sort(reverse = True)

sorted_list = sorted(combined_list, reverse=True)
print(sorted_list)
