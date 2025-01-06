def initials(name):

    name_lis = name.split()
    name_str = ""

    for name in name_lis:
        if name is not name_lis[-1]:
            initial = name[:1]
            name_str += f"{initial.upper()}."

        else:
            name_str += f"{name.title()}"

    return name_str
