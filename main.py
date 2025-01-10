def main():
    book_path = "books/frankenstein.txt"
    text = get_book_path(book_path)
    count = word_count(text)
    char_count = letter_count(text)
    letter_only = letter_filter(char_count)
    by_num = sort_by_number(letter_only)


    print(f"--- Begin report of {book_path} ---")
    print(f"{count} words found in the document")
    print("")
    for e in by_num:
        c = e["char"]
        n = e["num"]
        print(f"The '{c}' character was found {n} times")
    print("--- End report ---")
    

def get_book_path(path):    
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def word_count(text):
    words = text.split()
    count = 0
    for w in words:
        count += 1
    return count

def letter_count(text):
    lower_string = text.lower()
    letters = list(lower_string)
    filtered_letters = []
    character_count = {}
    for l in letters:
        if l != " ":
            filtered_letters.append(l)
    for c in filtered_letters:
        if c not in character_count:
            character_count[c] = 1
        else:
            character_count[c] += 1  

    return character_count

def letter_filter(mix):
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    letter_dic = []
    for l in mix:
        if l in letters:
            addi = {}
            addi["char"] = l
            addi["num"] = (mix[l])
            letter_dic.append(addi)
    return letter_dic

def sort_on(dict):
    return dict["num"]

def sort_by_number(list):
    list.sort(reverse=True, key=sort_on)
    return list


main()