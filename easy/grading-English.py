def gradingStudents(grades):
    for i, grade in enumerate(grades):
        if grade < 38:
            continue
        next_multiple_5 = grade - (grade % 5) + 5
        if (next_multiple_5 - grade) < 3:
            grades[i] = next_multiple_5
    return grades

