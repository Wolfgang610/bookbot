import sys
from stats import get_num_words
from stats import get_characters
from stats import get_ordered_pairs
from stats import book_bot
def main():
     if len(sys.argv) == 2:
        book_bot(sys.argv[1])
     else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()





