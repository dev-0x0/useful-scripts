#!/usr/bin/python3
#
# Downloads the latest burpsuite community jar file and saves it to /usr/share/burpsuite.jar (the default location at time of writing)
# EXTREMELY likely to break in the future
# as portswigger make any changes to their download page etc.
#
# Disclaimer:
# NEVER run code from github on your machine without making
# sure you know what it does first. I'm not responsible for any
# loss or damage incurred by running this script. Enjoy!
#
# dev0x0 
# 
# 
#

import os
import sys
import requests
import shutil
from bs4 import BeautifulSoup

LATEST_VER_URL = "https://portswigger.net/burp/releases/community/latest"
DOWNLOAD_URL = "https://portswigger.net/burp/releases/download?product=community&version={}&type=jar"

html = requests.get(LATEST_VER_URL)

if html.status_code != 200:
    raise("[!] Could not reach site "+BASE_URL)
    sys.exit(0)

print("[*] BurpSuite Site reached...")

# Parse html with bs4
content = BeautifulSoup(html.text, features="lxml")

if not content:
    raise("[!] Error parsing site content...")
    sys.exit(0)

print("[*] Latest burpsuite version: ", end="")
# get latest burp version from page text
version_heading = content.find('div', {'class': 'post-card'}).find_next('h1')
latest_version = version_heading.text[25:]
print(latest_version)

print("[*] Wgetting now ...")

# concatentate final download link
download_link = DOWNLOAD_URL.format(latest_version)

os.chdir("/usr/share/burpsuite")

# backup current jar just in case
os.system("sudo rm burpsuite.jar.old 2>/dev/null")
os.system("sudo mv burpsuite.jar burpsuite.jar.old")
print(download_link)
os.system("sudo wget -O burpsuite.jar {}".format(download_link))

