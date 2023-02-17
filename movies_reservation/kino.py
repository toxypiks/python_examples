def freieSitze(anzahlSitze):
    array_sitzplan = [[101,102,103,104,105,106,107,108,109,110],[201,202,203,204,205,206,207,208,209,210],[301,302,303,304,305,306,307,308,309,310]]
    array_reservierungen = [["F","F","F","T","T","T","T","F","F","T"],["F","T","F","T","F","T","F","T","F","T"],["F","F","T","F","T","T","T","T","F","T"]]

    count = 0
    stelle = -1
    item_count = -1
    ausgabe = 0
    freie_sitze_nummern = []

    for row in array_reservierungen:
        stelle += 1
        for item in row:
            item_count += 1
            if item == "T":
                count += 1
                freie_sitze_nummern.append(array_sitzplan[stelle][item_count])
            else:
                count = 0
                freie_sitze_nummern = []
            if count == anzahlSitze:
                print(freie_sitze_nummern[0])
                freie_sitze_nummern = []
                count = 0
            else:
                print(0)
        freie_sitze_nummern = []
        item_count = -1

def main():
    anzahlSitze = 3
    freieSitze(anzahlSitze)
    
if __name__ == "__main__":
    main()

     
