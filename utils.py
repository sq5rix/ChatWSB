import hashlib

def calculate_digest(input_string):
    # Encode the input string to bytes
    input_bytes = input_string.encode('utf-8')

    # Calculate the SHA-256 hash of the input bytes
    sha256_hash = hashlib.sha256(input_bytes)

    # Get the hexadecimal representation of the hash
    hex_digest = sha256_hash.hexdigest()

    # Convert the hexadecimal digest to an integer
    digest_number = int(hex_digest, 16)

    return digest_number

def main():
    input_string = "Hello, World!"
    digest_number = calculate_digest(input_string)
    print("Digest number of '{}' is: {}".format(input_string, digest_number))


if __name__ == "__main__":
    main()
