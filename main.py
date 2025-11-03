def get_book_text (path):
    with open(path) as f:
        return f.read()

def main():
    contents = get_book_text("books/frankenstein.txt")
    print(contents)

if __name__ == "__main__":
    main()
