from Soldiers.Archer import *
from Soldiers.Infantryman import *

class Army:
    def __init__(self, name, map_symbol, battlefield):
        self.name = name
        self.map_symbol = map_symbol
        self.soldiers = []
        self.battlefield = battlefield
        self.casualties = 0

    def addSwordsman(self,x,y,health,attack,army):
        if (x >= 0 and x < 20) and (y >= 0 and y < 20):
            self.soldiers.append(Infantryman(x,y,health,attack,self.battlefield,army))
        else:
            print('invalid coordinates')

    def addArcher(self,x,y,health,attack,army):
        if (x >= 0 and x < 20) and (y >= 0 and y < 20):
            self.soldiers.append(Archer(x,y,health,attack,self.battlefield,army))
        else:
            print('invalid coordinates')