import csv
with open("data.csv", "w+") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Column1", "Column2"])
    writer.writerow(["data1", "data2"])

with open("data.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

with open("data.csv", "a") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["data3", "data4"])

with open("data.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)

with open("data.csv", "a") as csvfile:
    fieldnames = ["Column1", "Column2"]
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writerow({"Column1": 123, "Column2": "new title"})
