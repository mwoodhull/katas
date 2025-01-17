import re

def domain_name(url):

    pattern = r"/(?<=\/\/).+(?=....)"

    match = re.search(pattern, url)
    print(match)
    if match:

        return match