from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Generate RSA Key Pair
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

# Save Keys to Files
with open("private.pem", "wb") as priv_file:
    priv_file.write(private_key)

with open("public.pem", "wb") as pub_file:
    pub_file.write(public_key)

# Create Message and Hash
message = b"Secure transaction data"
hash_obj = SHA256.new(message)

# Sign the Hash
signature = pkcs1_15.new(key).sign(hash_obj)
print(f"Digital Signature: {signature.hex()}")

# Verify the Signature
try:
    pkcs1_15.new(RSA.import_key(public_key)).verify(hash_obj, signature)
    print("✅ Signature is valid.")
except (ValueError, TypeError):
    print("❌ Signature is invalid.")

# Tamper with Message (to Test Invalid Signature)
#tampered_message = b"Tampered transaction data"
#tampered_hash = SHA256.new(tampered_message)
#
#try:
#    pkcs1_15.new(RSA.import_key(public_key)).verify(tampered_hash, signature)
#    print("✅ Signature is valid.")
#except (ValueError, TypeError):
#    print("❌ Signature is invalid due to tampered message.")  # Should fail
#
