from balue.encryptor import ComplexEncryptor

key = "super_secret_key"
encryptor = ComplexEncryptor(key)

plaintext = "This is a very secret message!"
encrypted = encryptor.encrypt(plaintext)
print("Encrypted:", encrypted)

decrypted = encryptor.decrypt(encrypted['ciphertext'], encrypted['indices'])
print("Decrypted:", decrypted)
