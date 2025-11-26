# Program 18: Count records in DAT file

import pickle

file = open("Data/marks.dat", "rb")
records = pickle.load(file)
file.close()

print("Total records:", len(records))
