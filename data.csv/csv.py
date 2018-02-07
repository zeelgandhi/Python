import csv
with open("date.csv", "w+") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Title","Description"])
    writer.writerow(["Row1", "Some descr."])
    
    



