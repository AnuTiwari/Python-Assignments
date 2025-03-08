subjects = ["Physics", "Chemistry", "Biology", "Mathematics", "Computer"]
marks = [int(input(f"Enter marks for {sub}: ")) for sub in subjects]

percentage = sum(marks) / 5

if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
elif percentage >= 40:
    grade = "E"
else:
    grade = "F"

print(f"Percentage: {percentage}% | Grade: {grade}")
