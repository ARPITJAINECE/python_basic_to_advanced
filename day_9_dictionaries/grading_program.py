student_scores = {"Harry": 88, "Ron": 78, "Hermione": 95, "Draco": 75, "Neville": 60}

# student_grades =

for student, score in student_scores.items():
    if 91 <= score <= 100:
        grade = "Outstanding"
    elif 81 <= score <= 90:
        grade = "Exceeds Expectations"
    elif 71 <= score <= 80:
        grade = "Acceptable"
    else:
        grade = "Fail"

    print(f"{student}: {grade}")
