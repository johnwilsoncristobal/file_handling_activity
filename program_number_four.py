# Read integers from integers.txt
with (open("./integers.txt", "r")) as source_file:
    numbers = [int(line.strip()) for line in source_file]
# Write squares of even numbers to double.txt
with (open("double.txt", "w")) as double_file:
    for num in numbers:
        if num % 2 == 0:
            double_file.write(str(num ** 2) + "\n")
# Write cubes of odd numbers to triple.txt
with (open("triple.txt", "w")) as triple_file:
    for num in numbers:
        if num % 2 != 0:
            triple_file.write(str(num ** 3) + "\n")