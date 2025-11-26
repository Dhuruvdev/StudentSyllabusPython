# Program 1: Read a text file and display each word separated by #

file = open("Data/sample.txt", "r")
for line in file:
    words = line.split()
    for word in words:
        print(word, end="#")
    print()
file.close()
