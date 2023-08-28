import hashlib
import csv

def generate_password_dict(limit):
    # Create an empty dictionary to store hashed passwords and their corresponding plaintext values
    password_dict = {}
    for i in range(limit + 1):
        # Hash the integer value using SHA-256 and store it in the dictionary with the plaintext value as the key
        password_dict[hashlib.sha256(str(i).encode('utf-8')).hexdigest()] = str(i)
    return password_dict

def crack_passwords(input_filename, output_filename, password_dict):
    # Open the input and output files for processing
    with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
        hash_file = csv.reader(infile)  # Create a CSV reader for the input file
        result_writer = csv.writer(outfile)  # Create a CSV writer for the output file
        for line in hash_file:
            if not line:
                continue  # Skip empty lines
            hash_pw = line[1]  # Extract the hashed password from the current line
            # Attempt to find the corresponding plaintext password in the password dictionary
            decrypted_pw = password_dict.get(hash_pw, 'password not found')
            mytuple = (line[0], decrypted_pw)  # Create a tuple with the original input and decrypted password
            result_writer.writerow(mytuple)  # Write the tuple to the output file

# Define the limit for password generation
limit = 9999
# Generate the password dictionary
password_dict = generate_password_dict(limit)

# Specify input and output filenames
input_filename = 'hashed_passwords.csv'
output_filename = 'result_of_cracking.csv'

# Call the function to crack passwords and store results in the output file
crack_passwords(input_filename, output_filename, password_dict)
