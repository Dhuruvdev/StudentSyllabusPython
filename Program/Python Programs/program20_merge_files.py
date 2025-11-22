# Program 20: Merge contents of two text files into one

file1 = open("Data/file1.txt", "r")
file2 = open("Data/file2.txt", "r")
file3 = open("Data/merged.txt", "w")

for line in file1:
    file3.write(line)

for line in file2:
    file3.write(line)

file1.close()
file2.close()
file3.close()

print("Files merged successfully!")
