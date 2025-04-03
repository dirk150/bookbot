def count_words(book_text):
    book_list = book_text.split()
    return f"Found {len(book_list)} total words"

def count_chars(book_text):
    char_dict = {}
    for char in book_text:
        lower_char = char.lower()
        if lower_char not in char_dict:
            char_dict[lower_char] = 1
        else:
            char_dict[lower_char] += 1
    return char_dict
def sorting_key(dict):
    return dict["num"]

def sort_char_count(char_dict):
    sorted_char_list = []
    for letter in char_dict:
        if letter.isalpha():
            count = char_dict[letter]
            sorted_char_list.append({"name":letter,"num":count})
    sorted_char_list.sort(reverse=True, key=sorting_key)
    return sorted_char_list