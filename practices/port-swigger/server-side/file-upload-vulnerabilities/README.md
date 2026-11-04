## File Upload Vulnerabilities

Practical labs covering insecure file upload functionality, upload restriction bypasses, and remote code execution through uploaded files.

### Lab Write-ups

| Lab Name | Vulnerability | Exploited By |
|---|---|---|
| [Remote Code Execution via Web Shell Upload](remote-code-execution-via-web-shell-upload/README.md) | Unrestricted File Upload | Uploading a PHP web shell to execute server-side code |
| [Web Shell Upload via Content-Type Restriction Bypass](web-shell-upload-via-content-type-restriction-bypass/README.md) | Content-Type Validation Bypass | Modifying the `Content-Type` header to bypass file type restrictions and upload a PHP web shell |