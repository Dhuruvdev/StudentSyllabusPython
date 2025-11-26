# DAT File Reader Utility - Simple tool to read DAT files created with pickle

import pickle
import sys

def read_dat_file(filename):
    try:
        file = open(filename, "rb")
        data = pickle.load(file)
        file.close()
        return data
    except FileNotFoundError:
        print("Error: File not found -", filename)
        return None
    except Exception as e:
        print("Error reading file:", e)
        return None

def display_data(data):
    if data is None:
        return
    
    if isinstance(data, list):
        print(f"\nTotal records: {len(data)}\n")
        for i, record in enumerate(data, 1):
            print(f"Record {i}:")
            if isinstance(record, dict):
                for key, value in record.items():
                    print(f"  {key}: {value}")
            else:
                print(f"  {record}")
            print()
    else:
        print("Data:", data)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python read_dat_file.py <filename.dat>")
        print("Example: python read_dat_file.py Data/students.dat")
    else:
        filename = sys.argv[1]
        data = read_dat_file(filename)
        display_data(data)
