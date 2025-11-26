# Program 2: Count vowels and consonants in a text file

file = open("Data/sample.txt", "r")
vowels = 0
consonants = 0

for line in file:
    for ch in line:
        if ch.isalpha():
            if ch in "aeiouAEIOU":
                vowels += 1
            else:
                consonants += 1

file.close()
print("Vowels:", vowels)
print("Consonants:", consonants)
