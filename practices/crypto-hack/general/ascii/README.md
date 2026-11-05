<!-- WVVoU01HTklUVFpNZVRsdVlWaFNiMlJYU1hWWk1qbDBUREkwZEZsWFduQmpWMFYyWkROS2NHUkhWakZqU0UwOQ== -->

## ASCII

### Objective
Convert an array of decimal integers into their corresponding ASCII characters to retrieve the flag.

### Solution

#### 1. Create `convert.py` 

Create a script to convert each integer into its corresponding ASCII character using Python's built-in `chr()` function.

```python
nums = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

flag = ''.join(chr(n) for n in nums)

print(flag)
```

#### 2. Run the script:

```bash
python3 convert.py
```

**Flag:** `crypto{ASCII_pr1nt4bl3}`

### Understanding the Method/Functions

- **`chr(n)`** – Converts an integer representing a Unicode code point into its corresponding character.
- **`ord(c)`** – Returns the Unicode code point of a single character as an integer.
- **`''.join()`** - Combines the resulting characters into a single string, reconstructing the flag.

### Lessons Learned

- Understand how ASCII represents characters using numerical values.
- Use Python's `chr()` to convert integers into characters.
- Use `ord()` to convert characters into their corresponding integer values.
- Recognize that `chr()` and `ord()` are useful for encoding and decoding character representations.

---

<div align="center">
  <sub> Created by <a href="https://github.com/n-afiqa/">@n-afiqa</a> · © 2026.</sub>
</div>
