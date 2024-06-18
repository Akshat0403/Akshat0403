def insert_demo(s, ch, k):
    modified_string = s[:k] + " " + ch + " " + s[k:]
    print("Modified String:", modified_string)

if __name__ == "__main__":
    original_String = "GeeksGeeks"
    ch_to_insert = "for"
    index_to_insert = 5
    print("Original String: ", original_String)
    insert_demo(original_String, ch_to_insert, index_to_insert)