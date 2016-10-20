import base64
import hashlib
import getpass

print("Enter easy remember password")
original_pass = getpass.getpass()
service = input("Enter service name: ")
digits = input("Enter length or leave blank using default (10): ")
digits = 10 if digits == '' else int(digits)
hash_obj = hashlib.sha256(str.encode(original_pass + service))
base64_pass = base64.b64encode(hash_obj.digest())
print("Password: {}".format(base64_pass.decode("ascii")[:digits]))
