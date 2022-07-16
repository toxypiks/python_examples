import csv
from random import randrange

def hole_journalsatz():
    print("journalsatz")

def lese_kundenid(satz):
    print("kundenid")

def lese_leistungsid(satz):
    print("leistungsid")

def lese_einzelpreis(satz):
    print("einzelpreis")

def lese_anzahl(satz):
    print("anzahl")

def hole_bezeichnung(leistungsid):
    bezeichnungen = ["Kaffee gekocht", "Brötchen geschmiert", "Obstschale aufgefüllt"]
    random_number = randrange(0,3)
    return bezeichnungen[random_number]

def schreibe_kundenid(kundenid):
    print("schreibe_kundenid")

def schreibe_kopfzeile():
    print("kopfzeile")

def schreibe_positionszeile(pos,leistungsid,bezeichnung,anzahl,einzelpreis,gesamtpreis):
    print("kopfzeile")

def schreibe_rechnungssumme(rechnungssumme):
    print("rechnungssumme")

journal = {'Datum': ["2016-04-01","2016-04-10","2016-04-10","2016-04-03","2016-04-11","2016-04-05"],'KundenID':["K00091","K00091","K00091","K01234","K01234","K01234"],'LeistungsID': [100076,100076,500123,200234,200234,200356],'EinzelPreis': [2.40,2.40,15.00,20.00,20.00,15.00],'Anzahl': [2,3,1,1,1,1]}

def erstelleRechnung(records):
    kunden_ids = []
    leistungs_ids = []
    einzelpreise_liste = []
    anzahl_liste = []

    position = 0
    rechnungen = []
    bezeichnung = ""

    final_dict = {}
    keys_final_dict = ["Pos", "LeistungsID","Bezeichnung der Leistung", "Anzahl", "Einzelpreis"]
    anzahl = 1
    liste_dict = []

    
    for key in journal:
        if key == 'KundenID':
            kunden_ids = list(journal.values())[1]
        if key == 'LeistungsID':
            leistungs_ids = list(journal.values())[2]
        if key == 'EinzelPreis':
            einzelpreise_liste = list(journal.values())[3]
        if key == 'Anzahl':
            anzahl_liste = list(journal.values())[4]

    with open("rechnungen.csv", 'wt') as csvFile:
        headers = ["Pos","LeistungsID","Bezeichnung_der_Leistung","Anzahl","EinzelPreis"]
        writer = csv.DictWriter(csvFile,fieldnames=headers)
        writer.writeheader()
        for i in range(len(kunden_ids)):
            for j in range(i + 1, len(kunden_ids)):
                print(kunden_ids)
                if kunden_ids[i] == kunden_ids[j] and leistungs_ids[i] == leistungs_ids[j]:
                    bezeichnungen = hole_bezeichnung(leistungs_ids[i])
                    position += 1
                    anzahl += 1
                    print("test")
                    #for i in range(5):
                    Pos  = position
                    LeistungsID = leistungs_ids[j]
                    Bezeichnung_der_Leistung = bezeichnungen
                    Anzahl = anzahl
                    EinzelPreis = 2

                    writer.writerow({
                        "Pos" : Pos,
                        "LeistungsID" : LeistungsID,
                        "Bezeichnung_der_Leistung" : Bezeichnung_der_Leistung,
                        "Anzahl" : Anzahl,
                        "EinzelPreis" : EinzelPreis
                    })
                        #Ergebnisse erst in Liste dann in csv damit gleiche Werte zusammen gefasst werden
                elif kunden_ids[i] == kunden_ids[j] and leistungs_ids[i] != leistungs_ids[j]:
                    bezeichnung = hole_bezeichnung(leistungs_ids[j])
                    position += 1
                    anzahl = 1
                    Pos  = position
                    LeistungsID = leistungs_ids[j]
                    Bezeichnung_der_Leistung = bezeichnungen
                    Anzahl = anzahl
                    EinzelPreis = 20

                    writer.writerow({
                            "Pos" : Pos,
                            "LeistungsID" : LeistungsID,
                            "Bezeichnung_der_Leistung" : Bezeichnung_der_Leistung,
                            "Anzahl" : Anzahl,
                            "EinzelPreis" : EinzelPreis
                        })
                elif kunden_ids[i] != kunden_ids[j]:
                    bezeichnung = hole_bezeichnung(leistungs_ids[i])
                    position += 1
                    anzahl = 1
                    #for i in range(5):
                    Pos  = position
                    LeistungsID = leistungs_ids[i]
                    Bezeichnung_der_Leistung = bezeichnungen
                    Anzahl = anzahl
                    EinzelPreis = 20

                    writer.writerow({
                            "Pos" : Pos,
                            "LeistungsID" : LeistungsID,
                            "Bezeichnung_der_Leistung" : Bezeichnung_der_Leistung,
                            "Anzahl" : Anzahl,
                            "EinzelPreis" : EinzelPreis
                        })
                    
                
                
                
                       # else:
                           # position = 1
                           # anzahl = 1
                            
                            #erst Liste von Werten machen und dann an dict appenden, sonst werden values jedes mal überschrieben
                            #muss noch ein else schreiben weil manchmal switch
                            #das geht nicht mit dicts!!!! weil key value paar eindeutig...vllt alles direkt in csv schreiben
    
                
def main():

    erstelleRechnung(5)
    my_dict = {'Bla': [], 'Bli': []}
    testding = randrange(5)

    for key in my_dict:
        my_dict['Bla'].append(testding)
    print(my_dict)
            
    
if __name__ == "__main__":
    main()
    

