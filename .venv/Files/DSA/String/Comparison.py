def string_compare(str1, str2):
    l1 = len(str1)
    l2 = len(str2)
    lmin = min(l1, l2)

    for i in range(lmin):
        str1_ch = ord(str1[i])
        str2_ch = ord(str2[i])

        if str1_ch != str2_ch:
            return 0
    if l1 != l2:
        return 0
    else:
        return