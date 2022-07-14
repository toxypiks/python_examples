from random import randrange

def fahreRegalAn (regalNr):
    print("regalNr:{} {}".format(regalNr,"hey"))

def fahreEbeneAn(ebeneNr):
    print("ebeneNr:{}".format(ebeneNr))

def fahreFachAn(fachNr):
    print("fachNr:{}".format(fachNr))

def pruefeWare(ware_id):
    random_number = randrange(0,2)
    if random_number == 0 :
        return True
    return False

def entnehmeWare(regalNr, ebeneNr,fachNr):
    print("regalNr:{}, ebeneNr:{}, fachNr{}".format(regalNr,ebeneNr,fachNr))

def kopiereZeile(liste_array,fehler_array,zeileL,zeileF):
    fehler_array.append(liste_array[zeileL])
    print("Zeile kopiert")
    
def entnehmeWaren(liste_array):
    ware_id = liste_array[0][0]
    regal = liste_array[0][1]
    ebene = liste_array[0][2]
    fach = liste_array[0][3]
    fehler_array = []
# 0(warenid) 1(regal) 2(Ebene) 3(fach)
    row_index = 0
    fehler_index = 0

    for row_index in liste_array
        #row = [344;1;1;1]
        waren_id = row[0]
        regal  = row[1]
        ebene = row[2]
        fach = row[3]
        fahreRegalAn(regal)
        fahreEbeneAn(ebene)
        fahreFachAn(fach)

        if pruefeWare(waren_id) == True:
            entnehmeWare(regal,ebene,fach)
        else:
            kopiereZeile(liste_array,fehler_array,row_index,fehler_index)
            fehler_index += 1
        row_index += 1    

    print("huhuhuhey")
    print(fehler_array)

def main():
    liste_array = []
    liste_array.append([233,1,1,1])
    liste_array.append([234,3,1,6])
    liste_array.append([235,1,4,1])
    liste_array.append([236,1,2,1])

    entnehmeWaren(liste_array)
    
if __name__ == "__main__":
    main()
    
    
