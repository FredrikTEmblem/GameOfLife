from random import randint
from celle import Celle


class Spillebrett:
# Oppretter konstruktøren med instansvariabler, og konstruerer et spillbrett
    def __init__(self,rader,kolonner):
        self._rader = rader
        self._kolonner = kolonner
        self._rutenett = []
        self._generasjon = 0
# Konstruerer spillbrettet
        for r in range(rader):                         # Bruker for-løkke for å iterere gjennom antall rader.
            self._rutenett.append([])                  # Bruker append for å legge til en liste for hver rad i rutenettet.
            for k in range(kolonner):                  # Bruker for-løkke for å iterere gjennom kolonnene i radene.
                self._rutenett[r].append(Celle())      # Appender en celle for hver kolonne i alle radene i rutenettet.

        self._generer()              # Kaller på generer i konstruktøren slik at det blir konstruert et tilfeldig spillbrett til å starte med.


    def _generer(self):
        for rader in self._rutenett:            # Bruker for-løkke og går gjennom alle radene i rutenettet.
            for kolonne in rader:               # Bruker nøstet for-løkke for å iterere gjennom alle kolonnene i alle radene.
                tall = randint(0,2)             # Et tilfeldig tall med kommandoen randint legges som en variabel fra 0 til og med 2.
                if tall == 1:                   # Hvis tallet er 1 skal cellen settes levende, gjennom denne strategien har hver celle 1/3
                    kolonne.settLevende()       # for å settes til live når spillbrettet lages.
                else:
                    kolonne.settDoed()

    def tegnBrett(self):
        # Metoden skal skrive ut spillbrettet til terminalen.
        print()
        print("Utskrift av spillebrett: \n")
        for rader in self._rutenett:            # Bruker nøstet for-løkke og itererer gjennom rutenettet.
            for k in rader:
                print(k.representasjon() , " " ,end="")     # Printer ut hver celle gjennom å kalle på metoden
            print("\n")                                     # representasjon fra klassen Celle.

    def finnNabo(self, rad, kolonne):
        # Metoden finner naboene til en celle og legger de i en liste.
        naboliste = []                      # Oppretter en tom liste.
        for r in range(-1,2):
            for k in range(-1,2):           # Iterer gjennom fra og med -1 til og med 1.
                naboRad = rad + r           # Nabo-celle vi maks ligge -1 eller 1 rader/kolonne vekk.
                naboK = kolonne + k         # Oppretter to variabler som tar vare på naboene for hver gang vi iterer gjennom rutenettet.

                status = True               # Foreløpig settes status til True.

                if r == 0 and k == 0:       # Dette er posisjonen til cellen, det vil bli False fordi man ikke kan være sin egen nabo.
                    status = False

                elif naboRad < 0 or naboRad >= self._rader:  # False, fordi det ikke finnes noen rader som er mindre enn 0 eller større enn antall rader.
                    status = False                           # Vil derfor ikke finnes noen naboer, fordi ved disse tilfellene er vi ved utkanten til rutenettet.

                elif naboK < 0 or naboK >= self._kolonner:  # Samme gjelder her for kolonner som over med rader.
                    status = False

                if status:                                              # Gjelder ingen av påstandene over er status gyldig.
                    naboliste.append(self._rutenett[naboRad][naboK])    # Nabocellene til cellen i rutenettet blir lagt inn i listen naboliste.

        return naboliste

    def oppdatering(self):
        # døde celler som skal få status levende
        bli_levende = []
        # levende celler som skal få status død
        bli_doed = []

        for rader in range(self._rader):
            for kolonner in range(self._kolonner):             # Itererer gjennom rutenettet.
                naboListe = self.finnNabo(rader,kolonner)      # Oppretter en naboliste som holder på naboene til cellen.
                levendeNaboer = 0                              # Foreløpig er antall naboer 0.

                for nabo in naboListe:              # Går gjennom alle naboene i listen.
                    if nabo.erLevende() == True:    # Hvis naboen er levende skal variabelen som har kontroll over levende naboer øke med 1.
                        levendeNaboer += 1

                x = self._rutenett[rader][kolonner]     # Oppretter et celle-objekt i rutenettet for rader og kolonner.
                celle_status = x.erLevende()            # Setter celle-objektet lik en annen variabel og sjekker om det celle-objektet er levende eller død.

                if celle_status == True:        # Dette gjelder hvis cellen er levende.
                    if levendeNaboer < 2 or levendeNaboer > 3:      # Har cellen mindre enn 2 naboer eller mer enn 3 naboer,
                        bli_doed.append(x)                          # så skal cellen død. Og legges i bli død listen.

                else:           # Dette gjelder hvis cellen er død.
                    if levendeNaboer == 3:          # Har cellen eksakt 3 naboer som er i live.
                        bli_levende.append(x)       # Så skal den døde cellen bli levende og legges i listen.

        for levende_celler in bli_doed:     # Itererer gjennom bli_doed listen og setter cellene til å bli døde.
            levende_celler.settDoed()

        for dode_celler in bli_levende:     # Itererer gjennom bli_levende listen og setter cellene til å bli levende.
            dode_celler.settLevende()

        self._generasjon += 1           # Når hele koden i oppdatering er kjørt skal generasjonsnummeret øke med 1, dermed er det klart for neste oppdatering av spillbrettet.

    def finnAntallLevende(self):
        # Setter en indeks lik 0, denne holder kontroll over hvor mange celler i spillbrettet som er i live.
        indeks = 0
        for rader in self._rutenett:
            for kolonner in rader:      # Itererer gjennom spillbrettet gjennom en nøstet for-løkke.
                if kolonner.erLevende() == True:
                    indeks += 1     # Hvis cellen er levende øker indeksen med 1.
        return indeks       # Vil til slutt returnerer alle levende celler i spillbrettet.
