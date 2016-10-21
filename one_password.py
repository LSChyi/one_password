import base64
import hashlib
import getpass

def generate_pass(original_pass, service, length):
    hash_obj = hashlib.sha256(str.encode(original_pass + service + str(length)))
    base64_pass = base64.b64encode(hash_obj.digest())
    return base64_pass.decode("ascii")[:length]

if __name__ == "__main__":
    print("Remembered password")
    original_pass = getpass.getpass()
    service = input("Enter service name: ")
    length = input("Enter length or leave blank using default (10): ")
    length = 10 if length == '' else int(length)
    print("Password: {}".format(generate_pass(original_pass, service, length)))
