import csv
import shutil
from tempfile import NamedTemporaryFile


def get_length(file_path):
    with open ("data.csv") as csvfile:
        reader = csv.reader(csvfile)
        reader_list = list(reader)
        #print(reader_list)
        return len(reader_list)
   
def append_data(file_path, name, email):
    fieldnames = ['id', 'name', 'email']
    #the num of rows?
    next_id= get_length(file_path)
    with open(file_path, "a") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        #writer.writeheader()
        writer.writerow({
            "id": next_id,
            "name": name,
            "email": email
        })
#append_data("data.csv", "Zeel", "zeelphysics@gmai")

filename = "data.csv"
temp_file = NamedTemporaryFile(delete = False)

with open(filename, "rb") as csvfile, temp_file:
    reader = csv.DictReader(csvfile)
    fieldnames = ["id", "name", "email", "amount", "sent"]
    writer = csv.DictWriter(temp_file, fieldnames = fieldnames)
    writer.writeheader()

    for row in reader:
        print(row)
        writer.writerow({
            "id": row["id"],
            "name": row["id"],
            "email": row["email"],
            "amount": 14000,
            "sent": "",
        })
shutil.move(temp_file.name, filename)