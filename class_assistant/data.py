# Function to print input csv line by line
import csv

def print_rows_csv(csv_file):
    with open(csv_file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            print(row)