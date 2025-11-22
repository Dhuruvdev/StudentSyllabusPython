# Program 8: Program to copy content from one file to another

source = open("Data/source.txt", "r")
destination = open("Data/destination.txt", "w")

for line in source:
    destination.write(line)

source.close()
destination.close()

print("File copied successfully!")
