def aes_workflow():
    from Crypto.Cipher import AES
    from Crypto.Random import get_random_bytes
    import base64

    #encrypt
    plaintext = "Text"
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(plaintext.encode())
    combined_ciphertext = base64.b64encode(cipher.nonce + tag + ciphertext).decode()

    #decrypt
    decoded_string = base64.b64decode(combined_ciphertext)
    nonce = decoded_string[:16]
    tag = decoded_string[16:32]
    ciphertext = decoded_string[32:]

    cipher_dec = AES.new(key, AES.MODE_GCM, nonce=nonce)
    decrypted = cipher_dec.decrypt_and_verify(ciphertext, tag)

    plaintext = decrypted.decode() # = Text

    #Description
    #basic Aes encryption and decryption



