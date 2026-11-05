<!-- WVVoU01HTklUVFpNZVRsdVlWaFNiMlJYU1hWWk1qbDBUREkwZEZsWFduQmpWMFYyWkROS2NHUkhWakZqU0UwOQ== -->

## Bytes and Big Integer

### Objective
Convert a large integer back into its original byte representation to retrieve the flag.

### Solution

#### 1. Install PyCryptodome:

```bash
python3 -m pip install pycryptodome --break-system-packages
```

#### 2. Create `convert_int_to_string.py`:

```python
from Crypto.Util.number import long_to_bytes

num = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

flag = long_to_bytes(num)

print(flag.decode())
```

#### 3. Run the script:

```bash
python3 convert_int_to_string.py
```

**Flag:** `crypto{3nc0d1n6_4ll_7h3_w4y_d0wn}`

### Understanding the Method/Functions

- **`long_to_bytes()`** – Converts a large integer into its corresponding byte representation.
- **`.decode()`** – Converts the resulting bytes into a readable string (UTF-8 by default).
- **`bytes_to_long()`** – Performs the reverse operation, converting bytes into a large integer.

- PyCryptodome provides `long_to_bytes()` and `bytes_to_long()` through its `Crypto.Util.number` module.

### Lessons Learned

- Understand how messages can be represented as large integers.
- Use `long_to_bytes()` to convert integers back into bytes.
- Use `bytes_to_long()` to convert bytes into integers.
- Recognize the relationship between integer and byte representations in cryptography.

---

<div align="center">
  <sub> Created by <a href="https://github.com/n-afiqa/">@n-afiqa</a> · © 2026.</sub>
</div>
