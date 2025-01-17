import re

def domain_name(url):

    pattern = r"(?<=\/\/).+(?=....)"

    match = re.search(pattern, url)
    print(match.group())
    if match:

        return match.group()