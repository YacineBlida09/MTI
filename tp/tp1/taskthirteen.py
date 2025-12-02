data_points = [10, 15, 20, 25, 30, 35]
#Calculate the sum of all data points.
somme = sum(data_points)
print(somme)

#Count how many data points are greater than 20
cpt = 0
for pt in data_points:
    if pt > 20: cpt += 1
print(f"nbr de pts sup a 20 est: {cpt}")