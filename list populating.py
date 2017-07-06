import csv

with open('compounds.csv', 'r') as f:
    reader = csv.reader(f)
    your_list = list(reader)

print (your_list)