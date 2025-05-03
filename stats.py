def get_book_text(filepath):
    """Reads and returns the contents of the file at the given filepath."""
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def count_total_words(book_text):
    """Counts the total number of words in the book."""
    words = book_text.split()
    return len(words)

def count_characters(book_text):
    """Counts the frequency of each character in the book text, case-insensitive."""
    book_text = book_text.lower()
    char_counts = {}
    for char in book_text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_char_counts(char_counts):
    """Sorts the character count dictionary into a list of dicts, descending by count."""
    sorted_list = [{"char": char, "num": count} for char, count in char_counts.items()]
    sorted_list.sort(key=lambda x: x["num"], reverse=True)
    return sorted_list
