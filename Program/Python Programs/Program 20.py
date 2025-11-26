# Program 20: Merge two text files

file1 = open("Data/file1.txt", "r")
file2 = open("Data/file2.txt", "r")
file3 = open("Data/merged.txt", "w")

file3.write(file1.read())
file3.write(file2.read())

file1.close()
file2.close()
file3.close()

print("Files merged!")
