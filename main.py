import sys
from stats import get_book_word_count, sorter

def main():
    if len(sys.argv) != 2: 
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) 

    filepath = sys.argv[1]
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    
    word_count = get_book_word_count(text)
    sorted_items = sorter(text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_items:
        ch = item["char"]
        if ch.isalpha():
            print(f"{ch}: {item['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()
