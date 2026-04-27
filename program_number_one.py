def save_even_and_odd():
# Read numbers from number.txt
    with(open("numbers.txt", "r")) as source_file:
        all_numbers = [int(line.strip()) for line in source_file]