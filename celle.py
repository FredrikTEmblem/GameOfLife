
class Celle:

    def __init__(self):
        self._celle = "doed"            # Cellen settes til død til å starte med.

    def settDoed(self):         # Metoden setter cellen til død og returnerer statusen.
        self._celle = "doed"
        return self._celle

    def settLevende(self):      # Metoden setter cellen til levende og returnerer statusen.
        self._celle = "levende"
        return self._celle

    def erLevende(self):        # Metoden sjekker om cellen er død eller levende.
        if self._celle == "levende":
            return True
        else:
            return False

    def representasjon(self):       # Hvis erLevende = True. Altså at cellen er levende,
        if self.erLevende() == True:
            return "O"                  # skal den printe ut "O". Er cellen død skal den printe ut "."
        else:
            return "."
