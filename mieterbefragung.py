einkommen_miete = [[4200,1200],[900,340],[1800,600],[3600,1100],[2700,800],[5900,1300]]

def prozente(anzahlGruppen,staffelung):

    output = []
    
    #prozentualer Anteil der Miete am Einkommen berechnen
    for miete in einkommen_miete:
        miete[1] = miete[1] /miete[0] * 100

    #Einkommensgruppe berechnen
    for data in einkommen_miete:
        if data[0]/staffelung >= anzahlGruppen:
            data[0] = int(anzahlGruppen - 1)
        else: data[0] = int(data[0]/staffelung)
        
    #bubble sort kleinste Einkommensgruppe zuerst
    tausche = 1
    while(tausche != 0):
        tausche = 0
        for i in range (0,len(einkommen_miete)-1):
            if einkommen_miete[i][0] > einkommen_miete[i+1][0]:
                tausche += 1
                temp = einkommen_miete[i][0]
                einkommen_miete[i][0] = einkommen_miete[i+1][0]
                einkommen_miete[i+1][0] = temp
    
    #wenn eine Einkommensgruppe doppelt vorkommt, soll sie nicht ans output Array angehangen werden
    seen = set()
    for x in einkommen_miete:
        if x[0] not in seen:
            output.append(x[1])
            seen.add(x[0])
    return output 
            
def main():
    staffelung = 1000
    anzahlGruppen = 5
    test = prozente(anzahlGruppen,staffelung)
    print(test)
    
if __name__ == "__main__":
    main()
 
