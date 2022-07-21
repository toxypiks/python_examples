einkommen_miete = [[4.200,1.200],[900,340],[1.800,600],[3.600,1.100],[2.700,800],[5.900,1.300]]



def prozente(anzahlGruppen,staffelung):
    #Gruppierung der Einkommensgruppen
    #Berechnung prozentualer Anteil der Miete
    einkommensgruppen = []
    test = 0

    for i in range(0,anzahlGruppen):
        test = test + staffelung
        einkommensgruppen.append(test)
    print(einkommensgruppen)

def main():
    staffelung = 1000
    anzahlGruppen = 5
    test = prozente(anzahlGruppen,staffelung)
    
if __name__ == "__main__":
    main()
 
