def get_book_word_count(text):
    words = text.split()
    return len(words)
    
def get_book_letter_count(text):
    lowered_letters = text.lower()
    letter_dictionary = {}
    for letter in lowered_letters:
        if letter.isalpha():
            if letter in letter_dictionary:
                    letter_dictionary[letter] += 1
            else :
                    letter_dictionary[letter] = 1
    return letter_dictionary


def sort_dictionary(letter_dictionary):
    sorted_letter_dictionary = dict(sorted(letter_dictionary.items(), key=lambda item: item[1], reverse=True))
    return sorted_letter_dictionary           