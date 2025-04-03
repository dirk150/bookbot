from stats import count_words, count_chars, sort_char_count
import sys

if len(sys.argv) != 2:
    print ("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filename):
    content_str = filename.read()
    return content_str

def main(book_path):
    with open(book_path) as f:
        booktext = get_book_text(f)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(count_words(booktext))
        print("--------- Character Count -------")
        result_chars_dict = count_chars(booktext)
        sorted_chars_dict = sort_char_count(result_chars_dict)
        for dict in sorted_chars_dict:
            print(f'{dict["name"]}: {dict["num"]}')
        print("============= END ===============")


main(sys.argv[1])