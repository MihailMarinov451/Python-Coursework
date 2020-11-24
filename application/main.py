from CommandExecutor import *
from Battlefield import *



def introduction():
    print('Welcome to Medieval War Simulator')
    print()
    print('In this program you will be given a battlefield upon which you will be able to deploy\n'
          'soldiers for two opposing armies - red and blue. After you have finished with all preparations,\n'
          'you will be able to initiate the simulation and observe the results.\n')
    print('Type \'help\' for more information.\n')


def initializeObjects(battlefield):
    battlefield.addEntity('dead', Army('dead', 'X', battlefield))
    battlefield.addEntity('red', Army('red', 'R', battlefield))
    battlefield.addEntity('blue', Army('blue', 'B', battlefield))


def programExecute():
    battlefield = Field()
    initializeObjects(battlefield)
    commandExe = CommandExecutor()
    introduction()
    commandExe.addAttribute('battlefield',battlefield)
    commandExe.execute()


if __name__ == '__main__':
    programExecute()

