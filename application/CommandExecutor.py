from Commands.Command_showMap import *
from Commands.Command_showCommands import *
from Commands.Command_add import *
from Commands.Command_simulate import *
from Commands.Command_example import *

class CommandExecutor():

    def __init__(self):
        self.attributes = {}

    def addAttribute(self, name, object):
        self.attributes[name] = object

    def execute(self):

        commands = {}
        commands['view'] = Command_showMap(self.attributes['battlefield'])
        commands['help'] = Command_showCommands()
        commands['add'] = Command_add(self.attributes['battlefield'])
        commands['simulate'] = Command_simulate(self.attributes['battlefield'])
        commands['example'] = Command_example(self.attributes['battlefield'], self.attributes)

        loop = True
        while loop == True:
            inpString = input()
            if inpString != '':
                inp = inpString.split()
                if inp[0] in commands:
                    commands[inp[0]].execute(inp)





