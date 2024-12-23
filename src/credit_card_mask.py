def credit_card_mask(password):

    if len(password) <= 4:
        return password

    else:
        lst_pass = list(password)

        for i in range(len(lst_pass) - 4):
            lst_pass[i] = "#"

        hidden_pass = "".join(lst_pass)

        return hidden_pass

    # if len(password) <= 4:
    #     return password

    # else:
    #     return '#'*(len(password)-4) + password[-4:]
