def removeChar(s, c):
    n = len(s)
    j = 0

    for i in range(n):
        if s[i] != c:
            s[j] = s[i]
            j += 1
    s = s[:j]
    return s

if __name__ == "__main__":
    s = "geeksforgeeks"
    s = list(s)
    s = removeChar(s, 'g')
    print(''.join(s))

