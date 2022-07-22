#artikel sind alle von einem Kunden erfasste gekaufte Waren

rabattierter_preis_gesamt = []

def rabatt_rechner(rabatt,artikel):
    for i in range(0,len(artikel)):
        rabatt_klasse = artikel[i][2]
        einzelpreis = artikel[i][3]
        menge = artikel[i][4]

def main():
    artikel = [[1,"Dünger","A",7.80,2],[2,"Garteneinfassung Granit","B",94.86,20],[3,"Rosen","C",56,3],[4,"Werkzeugset","D",87.50,1],[5,"Fliesen,Feinsteinzeug","B",40,5]]
    rabatt = [["A",2],["B",2.5],["C",7],["D",6],["E",5]]

    result = rabatt_rechner(rabatt,artikel)
    print(result)
    
if __name__ == "__main__":
    main()
