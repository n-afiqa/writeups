## XOR Properties

### Objective

Recover the original flag by using XOR properties to cancel out the three keys involved in the encryption.

### Solution

#### 1. Understand the XOR properties

The key properties are:

**Commutative:** A ⊕ B = B ⊕ A
**Associative:** A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C
**Identity:** A ⊕ 0 = A
**Self-Inverse:** A ⊕ A = 0

The important rule is that XORing the same value twice cancels it out:

A ⊕ B ⊕ B = A

Given:

```text
KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313

KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e

KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1

FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf
```

**2. Rearrange the XOR expression**

The encrypted flag is:

C = FLAG ⊕ KEY1 ⊕ KEY3 ⊕ KEY2

To recover the flag, XOR the encrypted flag with the same three keys:

FLAG = C ⊕ KEY1 ⊕ KEY3 ⊕ KEY2

Since `KEY2 ^ KEY3` is already provided, combine the known keys:

KEY1 ⊕ (KEY2 ⊕ KEY3)

#### 3. Install pwntools

```bash
python3 -m pip install pwntools --break-system-packages
```

#### 4. Create `decrypt.py`:

```python
from pwn import xor

KEY1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")

KEY2_KEY3 = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")

FLAG_KEY1_KEY3_KEY2 = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")

# Combine the known keys
combined_keys = xor(KEY1, KEY2_KEY3)

# Cancel out the keys to recover the flag
flag = xor(FLAG_KEY1_KEY3_KEY2, combined_keys)

print(flag.decode())
```

#### 5. Run the script:

```bash
python3 decrypt.py
```

**Flag:** `crypto{<actual output from script>}`

### Understanding the Method/Functions

- **xor()** – Performs an XOR (exclusive OR) operation between two byte strings. It is provided by the pwntools library (from pwn import xor).

### Lessons Learned

- Understand XOR properties: self-inverse, commutative and associative.
- Recognize that XORing the same value twice cancels it out.
- Rearrange XOR expressions to isolate unknown values.
- Combine partially known keys to recover the original plaintext.
- Use pwntools `xor()` to perform XOR operations on byte strings.