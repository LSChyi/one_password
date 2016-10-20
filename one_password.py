import base64
import hashlib
import getpass

def generate_pass(original_pass, service):
    hash_obj = hashlib.sha256(str.encode(original_pass + service))
    base64_pass = base64.b64encode(hash_obj.digest())
    return base64_pass.decode("ascii")[:digits]

if __name__ == "__main__":
    print("Enter easy remember password")
    original_pass = getpass.getpass()
    service = input("Enter service name: ")
    digits = input("Enter length or leave blank using default (10): ")
    digits = 10 if digits == '' else int(digits)
    print("Password: {}".format(generate_pass(original_pass, service)))
