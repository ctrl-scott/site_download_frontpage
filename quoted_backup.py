# quoted_backup.py
# Extracts all quoted content from a web page, excluding images or code tags.
# Created by ChatGPT in collaboration with a user.
# License: Creative Commons Zero (CC0) - Public Domain
# https://creativecommons.org/publicdomain/zero/1.0/
# for scottowen.jimdofree.com - June 21 2025 - USA

import requests
import re

# URL of the website to back up
url = 'https://scottowen.jimdofree.com'  # Replace with your desired URL

# Fetch the HTML source
response = requests.get(url)
html = response.text

# Find all content between single or double quotation marks
quoted_content = re.findall(r'["\'](.*?)["\']', html)

# Save the quoted content to a text file
with open('quoted_backup_output.txt', 'w', encoding='utf-8') as f:
    for item in quoted_content:
        f.write(item + '\n')

print(f"Done. Extracted and saved {len(quoted_content)} quoted strings.")

