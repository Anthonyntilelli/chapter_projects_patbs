#!/usr/bin/env python

import sys, requests

if len(sys.argv) != 2:
    print("Please add 1 url in as a command line argument (do not include https://)")
    exit(1)

# check for a valid url

res = requests.get(f"https://{sys.argv[1]}")
res.raise_for_status()

# Parse the html
# Find all links
# download all thoses links and report any 404s.
