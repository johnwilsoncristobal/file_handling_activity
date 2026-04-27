def save_even_and_odd():
# Read numbers from number.txt
    with(open("./numbers.txt", "r")) as source_file:
        all_numbers = [int(line.strip()) for line in source_file]      
# Write the even numbers
    with open("even_numbers.txt", "w") as even_file:
        for number in all_numbers:
            if number % 2 == 0:
                even_file.write(str(number) + "\n")
#Write the odd numbers
    with open("odd_numbers.txt", "w") as odd_file:
        for number in all_numbers:
            if number % 2 != 0:
                odd_file.write(str(number) + "\n")
# Run the function
save_even_and_odd()