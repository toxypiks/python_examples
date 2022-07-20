def split(word):
    return list(word)

def pruefeID(id):
    odd_ids = []
    even_ids = []
    my_strings = []
    string_checksums = []
    int_checksums = []
    odd_checksum = 0
    even_checksum = 0
    
    for i in range(0,len(id)-1,2):
        id[i] = id[i] * 2
        odd_ids.append(id[i])
        
    for digit in odd_ids:
        my_strings.append(str(digit))
    print(my_strings)
    
    for string in range(0,len(my_strings)):
        string_checksums.append(split(my_strings[string])) 
    print(string_checksums)
    
    for char_list in string_checksums:
        if len(char_list) > 1:
            for test in range(0,len(char_list)-1):
                new_int = int(char_list[test]) + int(char_list[test + 1])
                int_checksums.append(new_int)
        else: int_checksums.append(int(char_list[test]))
    print(int_checksums)

    for i in range(0,len(int_checksums)):
        odd_checksum = odd_checksum  + int_checksums[i]
    print(odd_checksum)

    for i in range(1,len(id)-1,2):
        even_ids.append(id[i])
    print(even_ids)

    for i in range(0,len(even_ids)):
        even_checksum = even_checksum + even_ids[i]
    print(even_checksum)

    even_odd_checksum = odd_checksum + even_checksum

    print(even_odd_checksum)
        
    



    
def main():
    id = [6,2,5,8,4,3,1,9,7,9]
    pruefeID(id)
    
if __name__ == "__main__":
    main()

