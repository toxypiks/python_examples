def auswertung(abdruck, schwelle, finger):
    liste_matches = suche(abruck)
    run = True
    i = 0
    while(run):
        match = liste_matches[i]
        if match[idFinger] != finger:
            liste_matches = loesche(liste_matches,i)
        else:    
            i = i+1    
        if(i-1 > laenge(liste_matches)):
            run = False        
    


def suche(abdruck):
    print("speicher matches in array")
    matches = []
    for element in abdrucke:
        abdruck_to_check = element[2]
        score = calc_score(abdruck, "{}".format(abdruck_to_check))
        if score > 0:
            match = {}
            match[score] = score
            match[idPerson] = element[0]
            match[idFinger] = element[1]
            matches.append(match)
    return matches


def laenge(array):
    print("gibt länge array zurück")
    return len(array)


def loesche(array,position):
    new_arrray = []
    for i in range(0,len(array)):
        if(i!=position):
            new_arrray.append(array[i])
    return new_array        




#(person_id,finger_id,1233)
abdrucke = [(1,2,1334),(1,4,2674),(2,0,1789),(3,4,1786),(4,2,9774),(5,2,1798),(5,6,6254),(6,3,2340),(6,4,3945),(7,5,7494),(7,0,9372),(7,5,7332),(8,0,4238),(8,6,5319),(9,0,9758)]

def calc_score(gesuchter_abdruck, abdruck):
    score = 0;
    for i in range(0,4)
        g_char = gesuchter_abdruck[i]:
        char = abdruck[i]:
        if char == g_char:
            score += 25
    return score        
