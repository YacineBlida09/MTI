#Create a 1D array (list) called temperatures with values [22.5, 24.1, 23.8, 25.0, 21.9].
temperatures = [22.5, 24.1, 23.8, 25.0, 21.9]

#Iterate through temperatures and print each value.
for temp in temperatures:
    print(temp, end = ',')

#Find and print the maximum temperature.
maxi = max(temperatures)
print(f"\nmax= {maxi}")

#Calculate and print the average temperature.
avg = sum(temperatures)/len(temperatures)
print(f"\navg= {avg}")