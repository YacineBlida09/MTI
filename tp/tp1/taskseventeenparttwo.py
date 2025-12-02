student_profile = {
    "name" : "Evie",
    "age" : 22,
    "major" : "Computer Science" ,
    "gpa" : 3.8
}

#Add a new key-value pair "university": "Tech University" to student_profile.
student_profile["university"] = "Tech University"
#student_profile.update({"university": "Tech University"})
print(student_profile)

#Remove the "age" key-value pair from the dictionary.
del student_profile["age"]
#student_profile.pop("age")
print(student_profile)

#Iterate through student_profile and print all keys.
for clef in student_profile:
    print(clef)

#Iterate through student_profile and print all values.
for clef in student_profile:
    print(student_profile[clef])

#Iterate through student_profile and print all key-value pairs.
for clef in student_profile:
    print(str(clef) +' '+ str(student_profile[clef]))
    