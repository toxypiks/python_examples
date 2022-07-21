einkommen_miete = [[4200,1200],[900,340],[1800,600],[3600,1100],[2700,800],[5900,1300]]

def prozente(anzahlGruppen,staffelung):

    output = []

    for miete in einkommen_miete:
        miete[1] = miete[1] /miete[0] * 100

    for data in einkommen_miete:
        if data[0]/staffelung >= anzahlGruppen:
            data[0] = int(anzahlGruppen - 1)
        else: data[0] = int(data[0]/staffelung)
        
    #bubble sort kleinste einkommensgruppe zuerst
    tausche = 1
    while(tausche != 0):
        tausche = 0
        for i in range (0,len(einkommen_miete)-1):
            if einkommen_miete[i][0] > einkommen_miete[i+1][0]:
                tausche += 1
                temp = einkommen_miete[i][0]
                einkommen_miete[i][0] = einkommen_miete[i+1][0]
                einkommen_miete[i+1][0] = temp
    print(einkommen_miete)
    
    #wenn eine einkommensgruppe doppelt vorkommt, soll sie nicht im output array vorkommen        
                
def main():
    staffelung = 1000
    anzahlGruppen = 5
    test = prozente(anzahlGruppen,staffelung)
    
if __name__ == "__main__":
    main()
 
