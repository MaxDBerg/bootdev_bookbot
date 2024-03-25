import time

def main():

    book = read_book()    

    num_of_words_in_whole_book = words_in_book(book)

    print(f"The number of words in the books is : {num_of_words_in_whole_book}")

    character_list = words_in_book_per_character(book)

    character_list.sort(reverse=True, key=sort_on)

    for character in character_list:
        print(character["char"] + " appears " + str(character["num"]) + " times in the book")

def sort_on(dict):
    return dict["num"]

def read_book():
    with open("books/frankenstein.txt") as book:
        book_contents = book.read()
        return book_contents

def words_in_book(book):
    book_wc = book.split()
    return len(book_wc)


def words_in_book_per_character(book):
    character_list = []

    for character in book:

        lowered_character = character.lower()

        char_index = is_char_in_list(lowered_character, character_list)
        
        if(char_index >= 0):

            character_list[char_index]["num"] += 1
 
        else:

            character_list.append({"char": lowered_character, "num": 1})    
    
    return character_list

def is_char_in_list(char, char_list):
        
    for i in range(0, len(char_list)):
    
        if char == char_list[i]["char"]:

            return i
    return -1

main()