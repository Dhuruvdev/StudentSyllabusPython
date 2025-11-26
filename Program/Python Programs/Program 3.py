# Program 3: Remove lines with commas and save to new file

file1 = open("Data/input.txt", "r")
file2 = open("Data/output.txt", "w")

for line in file1:
    if ',' not in line:
        file2.write(line)

file1.close()
file2.close()
print("Done! Lines without commas saved to output.txt")
