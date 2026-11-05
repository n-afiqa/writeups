<!-- WVVoU01HTklUVFpNZVRsdVlWaFNiMlJYU1hWWk1qbDBUREkwZEZsWFduQmpWMFYyWkROS2NHUkhWakZqU0UwOQ== -->

## Favourite Byte

### Objective
Decode a hexadecimal string that has been encrypted using single-byte XOR with an unknown key to retrieve the flag.

### Solution

#### 1. Install pwntools:

```bash
python3 -m pip install pwntools --break-system-packages
```

#### 2. Create `hex_to_byte.py`:

```python
from pwn import xor

hex_string = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

data = bytes.fromhex(hex_string)

for key in range(256):
    flag = xor(data, key)
    if b"crypto{" in flag:
        print(flag.decode())
```

#### 3. Run the script:

```bash
python3 hex_to_byte.py
```

**Flag:** `crypto{0x10_15_my_f4v0ur173_by7e}`

### Understanding the Method/Functions

1. **`bytes.fromhex(hex_string)`** – Converts the hexadecimal string into bytes.
2. **`xor(data, key)`** – XORs each byte of the data with the same single-byte key.
3. **`range(256)`** – Generates all possible single-byte values, from 0 to 255.
4. **`if b"crypto{" in flag`** – Checks whether the decrypted output contains the expected flag prefix.

**Why try 256 keys?**

A single byte contains 8 bits, giving it \(2^8 = 256\) possible values. Since the XOR key is unknown, the script brute-forces all 256 possibilities until it finds a result containing the expected flag prefix.

### Lessons Learned

- Understand how single-byte XOR encryption works.
- Convert hexadecimal data into bytes before applying XOR.
- Use brute force to test all possible single-byte keys.
- Use a known plaintext prefix (`crypto{`) to identify the correct decryption result.

---

<div align="center">
  <sub> Created by <a href="https://github.com/n-afiqa/">@n-afiqa</a> · © 2026.</sub>
</div>
