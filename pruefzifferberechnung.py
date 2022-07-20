def split(word):
    return list(word)

def pruefeID(id):
    new_id = []
    my_strings = []
    string_checksum = []
    int_checksum = []
    
    for i in range(0,len(id),2):
        id[i] = id[i] * 2
        new_id.append(id[i])
    for digit in new_id:
        my_strings.append(str(digit))
    print(my_strings)
    for string in range(0,len(my_strings)):
        string_checksum.append(split(my_strings[string]))
    for num in string_checksum:
        for i in num:
            int_checksum.append(int(i))
    print(int_checksum)
        
def main():
    id = [6,2,5,8,4,3,1,9,7,9]
    pruefeID(id)
    
if __name__ == "__main__":
    main()

