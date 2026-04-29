# Open student.txt and read all lines
with (open("./students.txt", "r")) as source_file:
    records = [line.strip().split() for line in source_file]
# Convert the records into tuple
    students = [(name, float(gwa)) for name, gwa in records]
# Find the student with the highest GWA
    highest_student = max(students, key=lambda x: x[1])
# Print the result
    print("Highest GWA:", highest_student[0], highest_student[1])