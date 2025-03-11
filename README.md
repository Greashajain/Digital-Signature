
# 🔐 Digital Signature in Python

This project demonstrates how to generate and verify **digital signatures** using **RSA and SHA-256** in Python. The implementation follows the **PKCS#1 v1.5** standard for secure message authentication.

## 🚀 Features
- Generate an **RSA key pair** (private & public keys).
- **Sign a message** using the private key.
- **Verify the signature** using the public key.
- Detect signature tampering or invalid messages.
- Uses **PyCryptodome** for cryptographic operations.

📜 Example Output

✅ Signature is valid.

❌ Signature is invalid due to tampered message.
