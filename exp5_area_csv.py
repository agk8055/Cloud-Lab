import csv

rows_to_write = []

with open("area.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        length = int(row[0])
        breadth = int(row[1])
        area = length * breadth
        rows_to_write.append([length, breadth, area])

with open("newarea.csv", 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Length", "Breadth", "Area"])
    writer.writerows(rows_to_write)

print("File 'newarea.csv' has been created successfully!")