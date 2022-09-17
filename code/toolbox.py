
import csv

# Read saved files and return 2D list
def csv_reader(filepath,delimiter=','):
    table = []
    with open(filepath, newline='') as file:
        rows = csv.reader(file, delimiter=delimiter)
        for row in rows:
            table.append(row)
            
    return table
