import hashlib
import csv

def hash_password_hack(input_file_name, output_file_name):
    rainbow = {}
    for i in range(10000):
       code = str(i).zfill(4)
       hashed_code = hashlib.sha256(code.encode('utf-8')).hexdigest()
       rainbow[hashed_code] = code

    rows = []
    with open(input_file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)

    with open(output_file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        for row in rows:
            writer.writerow([row[0], rainbow[row[1]]])

hash_password_hack('hashed_passwords.csv', 'encoded_passwords.csv')