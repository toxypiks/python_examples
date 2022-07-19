def auswertung(abdruck, schwelle, finger):
    liste_matches = suche(abdruck)
    run = True
    i = 0
    #fingerfilterteil
    if finger != 0:
        while(run):
            match = liste_matches[i]
            if match["idFinger"] != finger:
                liste_matches = loesche(liste_matches, i)
            else:    
                i = i+1     
            # abbruch bedingung        
            if(i+1 > laenge(liste_matches)):
                run = False
    # score filter teil
    run = True
    i = 0
    while(run):
        match = liste_matches[i]
        if match["score"] < schwelle:
            liste_matches = loesche(liste_matches, i)
        else:
            i = i+1
        if(i+1 > laenge(liste_matches)):
            run = False        
    return my_bubble_sort(liste_matches)

def my_bubble_sort(mein_array):
    if(len(mein_array) < 2):
        return mein_array
    tausche = 1
    while(tausche != 0):
        tausche = 0
        for i in range(0, len(mein_array)-1):
            if mein_array[i]["score"] < mein_array[i+1]["score"]:
                tausche += 1
                temp = mein_array[i]
                mein_array[i] = mein_array[i+1]
                mein_array[i+1] = temp
    return mein_array

def suche(abdruck):
    matches = []
    for element in abdrucke:
        abdruck_to_check = element[2]
        score = calc_score(abdruck, "{}".format(abdruck_to_check))
        if score > 0:
            match = {}
            match["score"] = score
            match["idPerson"] = element[0]
            match["idFinger"] = element[1]
            matches.append(match)
    return matches


def laenge(array):
    return len(array)


def loesche(array,position):
    new_array = []
    for i in range(0,len(array)):
        if(i!=position):
            new_array.append(array[i])
    return new_array        

#(person_id,finger_id,1233)
abdrucke = [(1,2,1334),(1,4,2674),(2,0,1789),(3,4,1786),(4,2,9774),(5,2,1798),(5,6,6254),(6,3,2340),(6,4,3945),(7,5,7494),(7,0,9372),(7,5,7332),(8,0,4238),(8,6,5319),(9,0,9758)]

def calc_score(gesuchter_abdruck, abdruck):
    score = 0;
    for i in range(0,4):
        g_char = gesuchter_abdruck[i]
        char = abdruck[i]
        if char == g_char:
            score += 25
    return score        

def main():

    abdruck = "1786"
    finger = 0
    score = 10
    ergebnis_liste = auswertung(abdruck,score,finger)
    print(ergebnis_liste)

    
if __name__ == "__main__":
    main()

