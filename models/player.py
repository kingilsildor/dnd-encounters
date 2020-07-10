class Party:
    def __init__(self, size, partyName, averagePartyLvl):
        self.size = size
        self.partyName = partyName
        self.averagePartyLvl = averagePartyLvl

def showParty():
     pass

def averageLvl():
    pass

class Player(Party):
    def __init__(self, name, lvl, characterClass):
        Party.__init__(self)


