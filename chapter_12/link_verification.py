#!/usr/bin/env python

import sys, requests, bs4

if len(sys.argv) != 2:
    print("Please add 1 url in as a command line argument")
    exit(1)

url = sys.argv[1]
if not url.startswith("https://") and not url.startswith("http://"):
    print("Url MUST start with \"http://\" or \"https://\"")
    exit(1)

res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,"html.parser")
a_list = soup.select("a")

if len(a_list) == 0:
    print("There are no anchors on the page.")
    exit(0)

for a in a_list:
    test_link = a.attrs["href"]
    try:    
        if not test_link.startswith("https://") and not test_link.startswith("http://"):
            link = requests.get(url + test_link) # Relative path
        else:
            link = requests.get(test_link)
    except KeyboardInterrupt:
        print("Exiting:...")
        exit(1)
    except Exception as err:
        print(f"----> Skipping {test_link}: {err}")

    if link.status_code == 404:
      print(f"{test_link} was NOT Found")
    

    # Tested with:
    # https://google.com
    # https://example.com
    # https://badssl.com
