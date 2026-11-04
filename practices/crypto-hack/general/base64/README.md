## Base64

### Objective
Convert a hexadecimal string into bytes, then encode the bytes into Base64 to retrieve the flag.

### Solution

#### 1. Create `decode_base64.py`:

```python
import base64

hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

data = bytes.fromhex(hex_string)
flag = base64.b64encode(data)

print(flag.decode())
```

#### 2. Run the script:

```bash
python3 decode_base64.py
```

**Flag:** `crypto/Base+64+Encoding+is+Web+Safe/`

Submit the output as the flag.

### Understanding the Method/Functions

- **`bytes.fromhex()`** – Converts a hexadecimal string into bytes.
- **`base64.b64encode()`** – Encodes bytes into Base64 representation.
- **`.decode()`** – Converts the resulting bytes into a readable string (UTF-8 by default).

### Lessons Learned

- Understand the difference between hexadecimal, bytes, and Base64 representations.
- Use Python's `bytes.fromhex()` to convert hexadecimal data into bytes.
- Use `base64.b64encode()` to encode binary data into Base64.
- Recognize that Base64 is an encoding scheme, not encryption.