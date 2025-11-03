def get_book_word_count (text):
    words = text.split()
    return len(words)

def character_count (text):
    dict_chars = {}
    lower_chars = text.lower()
    for c in lower_chars:
        if c in dict_chars:
            dict_chars[c] = dict_chars[c] +1
        else:
            dict_chars[c] = 1
    return dict_chars

def sorter(text):
    counts = character_count(text)
    items = []
    for ch, n in counts.items():
        items.append({"char": ch, "num": n})
    
    def sort_on(item):
        return item["num"]
    
    items.sort(key=sort_on, reverse=True)
    return items 
