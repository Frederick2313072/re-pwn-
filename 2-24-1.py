from Crypto.Util.number import *
import base64
import base58
import hashlib
flag1="M0hBajFITHVLcWV6R1BOcEM5MTR0R0J3eGZVODV6MTJjZUhGZFNHQw=="
flag= int(base58.b58decode(base64.b64decode(flag1)))
print(flag)

flag = long_to_bytes(flag)
flag.decode("utf-8")
flag = hashlib.md5(flag).hexdigest()
print(flag)