from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def encrypt_string(plaintext: str, key: bytes):
    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(plaintext.encode())
    return base64.b64encode(cipher.nonce + tag + ciphertext).decode()

def decrypt_string(cyphertext: str, key:bytes):
    decoded_string = base64.b64decode(cyphertext)
    nonce = decoded_string[:16]
    tag = decoded_string[16:32]
    ciphertext = decoded_string[32:]

    cipher_dec = AES.new(key, AES.MODE_GCM, nonce=nonce)
    decrypted = cipher_dec.decrypt_and_verify(ciphertext, tag)
    return base64.b64encode(decrypted).decode()

def main():
    print("Welcome to AES encryption and decryption!")
    is_finished = False

    while not is_finished:
        message = "\nChoose an option:\n"
        message += "1 - Encrypt\n2 - Decrypt\nq - Quit"
        print(message)
        decision = input("Enter your choice: ")

        match decision:
            case "1":
                invoke_encryption()
                is_finished = False if input("Encrypt another message? (y/n): ").lower() == "y" else True
            case "2":
                invoke_decryption()
                is_finished = False if input("Encrypt another message? (y/n): ").lower() == "y" else True
            case "q":
                return
            case _:
                print("Invalid choice!")

def invoke_encryption():
    plaintext = input("\nEnter your message: ")
    key = get_random_bytes(16)
    encoded_key = base64.b64encode(key).decode()
    encrypted_string = encrypt_string(plaintext, key)
    print(f"This is the generated key. Store it somewhere safe:\n{encoded_key}")
    print(f"This is the encrypted message:\n{encrypted_string}")

def invoke_decryption():
    cyphertext = input("\nEnter your encrypted message: ")
    encoded_key = input("\nEnter your key: ")
    decoded_key = base64.b64decode(encoded_key)
    decrypted_string = decrypt_string(cyphertext, decoded_key)
    ascii_string = base64.b64decode(decrypted_string).decode()
    print(f"This is the decrypted message:\n{ascii_string}")

main()





