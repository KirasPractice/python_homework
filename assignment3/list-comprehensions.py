import csv


rows = []
with open("assignment3/employees.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        rows.append(row)

    full_name = [ row[0] + " " + row[1] for row in rows[1:]]
    print(full_name)
    
    e_names = [ name for name in full_name if "e" in name]
    print(e_names)
