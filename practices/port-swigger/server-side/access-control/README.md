## Access Control

Practical labs covering access control vulnerabilities and authorization weaknesses in web applications.

### Lab Write-ups

| Lab Name | Vulnerability | Exploited By |
|---|---|---|
| [Unprotected Admin Functionality](unprotected-admin-functionality/README.md) | Broken Access Control | Discovering hidden admin endpoint through `robots.txt` |
| [Unprotected Admin Functionality with Unpredictable URL](unprotected-admin-functionality-with-unpredictable-url/README.md) | Broken Access Control | Discovering admin endpoint in JavaScript |
| [User Role Controlled by Request Parameter](user-role-controlled-by-request-parameter/README.md) | Privilege Escalation | Modifying client-controlled cookie parameter |
| [User ID Controlled by Request Parameter with Unpredictable User IDs](user-id-controlled-by-request-parameter-with-unpredictable-user-ids/README.md) | IDOR | Manipulating user ID using an exposed GUID |
| [User ID Controlled by Request Parameter with Password Disclosure](user-id-controlled-by-request-parameter-with-password-disclosure/README.md) | IDOR / Information Disclosure | Modifying user ID to access administrator credentials |