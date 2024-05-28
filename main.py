def main():
    the_path = "books/frankenstein.txt"
    text = get_book_content(the_path)
    number_of_words = get_number_of_words(text=text)
    letter_conts = get_number_of_each_char(text=text.lower())
    print(f"--- Begin report of {the_path} --")
    print(f"{number_of_words} words found in the document")
    for char in get_number_of_each_char(text=text):
        print(f"The '{char}' character was found {get_number_of_each_char(text)[char]} times")
    print("--- End report ---")



def get_number_of_words(text):
    words = text.split()
    return len(words)


def get_number_of_each_char(text):
    new_lower_text = text.lower()
    letter_counts = {}
    for char in new_lower_text:
        if char.isalpha():
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1
    return letter_counts


def get_book_content(path):
    with open(path) as f:
        return f.read()
    

main()