import csv

with open('unemployment_data_us.csv') as unempdata:
    for row in unempdata:
        print(row)