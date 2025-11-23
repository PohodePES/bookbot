from stats import count_of_words, count_characters, characters_dict_to_sorted_list
import sys


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")

    text = get_book_text(book_path)
    count_of_words(text)

    print("--------- Character Count -------")

    chars = count_characters(text)
    sorted_chars = characters_dict_to_sorted_list(chars)

    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


def get_book_text(file_path):
    with open(file_path, "r") as f:
        return f.read()


main()
