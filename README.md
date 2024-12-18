# Project: Simple Ransomware Simulation

This project is a Python application that simulates file encryption and decryption processes, emulating basic ransomware functionality. The project focuses on encrypting certain files and decrypting them later using a specific key. It utilizes the `cryptography` library to ensure secure and modern encryption.

## Use Case
This project is designed for individuals interested in cybersecurity, developers aiming to understand the logic behind ransomware, and security researchers. It provides a basic example of encryption and decryption processes, serving as a learning tool for anyone interested in encryption mechanics and basic ransomware functionality. 

Awareness of the threats posed by ransomware in real-world scenarios can be heightened by studying projects like this. However, the intent of this project is not to create vulnerabilities or cause harm but rather to educate on how such software works.

## Files and Their Functions

### ransom_encrypted.py (File Encryption)
This file encrypts specific files in the current directory using a `Fernet` key and sends the key to the user’s provided email address. The program focuses on securely encrypting files so that they can only be accessed with a secret key.

- **Command Line Usage**:
    ```bash
    python ransom_encrypted.py -e "your_email@gmail.com" -p "your_password"
    ```
  - `-e` parameter: Specifies the email address.
  - `-p` parameter: Specifies the email password (works with SMTP-supported services like Gmail).

- **Encryption Process**:
  - When the program is run, it sends the encryption key to the specified email address.
  - This key is then used to encrypt files in the directory, and each file listed in `file_list` will be encrypted. The `ransom_encrypted.py` and `ransom_decrypted.py` files are excluded from this process to avoid self-encryption.

### ransom_decrypted.py (File Decryption)
This file is used to decrypt files that were encrypted by `ransom_encrypted.py`. It prompts the user to enter the encryption key and then decrypts all encrypted files in the current directory.

- **Command Line Usage**:
    ```bash
    python ransom_decrypted.py
    ```
  - When run, the program prompts the user to enter the encryption key.
  - If the correct key is provided, the encrypted files are decrypted and returned to their original state.
  
- **Decryption Process**:
  - The user enters the previously sent encryption key.
  - If the correct key is entered, the files listed in `file_list` are unlocked.
  - Successfully decrypted files will return to their original content.

## Setup and Requirements
To use this project, follow these steps:
1. Install the `cryptography` library:
    ```bash
    pip install cryptography
    ```
2. Python 3.6 or above is recommended for compatibility.

## Warnings and Important Notes

- **Cybersecurity and Legal Warning**: This project is intended for educational purposes only. The ransomware simulation is designed to promote cybersecurity awareness. Using this tool for unauthorized purposes or outside of controlled environments can have legal consequences. Unauthorized or illegal usage is strictly discouraged and is the responsibility of the user.

- **Protect Your Security**: For the program to send emails, you may need to enable “allow less secure apps” for your Gmail or email account. Note that enabling this option may reduce your account's security. Use a test email account if necessary.

- **Avoid Using on Real Data**: This project is intended solely as a simulation. It should not be used on sensitive or personal data. Only use test files for encryption.

- **Create Backups**: Encrypting files may lead to irreversible data loss. Ensure you have backups of any important files before running this project.

- **SMTP Security**: Since the program sends the encryption key via email, Gmail or similar SMTP servers are used. For security reasons, using only a trusted test account for this is recommended.

## Disclaimer
This project is provided solely as an educational simulation example. The user is responsible for any unauthorized or illegal actions. The project developer is not liable for any consequences arising from misuse or illegal activities.

**Note**: This project aims to raise awareness of ransomware and its impact. It should only be used in professional and controlled educational environments.
