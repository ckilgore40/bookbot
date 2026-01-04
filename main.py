from stats import word_count, occorances, sorted_dict
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
      
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        BOOK_PATH = sys.argv[1]
        letter_stats = occorances(get_book_text(BOOK_PATH))
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {BOOK_PATH}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count(get_book_text(BOOK_PATH))} total words")
        print("--------- Character Count -------")
        for item in sorted_dict(letter_stats):
            if item["char"].isalpha():
                print(f"{item["char"]}: {item["num"]}")
        print("============= END ===============")

main()