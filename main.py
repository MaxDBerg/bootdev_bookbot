def main():

    book = read_book()    

    num_of_words_in_whole_book = words_in_book(book)

    print(f"The number of words in the books is : {num_of_words_in_whole_book}")

    num_of_words_for_each_character = words_in_book_per_character(book)

    for character in num_of_words_for_each_character:
        print(f"{character} has {num_of_words_for_each_character[character]} words in the book")

def read_book():
    with open("books/frankenstein.txt") as book:
        book_contents = book.read()
        return book_contents

def words_in_book(book):
    book_wc = book.split()
    return len(book_wc)


def words_in_book_per_character(book):
    character_wc_instances = {"frankenstein": 0,}

    book_split_by_word = book.split()

    for word in book_split_by_word:
        for character in character_wc_instances:
            if word.lower() == character.lower():
                character_wc_instances["frankenstein"] += 1
    return character_wc_instances


main()