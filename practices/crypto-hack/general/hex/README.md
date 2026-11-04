## Hex

### Objective
Convert a hexadecimal string into bytes and decode it into a readable message to retrieve the flag.

### Solution

#### 1. Create `convert_hex_to_byte.py`:

```python
hex_string = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"

flag = bytes.fromhex(hex_string)

print(flag.decode())
```

##### 2. Run the script:

```bash
python3 convert_hex_to_byte.py
```

**Flag:** `crypto{You_will_be_working_with_hex_strings_a_lot}`

### Understanding the Method/Functions

- **`bytes.fromhex()`** – Converts a hexadecimal string into bytes.
- **`.hex()`** – Converts a byte string into its hexadecimal representation.
- **`.decode()`** – Converts bytes into a readable string (UTF-8 by default).

### Lessons Learned

- Understand how hexadecimal represents byte values.
- Use `bytes.fromhex()` to decode hexadecimal strings into bytes.
- Use `.hex()` to convert bytes back into hexadecimal.
- Use `.decode()` to retrieve readable text from bytes.