import csv

def writefile(data):
    with open('repositories.csv', "w", encoding='utf-8') as f:
        writer = csv.writer(f)
        for el in data:
            row = list(el.values())
            writer.writerow(row)