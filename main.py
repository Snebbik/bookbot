from stats import get_book_word_count, get_book_letter_count, sort_dictionary
import sys


def main():
    if len(sys.argv) < 2:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    letter_dictionary = get_book_letter_count(text)
    sorted_letters = sort_dictionary(letter_dictionary)
    print ("============ BOOKBOT ============")
    print ("Analyzing book found at ",(book_path),"...")
    print ("----------- Word Count ----------")
    print (f"Found {get_book_word_count(text)} total words")
    print ("--------- Character Count -------")
    for key, value in sorted_letters.items():
        print (f"{key}: {value}")
    print ("============= END ===============")     
                                                                                                                                                                 

def get_book_text(path):
    with open(path) as f:
        return f.read()



if __name__ == "__main__":
    main()