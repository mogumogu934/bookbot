def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()


def get_word_count(book_path):
    return len(get_book_text(book_path).split())


def get_letter_count(book_path):
    letters = 0
    for i in get_book_text(book_path):
        if i.isalpha():
            letters += 1
    return letters


def get_individual_letter_counts(book_path):
    letters_dict = {}
    for letter in get_book_text(book_path).lower():
        if letter.isalpha():
            if letter in letters_dict:
                letters_dict[letter] += 1
            else:
                letters_dict[letter] = 1
   
    #Convert to a list of dictionaries
    letter_list = []
    for letter, count in letters_dict.items():
        letter_list.append({"char": letter, "num": count})
        
    letter_list.sort(reverse = True, key = lambda x: x["num"])
    return letter_list


def main():
    book_path = "books/frankenstein.txt"
    
    # Get the list of letter counts
    letter_counts = get_individual_letter_counts(book_path)
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{get_word_count(book_path)} words found in the document\n")
    print(f"{get_letter_count(book_path)} letters were found in the document\n")
    
    for item in letter_counts:
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

main()
