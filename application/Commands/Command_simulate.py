import sys
import random
from Commands.Command_showMap import *
class Command_simulate:
    def __init__(self,battlefield):
        self.battlefield = battlefield


    def showStatistics(self):
        print()
        print('Battle stats:')
        print()
        print('Surviors:')
        for i1 in self.battlefield.armies:
            for i2 in self.battlefield.armies[i1].soldiers:
                if i2.alive == True:
                    print(f'{i2.army} {i2.type} - {i2.health}hp - kills: {i2.kills}')
        print()

        for i1 in self.battlefield.armies:
            if i1 != 'dead':
                print(f'{i1} army casualties: {self.battlefield.armies[i1].casualties}')




        wait = input()
        sys.exit()

    def checkTeams(self):
        if len(self.battlefield.armies['red'].soldiers) == 0:
            print('The blue army wins.')
            self.showStatistics()

        elif len(self.battlefield.armies['blue'].soldiers) == 0:
            print('The red army wins')
            self.showStatistics()



    def execute(self,parameters):
        loop = True
        armies = self.battlefield.armies
        turn = 1

        print('Battle participants:')
        for i1 in self.battlefield.armies:
            for i2 in self.battlefield.armies[i1].soldiers:
                if i2.alive == True:
                    print(f'{i2.army} {i2.type} - health: {i2.health}hp - damage: {i2.attack}p')
        print()

        self.battlefield.print()
        while loop:
            print('Press Enter for next turn')
            inp = input()
            print()
            print('---------------------------')
            print()
            print(f'Turn {turn}')

            soldiersTemp = []

            for i1 in armies:
                for i2 in armies[i1].soldiers:
                    if i2.alive == True:
                        soldiersTemp.append(i2)

            random.shuffle(soldiersTemp)

            for i1 in soldiersTemp:
                if i1.alive == True:
                    i1.act()


            self.battlefield.print()
            self.checkTeams()
            turn = turn + 1