einkommen_miete = [[4200,1200],[900,340],[1800,600],[3600,1100],[2700,800],[5900,1300]]



def prozente(anzahlGruppen,staffelung):
    #Gruppierung der Einkommensgruppen
    #Berechnung prozentualer Anteil der Miete
    bereich_euro = []
    einkommen = []
    test = 0
    einkommensgruppe = 0
    einkommensgruppen = []

    for i in range(0,anzahlGruppen-1):
        test = test + staffelung
        bereich_euro.append(test)
    print(bereich_euro)

    for i in range(0,len(einkommen_miete)):
        einkommen.append(einkommen_miete[i][0])

    for value in einkommen:
        if value/staffelung >= anzahlGruppen:
            einkommensgruppen.append(str(anzahlGruppen -1))
        else:
            einkommensgruppen.append((str(value/staffelung)).split(".")[0])
    print(einkommensgruppen)

def main():
    staffelung = 1000
    anzahlGruppen = 5
    test = prozente(anzahlGruppen,staffelung)
    
if __name__ == "__main__":
    main()
 
