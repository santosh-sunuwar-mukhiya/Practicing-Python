import bcrypt

password = "santosh123"

# Convert password to bytes and hash it
password_bytes = password.encode('utf-8')
password_hash = bcrypt.hashpw(password_bytes, bcrypt.gensalt())

print(f"Password hash: {password_hash.decode('utf-8')}")

# Example: Verify the password
is_valid = bcrypt.checkpw(password_bytes, password_hash)
print(f"Verification: {is_valid}")