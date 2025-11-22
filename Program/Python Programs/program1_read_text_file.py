# Program 1: Read a text file line by line and display each word separated by #

file = open("Sample_Data/sample.txt", "r")
for line in file:
    words = line.split()
    for word in words:
        print(word, end="#")
    print()
file.close()
