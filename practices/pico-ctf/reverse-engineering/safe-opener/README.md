## Safe Opener

### Objective:
Recover the lost key.

### Solution:
I started by inspecting `SafeOpener.java` with ExifTool, which identified it as a Java application. Reading the source code revealed that the `openSafe` method compares the encoded user input against a hardcoded `encodedKey`:
`cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz`

Since the key was Base64-encoded, I decoded it using CyberChef and recovered the password:
`pl3as3_l3t_m3_1nt0_th3_saf3`

The decoded password is the flag.

### Lessons Learned:
Reading source code and identifying encoded hardcoded values can help uncover secrets in reverse engineering challenges.