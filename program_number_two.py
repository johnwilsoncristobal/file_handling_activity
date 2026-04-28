# Open student.txt and read all lines
with open("./students.txt", "r") as source_file:
    records = [line.strip().split() for line in source_file]