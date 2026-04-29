with open("./mylife.txt", "w") as life_file:
# Ask for first line
    line = input("Enter line: ")
    life_file.write(line + "\n")