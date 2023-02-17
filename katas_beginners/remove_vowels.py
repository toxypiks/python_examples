def remove_vowel(text):
    string_list = list(text)
    new_string_list = []
    for string in string_list:
        if string != 'a' and string != 'A'and string != 'o' and string != 'O' and string != 'u' and string != 'U' and string != 'e' and string != 'E' and string != 'i' and string != 'I':
            new_string_list.append(string)
    return ' '.join(new_string_list)
            
def main():

    text = "This website is for losers LOL!"
    new_text = remove_vowel(text)
    print(new_text)

if __name__ == "__main__":
    main()
