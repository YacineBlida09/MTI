student_scores = [85, 92, 78, 95, 88]
#Ask the user to enter a score to search for. If found, print its index; otherwise, print the message "Score not found."
score = int(input("Donner une note a rechercher: "))
if score in student_scores:
    print(student_scores.index(score)+1)
else:
    print("existe pas")

#Update the score of the third student (index 2) to 80. Print the updated student_scores.
student_scores[2] = 80
print(student_scores)