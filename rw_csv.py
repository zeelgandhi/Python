import csv
with open("data.csv", "w+") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Column1", "Column2"])
    writer.writerow(["Column1", "Column2"])




with open("data.csv", "a") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["data1", "data2"])

with open("data.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)