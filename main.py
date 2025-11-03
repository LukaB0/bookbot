from stats import get_book_word_count, character_count

def main():
    word_count = get_book_word_count()
    char_count = character_count()
    print(f"Found {word_count} total words")
    print(char_count)

if __name__ == "__main__":
    main()
