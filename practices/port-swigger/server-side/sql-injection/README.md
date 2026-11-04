# SQL Injection

Practical labs covering SQL injection techniques, database query manipulation, data retrieval, and authentication bypass.

### Lab Write-ups

| Lab Name | Vulnerability | Exploited By |
|---|---|---|
| [SQL Injection Vulnerability in WHERE Clause Allowing Retrieval of Hidden Data](sql-injection-vulnerability-in-where-clause-allowing-retrieval-of-hidden-data/README.md) | WHERE Clause Manipulation to Bypass Data Restrictions | Boolean-based injection (`OR 1=1`) and SQL comment syntax (`--`) |
| [SQL Injection Vulnerability Allowing Login Bypass](sql-injection-vulnerability-allowing-login-bypass/README.md) | Authentication Bypass via SQL Injection | SQL comment injection (`'--`) to neutralize the password condition |