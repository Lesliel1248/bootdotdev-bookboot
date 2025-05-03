import sys
from stats import get_book_text, count_total_words, count_characters, sort_char_counts

def main():
    # Validate command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")

    try:
        book_text = get_book_text(filepath)
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        sys.exit(1)

    word_count = count_total_words(book_text)
    char_counts = count_characters(book_text)
    sorted_chars = sort_char_counts(char_counts)

    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    for entry in sorted_chars:
        char = entry["char"]
        # Optional: filter output to show only meaningful characters
        if char.isalpha():
            print(f"{char}: {entry['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()
