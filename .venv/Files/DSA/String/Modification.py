def replace_Character_at_index(string, index, new_character):
    string_list = list(string)
    string_list[index] = new_character
    return ''.join(string_list)

def main():
    original_string = "Geeks for Geeks"
    index = 6
    new_character = "F"
    print("Original String = ", original_string)
    modified_string = replace_Character_at_index(original_string, index, new_character)
    print("Modified String = ", modified_string)

if __name__ == "__main__":
    main()