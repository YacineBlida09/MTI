student_profile = {
    "name" : "Evie",
    "age" : 22,
    "major" : "Computer Science" ,
    "gpa" : 3.8
}

#Print the entire student_profile dictionary.
print(student_profile)

#Access and print the student's name.
print(student_profile["name"])

#Access and print the student's major.
print(student_profile["major"])

#Try to access a non-existent key and observe the error.
print(student_profile["key"])