from stats import count_words, count_characters, letter_dictionaries
import sys



def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else: 
        path_to_file = sys.argv[1]
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(f"Found {count_words(get_book_text(path_to_file))} total words")
        print("--------- Character Count -------")
        letter_list = letter_dictionaries(count_characters(get_book_text(path_to_file)))
        for i in letter_list:
            if i["char"].isalpha():
                print(f"{i["char"]}: {i["num"]}")
main()