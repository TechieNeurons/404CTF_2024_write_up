import base64

# Define your long_byte variable
long_byte = [215,194,241,104,227,144,...]

# Define your base64 string
base64_string = "base64 here"

# Decode the base64 string to get bytes
base64_bytes = base64.b64decode(base64_string)

decoded_bytes = []
# Perform XOR operation
for i in range(len(base64_bytes)):
    decoded_bytes.append(base64_bytes[i] ^ long_byte[i % len(long_byte)])

# Convert bytes to characters
decoded_text = ''.join(chr(byte) for byte in decoded_bytes)

# Print the result
print(decoded_text)
