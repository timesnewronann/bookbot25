from stats import count_words, count_characters, chars_dict_to_sorted_list
import sys


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        # do something with f (the file) here
        file_contents = f.read()
        return file_contents


def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)  # Read file ONCE
    num_words = count_words(text)  # Pass text, get result back
    print(f"Found {num_words} total words")  # Now YOU control when to print
    count = count_characters(text)
    print(f"Character Count Dictionary: {count}")

    chars_sorted_list = chars_dict_to_sorted_list(count)
    print_report(book_path, num_words, chars_sorted_list)


if __name__ == "__main__":
    main() 
