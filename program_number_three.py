# Open or Create the file mylife.txt in write"
with (open("./mylife.txt", "w")) as life_file:
# Ask for first line
    line = input("Enter line: ")
    life_file.write(line + "\n")
# Loop until it says no
    while True:
        choice = input("Are there more lines y/n? ")
        if choice.lower() == "y":
            line = input("Enter line: ")
            life_file.write(line + "\n")
        else:
            break