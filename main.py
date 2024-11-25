def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path) 
    word_count = count_words(text)
    letter_count = count_characters(text)

    write_report(book_path, word_count, letter_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    string_list = text.split()
    return len(string_list)    

def count_characters(text):

    characters = []
    dictionary = {}

    for n in text.lower():
        if n not in characters:
            characters.append(n)
            dictionary[n] = 0
        
        if n in characters:
            dictionary[n] += 1

    return dictionary

def write_report(title, word_count, letter_count):
    print(f"Begin report of ---{title}---")
    print(f"{word_count} words found in the the document\n")

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
              'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


    for key in letter_count:
        if key in letters:
            print(f"The '{key}' character was found {letter_count[key]} times.\n")
    
    print("---End Report---")
    

main()

