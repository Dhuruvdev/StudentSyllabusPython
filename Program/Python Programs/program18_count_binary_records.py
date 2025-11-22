# Program 18: Count number of records in binary file

import pickle

file = open("Data/marks.dat", "rb")
records = pickle.load(file)
file.close()

count = len(records)
print("Number of records in binary file:", count)
