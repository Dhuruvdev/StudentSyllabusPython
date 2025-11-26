# Program 8: Copy file contents from one file to another

source = open("Data/source.txt", "r")
dest = open("Data/destination.txt", "w")

for line in source:
    dest.write(line)

source.close()
dest.close()
print("File copied!")
