def count_words(text):
    words = text.split()
    num_words = len(words)

    return num_words


"""
takes the text from the book as a string, and returns the number of times each character, (including symbols and spaces), appears in the string.
"""


def count_characters(text):
    count = {}
    text = text.lower()
    words = text.split()
    for word in words:
        for letter in word:
            if letter in count:
                count[letter] += 1
            else:
                count[letter] = 1

    return count


def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(chars_dict):
    sorted_list = []

    # Step 1: Convert dict to list of dicts
    for ch in chars_dict:
        sorted_list.append({"char": ch, "num": chars_dict[ch]})

    # Step 2: Sort the list
    sorted_list.sort(reverse=True, key=sort_on)

    # Step 3: Return it
    return sorted_list
