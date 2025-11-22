# Program 3: Remove all lines containing the character ',' and write remaining lines to another file

file1 = open("Data/input.txt", "r")
file2 = open("Data/output.txt", "w")

for line in file1:
    if ',' not in line:
        file2.write(line)

file1.close()
file2.close()

print("Lines without comma have been written to output.txt")
