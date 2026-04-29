# Read integers from integers.txt
with (open("integers.txt", "r")) as source_file:
    numbers = [int(line.strip()) for line in source_file]