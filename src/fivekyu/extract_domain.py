import re

def domain_name(url):

    pattern = r"(?:https?:\/\/)?(?:www\.)?([a-zA-Z0-9-]+)"

    match = re.search(pattern, url)

    if match:

        return match.group(1)
        
    else:
        return 'not found'