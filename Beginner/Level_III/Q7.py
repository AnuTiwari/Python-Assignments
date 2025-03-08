def create_student_subject_dict():
    num_students = int(input("Enter the number of students: "))

    students = []
    subjects = []

    # Taking input for students
    for i in range(num_students):
        student = input(f"Enter name of student {i+1}: ")
        students.append(student)

    # Taking input for subjects
    for i in range(num_students):
        subject = input(f"Enter subject for {students[i]}: ")
        subjects.append(subject)

    # Creating dictionary using dictionary comprehension
    student_dict = {students[i]: subjects[i] for i in range(num_students)}

    return student_dict

def main():
    student_subject_dict = create_student_subject_dict()
    
    # Displaying the dictionary
    print("\nStudent-Subject Mapping:")
    for student, subject in student_subject_dict.items():
        print(f"{student}: {subject}")

if __name__ == "__main__":
    main()
