def accum(st):

    ls_st = list(st.lower())

    for i in range(0, len(ls_st)):

        ls_st[i] = ls_st[i] * (i + 1)
        ls_st[i] = ls_st[i].title()

    return "-".join(ls_st)
