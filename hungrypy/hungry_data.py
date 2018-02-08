import csv

def get_length(file_path):
    return 1
   
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
append_data("data.csv", "Zeel", "zeelphysics@gmai")