def pruefeID(id):
    for i in range(0,len(id),2):
        print(id[i])
        
def main():
    id = [6,2,5,8,4,3,1,9,7,9]
    pruefeID(id)
    
if __name__ == "__main__":
    main()

