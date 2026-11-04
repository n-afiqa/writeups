## XOR Starter

### Objective

XOR each character in the string with the integer 13, convert the resulting integers back into characters, and retrieve the flag in the format `crypto{new_string}`.

### Solution

#### 1. Understand the logic

Convert each character into its ASCII integer, perform XOR with 13, then convert the result back into a character.

```text
String → ASCII integer → XOR → Character → String
```

#### 2. Install pwntools

```bash
sudo apt install python3-pwntools
```

#### 3. Create `new_string.py`:

```python
data = "label"

flag = ''.join(chr(ord(char) ^ 13) for char in data)

print(f"crypto{{{flag}}}")
```

#### 4. Run the script:

```bash
python3 new_string.py
```
**Flag:** `crypto{aloha}`

### Understanding the Method/Functions

- **`ord()`** – Converts a character into its corresponding Unicode integer value.
- **`^`** – Performs the bitwise XOR operation between two integers.
- **`chr()`** – Converts an integer into its corresponding Unicode character.
- **`''.join()`** – Combines individual characters into a single string.
- **`f-string`** – Formats the output. Double braces `{{ }}` produce literal curly braces.

### Lessons Learned

- Understand how XOR operates on integer values.
- Use `ord()` and `chr()` to convert between characters and integers.
- Apply XOR directly to character values without converting the entire string into bytes.
- Use `join()` to reconstruct the resulting string.