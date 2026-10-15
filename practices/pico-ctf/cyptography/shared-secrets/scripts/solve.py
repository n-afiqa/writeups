from pathlib import Path
import ast

data = {}

for line in Path("message.txt").read_text().splitlines():
    key, value = line.split(" = ", 1)
    data[key] = ast.literal_eval(value) if key != "enc" else bytes.fromhex(value)

g = data["g"]
p = data["p"]
A = data["A"]
b = data["b"]
enc = data["enc"]

shared = pow(A, b, p)
key = shared % 256

flag = bytes(c ^ key for c in enc)

print(f"Shared key byte: {key}")
print(f"Flag: {flag.decode()}")
