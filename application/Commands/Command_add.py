from Commands.Command_addSwordsman import *
from Commands.Command_addArcher import *

class Command_add:
    def __init__(self, battlefield):
        self.battlefield = battlefield
        self.commands = {}
        self.commands['swordsman'] = Command_addSwordsman(battlefield)
        self.commands['archer'] = Command_addArcher(battlefield)

    def execute(self,parameters):

        x = int(parameters[3])
        y = int(parameters[4])
        if self.battlefield.field[y][x] == '_':
            if parameters[1] in self.commands:
                self.commands[parameters[1]].execute(parameters)
        else:
            print('the coordinates are already occupied')
