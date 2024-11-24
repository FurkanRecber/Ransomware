import os
from cryptography.fernet import Fernet

secret_key = input("Enter your key: ")

file_list = []

for file in os.listdir():
    if file == "ransom_encrypted.py" or file == "generated.key" or file == "ransom_decrypted.py":
        continue
    if os.path.isfile(file):
        file_list.append(file)

print(file_list)


for file in file_list:
    try:
        with open(file, "rb") as files:
            contents = files.read()
        contents_decrypted = Fernet(secret_key).decrypt(contents)
        with open(file, "wb") as files:
            files.write(contents_decrypted)
        print(f"Successfully decrypted: {file}")
    except Exception as e:
        print(f"Failed to decrypt {file}: {e}")
