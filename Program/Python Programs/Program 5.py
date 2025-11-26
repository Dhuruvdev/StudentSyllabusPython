# Program 5: Read and write data to a DAT file

import pickle

records = [{"roll": 1, "name": "Aman", "marks": 85}, {"roll": 2, "name": "Sonia", "marks": 90}]

file = open("Data/marks.dat", "wb")
pickle.dump(records, file)
file.close()
print("File created!")

file = open("Data/marks.dat", "rb")
data = pickle.load(file)
file.close()

for record in data:
    print(record)
