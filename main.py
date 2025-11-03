from stats import get_book_word_count

def main():
    word_count = get_book_word_count()
    print(f"Found {word_count} total words")

if __name__ == "__main__":
    main()
