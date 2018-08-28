import requests
import argparse

headers = {'Strict-Transport-Security', 'Public-Key-Pins', 'X-Frame-Options', 'X-XSS-Protection', 'X-Content-Type-Options', 'Content-Security-Policy', 'X-Permitted-Cross-Domain-Policies', 'Referrer-Policy', 'Expect-CT', 'Feature-Policy'}

parser = argparse.ArgumentParser(description='Fetch HTTP headers related to security.')
parser.add_argument('target', help='Target server.')
parser.add_argument('-L', '--location', action='store_true', dest="location", help='If set, headless will follow 30X redirects. Default is False.', default=False)
parser.add_argument('-A', '--user-agent', dest="uagent", help='Allows for the usage of custom User-Agent value.', default=requests.Session().headers['User-Agent'])
args = parser.parse_args()

try:
    r = requests.head(args.target, allow_redirects=args.location, headers={'User-Agent':args.uagent})

    print '\033[92m[+] Request Completed, received code ' + str(r.status_code) + ' for "' + r.url + '".\n'

    for h in headers:
        try:
            print "\033[92m[+] The '" + h + "' header was detected with the '" + r.headers[h] + "' value."
        except Exception as e:
            print "\033[91m[-] The '" + h + "' header was not detectedself."
except Exception as e:
    print 'Uh oh, something bad happened. Dying.'
    print 'Exception: ' + e
