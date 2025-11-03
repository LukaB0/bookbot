def get_book_text (path):
    with open(path) as f:
        return f.read()

def get_book_word_count ():
    contents = get_book_text("books/frankenstein.txt")
    words = contents.split()
    return len(words)