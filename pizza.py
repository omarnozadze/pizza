from tabulate import tabulate
import csv
import sys

try:
    if len(sys.argv) == 1:
        print("Too few command-line arguments")
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
    else:    
        with open ("regular.csv") as csvfile:
            rows = csv.reader(csvfile, )
            date = []
            for row in rows:
                date.append(row)
        print (tabulate(date, headers="firstrow",tablefmt = "psql"))        
except FileNotFoundError:
    sys.exit("File does not exist")



