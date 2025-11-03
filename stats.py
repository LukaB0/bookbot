def get_book_text (path):
    with open(path) as f:
        return f.read()

def get_book_word_count ():
    contents = get_book_text("books/frankenstein.txt")
    words = contents.split()
    return len(words)

def character_count ():
    dict_chars = {}
    characters = get_book_text("books/frankenstein.txt")
    lower_chars = characters.lower()
    for c in lower_chars:
        if c in dict_chars:
            dict_chars[c] = dict_chars[c] +1
        else:
            dict_chars[c] = 1
    return dict_chars
