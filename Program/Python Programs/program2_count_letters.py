# Program 2: Count vowels, consonants, uppercase and lowercase letters in a text file

file = open("Sample_Data/sample.txt", "r")

vowels = 0
consonants = 0
uppercase = 0
lowercase = 0

for line in file:
    for ch in line:
        if ch.isalpha():
            if ch in "aeiouAEIOU":
                vowels = vowels + 1
            else:
                consonants = consonants + 1
            
            if ch.isupper():
                uppercase = uppercase + 1
            else:
                lowercase = lowercase + 1

file.close()

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)
