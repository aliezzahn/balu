# balue

Balue is a Python package that implements a multi-layered encryption algorithm for educational purposes. It combines substitution, permutation, and XOR encryption techniques to provide a basic encryption and decryption functionality.

## Features

- **Substitution Cipher**: Shifts each byte of the plaintext based on a key.
- **Permutation Cipher**: Shuffles the bytes of the text.
- **XOR Cipher**: XORs the shuffled bytes with the key.

## Installation

### Using Poetry

1. **Install Poetry** if not already installed:

    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```

2. **Clone the repository**:

    ```bash
    git clone git@github.com:aliezzahn/balue.git
    cd balue
    ```

3. **Install the dependencies**:

    ```bash
    poetry install
    ```

### Manual Installation

1. **Clone the repository**:

    ```bash
    git clone git@github.com:aliezzahn/balue.git
    cd balue
    ```

2. **Install the dependencies** using `pip`:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Encryption and Decryption Example

Here's how you can use the `ComplexEncryptor` class to encrypt and decrypt a message.

1. **Create an encryptor instance** with a secret key.
2. **Encrypt a plaintext message**.
3. **Decrypt the ciphertext** to get back the original message.

```python
from balue.encryptor import ComplexEncryptor

# Initialize the encryptor with a secret key
key = "super_secret_key"
encryptor = ComplexEncryptor(key)

# Define the plaintext to be encrypted
plaintext = "This is a very secret message!"

# Encrypt the plaintext
encrypted = encryptor.encrypt(plaintext)
print("Encrypted:", encrypted)

# Decrypt the ciphertext
decrypted = encryptor.decrypt(encrypted['ciphertext'], encrypted['indices'])
print("Decrypted:", decrypted)
```

### Running the Test Script

To test the encryption and decryption process, you can run the provided test script.

```bash
python tests/test_encryptor.py
```

## Project Structure

```
balue/
│
├── README.md
├── balue/
│   ├── __init__.py
│   └── encryptor.py
└── tests/
    └── test_encryptor.py
├── pyproject.toml
```

## Security Considerations

This package is intended for educational purposes and should not be used for securing sensitive data in production environments. For real-world applications, rely on well-established cryptographic libraries and algorithms such as AES, RSA, and others provided by libraries like `cryptography`, `PyCrypto`, or `PyCryptodome`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.

## Acknowledgments

- Inspired by classical encryption techniques and the need to understand basic cryptographic principles.