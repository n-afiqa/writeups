## information

### Objective:
Uncover the flag.

### Solution:
I started by inspecting `cat.jpg` with ExifTool and found encoded text `YWNhZGVteXt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9` in the metadata.

After decoding the text with CyberChef, I recovered the flag:
`academy{the_m3tadata_1s_modified}`

### Lessons Learned:
Image metadata can contain encoded data that reveals the flag when decoded.