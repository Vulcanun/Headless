# headless
Fetches HTTP headers from the target and compares them to the OWASP Secure Headers Project.

## Usage
headless' main parameter is the target web application.

```
vulcanun@harder:~$ python headless.py https://udemy.com
[+] The 'Expect-CT' header was detected with the 'max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"' value.
[-] The 'X-XSS-Protection' header was not detected.
[+] The 'X-Content-Type-Options' header was detected with the 'nosniff' value.
[-] The 'Content-Security-Policy' header was not detected.
[-] The 'Strict-Transport-Security' header was not detected.
[-] The 'Feature-Policy' header was not detected.
[-] The 'X-Permitted-Cross-Domain-Policies' header was not detected.
[-] The 'X-Frame-Options' header was not detected.
[-] The 'Referrer-Policy' header was not detected.
[-] The 'Public-Key-Pins' header was not detected.

```
