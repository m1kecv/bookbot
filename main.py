def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()
        
        print(f"--- Begin report of {book_path} ---")
        print(f"{words_count(file_contents)} words found in the document\n")
        print_char_count(file_contents)
        print("--- End report ---")

def words_count(text):
    words = text.split()
    return len(words)

def print_char_count(text):
    result = {}
    chars =  "abcdefghijklmnopqrstuvwxyz"
    
    for c in chars:
        result[c] = 0


    for c in text:
        if c in chars:
            result[c] += 1

    result = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))

    for item in result.items():
        print(f"The '{item[0]}' character was found {item[1]} times")

    return result

main()