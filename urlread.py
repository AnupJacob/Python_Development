# ---------------------------------

# File          : urlread
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 07/12/2025
# Modified Date : 07/12/2025
# Description   :
# Licensing     : Anup Jacob, LYIT
# ----------------------------------

import requests

def urlread():
    url = "https://www.w3schools.com/python/python_decorators.asp"

    response = requests.get(url)
    text = response.text

    searchphrase = "But, when a function is decorated, the metadata of the original function is lost."

    found = False
    lines = text.splitlines()
    for i,line in enumerate(lines, start=1):
        if searchphrase in line:
            print(f"found in Line :{i}")
            found = True

    if not found:
        print(f"The line is not in the url.")

if __name__ == '__main__':

    urlread()


