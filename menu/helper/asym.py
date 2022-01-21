import rsa

publicKeyRsa, privateKeyRsa = rsa.newkeys(512)


def encrypt_rsa(message):
    crypted_message: bytes = rsa.encrypt(message.encode(), publicKeyRsa)
    print(crypted_message.hex())


def decrypt_rsa(message):
    decrypted_message: bytes = rsa.decrypt(bytes.fromhex(message), privateKeyRsa)
    print(decrypted_message.decode("utf-8").strip())
