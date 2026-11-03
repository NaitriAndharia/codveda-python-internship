
import os

# Get the folder location
folder = os.path.dirname(os.path.abspath(__file__))
print("Folder Location:", folder)
print("Files Available:", os.listdir(folder))

input_file = os.path.join(folder, "sample.txt")
encrypted_file = os.path.join(folder, "encrypted.txt")
decrypted_file = os.path.join(folder, "decrypted.txt")


# Encryption Function
def encrypt(text):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 + 3) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + 3) % 26 + 97)
        else:
            result += char

    return result


# Decryption Function
def decrypt(text):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 - 3) % 26 + 65)
            else:
                result += chr((ord(char) - 97 - 3) % 26 + 97)
        else:
            result += char

    return result


# Main Program
try:
    # Read original file
    with open(input_file, "r", encoding="utf-8") as file:
        original_text = file.read()

    # Encrypt the text
    encrypted_text = encrypt(original_text)

    # Save encrypted text
    with open(encrypted_file, "w", encoding="utf-8") as file:
        file.write(encrypted_text)

    # Decrypt the text
    decrypted_text = decrypt(encrypted_text)

    # Save decrypted text
    with open(decrypted_file, "w", encoding="utf-8") as file:
        file.write(decrypted_text)

    print("File Encrypted Successfully!")
    print("Encrypted file saved as: encrypted.txt")

    print("File Decrypted Successfully!")
    print("Decrypted file saved as: decrypted.txt")

except FileNotFoundError:
    print("Error: sample.txt file not found!")

except Exception as e:
    print("An error occurred:", e)
