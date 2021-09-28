from celle import Celle
from spillebrett import Spillebrett

def hovedprogram():
    print("Velkommen ti Game of Life!")
    rader = int(input("Oppgi antall rader du vil ha på spillbrettet ditt: "))
    kolonner = int(input("Oppgi antall kolonner du vil ha på spillbrettet ditt: "))
    spill = Spillebrett(rader,kolonner)
    print(spill.tegnBrett())
    print("Generasjon: " , spill._generasjon)
    print("Antall levende celler: " , spill.finnAntallLevende())


    svar = input("Trykk enter for å gå videre med spillet, trykk q for å avslutte: ")
    while svar != "q":
        spill.oppdatering()
        print(spill.tegnBrett())
        print("Generasjon: " , spill._generasjon)
        print("Antall levende celler: " , spill.finnAntallLevende())
        svar = input("Trykk enter for å gå videre med spillet, trykk q for å avslutte: ")

hovedprogram()
