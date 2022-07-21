einkommen_miete = [[4200,1200],[900,340],[1800,600],[3600,1100],[2700,800],[5900,1300]]



def prozente(anzahlGruppen,staffelung):
    #Gruppierung der Einkommensgruppen
    #Berechnung prozentualer Anteil der Miete
    bereich_euro = []
    test = 0
    einkommensgruppe = 0

    for i in range(0,anzahlGruppen-1):
        test = test + staffelung
        bereich_euro.append(test)
    print(bereich_euro)

    for i in range(0,len(einkommen_miete)):
        print(einkommen_miete[i][0])
        

def main():
    staffelung = 1000
    anzahlGruppen = 5
    test = prozente(anzahlGruppen,staffelung)
    
if __name__ == "__main__":
    main()
 
