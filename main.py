import sys
from stats import get_num_words, get_character_count, sort_dict

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    args = sys.argv
    if len(args) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(args[1])
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {args[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(text)} total words")
    print("--------- Character Count -------")
    character_count = get_character_count(text)
    for character in sort_dict(character_count):
        for k, v in character.items():
            if k.isalpha():
                print(f"{k}: {v}")
    print("============= END ===============")

main()