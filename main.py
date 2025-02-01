def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dict = get_char_dict(text)
    char_sorted_list = chars_dict_to_sorted_list(char_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in char_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print()
    print("--- End report ---")



def get_num_words(text):
    words = text.split()
    return len(words)



def sort_on(d):
    return d["num"]



def chars_dict_to_sorted_list(char_dict):
    sorted_list = []
    for ch in char_dict:
        sorted_list.append({"char": ch, "num": char_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list



def get_char_dict(text):
    char_freq = {}
    for t in text:
        lower = t.lower()
        if lower in char_freq:
            char_freq[lower] += 1
        else: 
            char_freq[lower] = 1
        
    return char_freq



def get_book_text(path):
    with open(path) as f:
        return f.read()
    


main()