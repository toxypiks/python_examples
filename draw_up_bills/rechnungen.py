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

def erstelleRechnung():
    kunden_ids = []
    leistungs_ids = []
    einzelpreise_liste = []
    anzahl_liste = []

    position = 0
    bezeichnung = ""
    anzahl = 1

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
                if kunden_ids[i] == kunden_ids[j] and leistungs_ids[i] == leistungs_ids[j]:
                    bezeichnungen = hole_bezeichnung(leistungs_ids[i])
                    position += 1
                    anzahl += 1
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
                elif kunden_ids[i] != kunden_ids[j] and leistungs_ids[i] != leistungs_ids[j]:
                    bezeichnung = hole_bezeichnung(leistungs_ids[j])
                    position += 1
                    anzahl = 1
                    Pos  = position
                    LeistungsID = leistungs_ids[j]
                    Bezeichnung_der_Leistung = bezeichnungen
                    Anzahl = anzahl
                    EinzelPreis = 40

                    writer.writerow({
                            "Pos" : Pos,
                            "LeistungsID" : LeistungsID,
                            "Bezeichnung_der_Leistung" : Bezeichnung_der_Leistung,
                            "Anzahl" : Anzahl,
                            "EinzelPreis" : EinzelPreis
                        })
    
                
def main():

    erstelleRechnung()
            
    
if __name__ == "__main__":
    main()
    

