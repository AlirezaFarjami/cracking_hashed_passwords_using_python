import hashlib
import csv

password_dict = dict()
for i in range(9999+1):
    password_dict[hashlib.sha256(str(i).encode('utf-8')).hexdigest()] = str(i)

with open ('hashtable.csv', 'r') as file:
    with open ('result_of_cracking.csv', 'w') as file2:
        hash_file = csv.reader(file)
        result_writer = csv.writer(file2)
        for line in hash_file:
            if not line:
                continue
            hash_pw = line[1]
            decrypted_pw = (str(password_dict.get(hash_pw, 'password not found')))
            mytuple = (line[0], line[1] , decrypted_pw)
            result_writer.writerow(mytuple)
