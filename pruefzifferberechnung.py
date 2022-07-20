def pruefeID(id):
    new_id = []
    my_strings = []
    
    for i in range(0,len(id),2):
        id[i] = id[i] * 2
        new_id.append(id[i])
    for digit in new_id:
        my_strings.append(str(digit))
    print(my_strings)
    
        
def main():
    id = [6,2,5,8,4,3,1,9,7,9]
    pruefeID(id)
    
if __name__ == "__main__":
    main()

