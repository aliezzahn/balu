import os
from hashlib import sha256
from random import shuffle, randint

class ComplexEncryptor:
    def __init__(self, key: str):
        self.key = sha256(key.encode()).digest()  # Use SHA-256 to derive a 256-bit key

    def _substitution_cipher(self, data: bytes, key: bytes) -> bytes:
        return bytes((data[i] + key[i % len(key)]) % 256 for i in range(len(data)))

    def _permutation_cipher(self, data: bytes) -> bytes:
        data_list = list(data)
        indices = list(range(len(data_list)))
        shuffle(indices)
        permuted_data = bytes(data_list[i] for i in indices)
        return permuted_data, indices

    def _reverse_permutation_cipher(self, data: bytes, indices: list) -> bytes:
        reversed_data = [None] * len(data)
        for original_index, permuted_index in enumerate(indices):
            reversed_data[permuted_index] = data[original_index]
        return bytes(reversed_data)

    def _xor_cipher(self, data: bytes, key: bytes) -> bytes:
        return bytes(data[i] ^ key[i % len(key)] for i in range(len(data)))

    def encrypt(self, plaintext: str) -> dict:
        data = plaintext.encode()
        
        # Step 1: Substitution cipher
        substituted_data = self._substitution_cipher(data, self.key)
        
        # Step 2: Permutation cipher
        permuted_data, indices = self._permutation_cipher(substituted_data)
        
        # Step 3: XOR cipher
        encrypted_data = self._xor_cipher(permuted_data, self.key)
        
        return {
            'ciphertext': encrypted_data,
            'indices': indices
        }

    def decrypt(self, ciphertext: bytes, indices: list) -> str:
        # Step 3: XOR cipher (reverse)
        xor_reversed_data = self._xor_cipher(ciphertext, self.key)
        
        # Step 2: Permutation cipher (reverse)
        permuted_reversed_data = self._reverse_permutation_cipher(xor_reversed_data, indices)
        
        # Step 1: Substitution cipher (reverse)
        decrypted_data = self._substitution_cipher(permuted_reversed_data, bytes(-x % 256 for x in self.key))
        
        return decrypted_data.decode()
