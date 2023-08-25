import hashlib
import csv

# Function to generate a dictionary of hashed passwords
def generate_password_dict(limit):
    password_dict = {}
    for i in range(limit + 1):
        # Hash the password and store it as key, with the original password as value
        password_dict[hashlib.sha256(str(i).encode('utf-8')).hexdigest()] = str(i)
    return password_dict

# Function to crack hashed passwords and write results to an output file
def crack_passwords(input_filename, output_filename, password_dict):
    # Open input CSV file for reading and output CSV file for writing
    with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
        # Create CSV reader for input file and CSV writer for output file
        hash_file = csv.reader(infile)
        result_writer = csv.writer(outfile)
        print(type(hash_file))
        print(type(result_writer))
        print(type(infile))
        print(type(outfile))
        
        # Loop through each line (hashed password) in the input CSV
        for line in hash_file:
            if not line:
                continue  # Skip empty lines
            
            # Extract the hashed password from the line
            hash_pw = line[1]
            # Look up the original password in the password dictionary
            decrypted_pw = password_dict.get(hash_pw, 'password not found')
            # Create a tuple with original hash, input hash, and decrypted password
            mytuple = (line[0], line[1], decrypted_pw)
            # Write the tuple to the output CSV file
            result_writer.writerow(mytuple)

# Set the limit for generating passwords
limit = 9999
# Generate the password dictionary
password_dict = generate_password_dict(limit)

# Define input and output filenames
input_filename = 'hashed_passwords.csv'
output_filename = 'result_of_cracking.csv'

# Call the function to crack passwords and write results
crack_passwords(input_filename, output_filename, password_dict)
