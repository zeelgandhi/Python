import csv
import datetime
import shutil
from tempfile import NamedTemporaryFile


def get_length(file_path):
    with open("data.csv") as csvfile:
        reader = csv.reader(csvfile)
        reader_list = list(reader)
        # print(len(reader_list))
        return len(reader_list)

def append_data(file_path, name, email, amount):
    fieldnames = ['id', 'name', 'email', 'amount', 'sent', 'date']
    # the num of rows?
    next_id = get_length(file_path)
    with open(file_path, "a") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({
            "id": next_id,
            "name": name,
            "email": email,
            "amount": amount,
            "sent": "",
            "date": datetime.datetime.now()
        })

#append_data()
#append_data("data.csv", "Zeel", "zeelphysics@gmail.com", 145)


filename = "data.csv"
temp_file = NamedTemporaryFile(delete=False)

with open(filename, "rb") as csvfile, temp_file:
    reader = csv.DictReader(csvfile)
    fieldnames =  ['id', 'name', 'email', 'amount', 'sent', 'date']
   # print(fieldnames)
    writer = csv.DictWriter(temp_file, fieldnames= fieldnames)
    #writer.writeheader()
   #writer.writerow({"id": 123,"name": "new title","email":"tesst","amount":123,"sent":True,"date":datetime.datetime.now})
    for row in reader:
        if row[b'id'] == 4:
            row[b'sent'] = True
            #print(row)
        writer.writerow(row)

    shutil.move(temp_file.fieldnames.name, filename)
