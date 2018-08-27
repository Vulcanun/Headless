import requests
import argparse

headers = {'Strict-Transport-Security', 'Public-Key-Pins', 'X-Frame-Options', 'X-XSS-Protection', 'X-Content-Type-Options', 'Content-Security-Policy', 'X-Permitted-Cross-Domain-Policies', 'Referrer-Policy', 'Expect-CT', 'Feature-Policy'}

parser = argparse.ArgumentParser(description='Fetch HTTP headers related to security.')
parser.add_argument('target', help='Target server.')
args = parser.parse_args()

r = requests.head(args.target).headers

for h in headers:
    try:
        print "\033[92m[+] The '" + h + "' header was detected with the '" + r[h] + "' value."
    except Exception as e:
        print "\033[91m[-] The '" + h + "' header was not detected."
