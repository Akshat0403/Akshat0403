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
        return 1

string1 = "Geeksforgeeks"
string2 = "Practice"
string3 = "Geeks"
string4 = "Geeks"

print("Comparing", string1, "and", string2, ":", string_compare(string1, string2))
print("Comparing", string2, "and", string3, ":", string_compare(string2, string3))
print("Comparing", string3, "and", string4, ":", string_compare(string3, string4))
print("Comparing", string4, "and", string1, ":", string_compare(string4, string1))