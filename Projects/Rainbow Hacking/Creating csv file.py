import csv
import hashlib


# Function to hash a password using SHA-256
def hash_password(password):
    hash_object = hashlib.sha256(password.encode('utf-8'))
    return hash_object.hexdigest()


# Define names and their passwords
names_and_passwords = {
    "Alice": "1234",
    "Bob": "5678",
    "Charlie": "9101",
    "Diana": "1213"
}

# File to write the CSV data
file_name = "hashed_passwords.csv"

# Write names and hashed passwords to the CSV file
with open(file_name, mode="w", newline="") as file:
    writer = csv.writer(file)

    # Write names and their corresponding password hashes
    for name, password in names_and_passwords.items():
        hashed_password = hash_password(password)
        writer.writerow([name, hashed_password])