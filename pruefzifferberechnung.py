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
    
    for string in range(0,len(my_strings)):
        string_checksums.append(split(my_strings[string])) 
    
    for char_list in string_checksums:
        if len(char_list) > 1:
            for i in range(0,len(char_list)-1):
                new_int = int(char_list[i]) + int(char_list[i + 1])
                int_checksums.append(new_int)
        else: int_checksums.append(int(char_list[i]))

    for i in range(0,len(int_checksums)):
        odd_checksum = odd_checksum  + int_checksums[i]

    for i in range(1,len(id)-1,2):
        even_ids.append(id[i])

    for i in range(0,len(even_ids)):
        even_checksum = even_checksum + even_ids[i]

    even_odd_checksum = odd_checksum + even_checksum

    larger_multiple = even_odd_checksum + (10 - even_odd_checksum % 10)

    number_to_check = larger_multiple - even_odd_checksum

    if number_to_check == id[len(id)-1]:
        return True
    else: return False
    
def main():
    id = [6,2,5,8,4,3,1,9,7,9]
    my_bool = pruefeID(id)
    print(my_bool)
    
if __name__ == "__main__":
    main()

