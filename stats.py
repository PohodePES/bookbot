
def count_of_words(book_text):
    words = book_text.split()
    print(f"Found {len(words)} total words")

def count_characters(book_text):
    chars = {}

    for char in book_text.lower():
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

    return chars

def sort_on(item):
    return item["num"]


def characters_dict_to_sorted_list(char_dict):
    result = []

    for char, count in char_dict.items():
        if char.isalpha():
            result.append({"char": char, "num": count})

    result.sort(reverse=True, key=sort_on)

    return result
