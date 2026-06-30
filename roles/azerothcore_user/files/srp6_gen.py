#!/usr/bin/env python3
import sys, os, hashlib, json

N = int("894B645E89E1535BBDAD5B8B290650530801B18EBFBF5E8FAB3C82872A3E9BB7", 16)
g = 7

def calculate_verifier(username, password, salt_bytes):
    h1 = hashlib.sha1((username.upper() + ":" + password.upper()).encode()).digest()
    h2 = hashlib.sha1(salt_bytes + h1).digest()
    x = int.from_bytes(h2, byteorder='little')
    v = pow(g, x, N)
    return v.to_bytes(32, byteorder='little')

username, password = sys.argv[1], sys.argv[2]
salt = os.urandom(32)
verifier = calculate_verifier(username, password, salt)

print(json.dumps({
    "salt": salt.hex(),
    "verifier": verifier.hex()
}))
