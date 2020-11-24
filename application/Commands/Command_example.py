from Commands.Command_showMap import *
from Commands.Command_showCommands import *
from Commands.Command_add import *
from Commands.Command_simulate import *

class Command_example:
    def __init__(self, battlefield, attributes):
        self.battlefield = battlefield
        self.attributes = attributes

    def execute(self,parameters):
        commands = {}
        commands['view'] = Command_showMap(self.attributes['battlefield'])
        commands['help'] = Command_showCommands()
        commands['add'] = Command_add(self.attributes['battlefield'])
        commands['simulate'] = Command_simulate(self.attributes['battlefield'])



        inpTemp = 'add swordsman blue 2 5 50 10'
        inp1Temp = inpTemp.split()
        commands[inp1Temp[0]].execute(inp1Temp)
        inpTemp = 'add swordsman blue 2 7 50 10'
        inp1Temp = inpTemp.split()
        commands[inp1Temp[0]].execute(inp1Temp)
        inpTemp = 'add swordsman blue 2 9 50 10'
        inp1Temp = inpTemp.split()
        commands[inp1Temp[0]].execute(inp1Temp)
        inpTemp = 'add swordsman blue 2 11 50 10'
        inp1Temp = inpTemp.split()
        commands[inp1Temp[0]].execute(inp1Temp)
        inpTemp = 'add swordsman blue 2 13 50 10'
        inp1Temp = inpTemp.split()
        commands[inp1Temp[0]].execute(inp1Temp)
        inpTemp = 'add swordsman blue 2 15 50 10'
        inp1Temp = inpTemp.split()
        commands[inp1Temp[0]].execute(inp1Temp)


        inpTemp = 'add swordsman red 17 5 50 10'
        inp1Temp = inpTemp.split()
        commands[inp1Temp[0]].execute(inp1Temp)
        inpTemp = 'add swordsman red 17 7 50 10'
        inp1Temp = inpTemp.split()
        commands[inp1Temp[0]].execute(inp1Temp)
        inpTemp = 'add swordsman red 17 9 50 10'
        inp1Temp = inpTemp.split()
        commands[inp1Temp[0]].execute(inp1Temp)
        inpTemp = 'add swordsman red 17 11 50 10'
        inp1Temp = inpTemp.split()
        commands[inp1Temp[0]].execute(inp1Temp)
        inpTemp = 'add swordsman red 17 13 50 10'
        inp1Temp = inpTemp.split()
        commands[inp1Temp[0]].execute(inp1Temp)
        inpTemp = 'add swordsman red 17 15 50 10'
        inp1Temp = inpTemp.split()
        commands[inp1Temp[0]].execute(inp1Temp)


        inpTemp = 'add archer blue 0 7 40 5'
        inp1Temp = inpTemp.split()
        commands[inp1Temp[0]].execute(inp1Temp)
        inpTemp = 'add archer blue 0 9 40 5'
        inp1Temp = inpTemp.split()
        commands[inp1Temp[0]].execute(inp1Temp)
        inpTemp = 'add archer blue 0 11 40 5'
        inp1Temp = inpTemp.split()
        commands[inp1Temp[0]].execute(inp1Temp)
        inpTemp = 'add archer blue 0 13 40 5'
        inp1Temp = inpTemp.split()
        commands[inp1Temp[0]].execute(inp1Temp)

        inpTemp = 'add archer red 19 7 40 5'
        inp1Temp = inpTemp.split()
        commands[inp1Temp[0]].execute(inp1Temp)
        inpTemp = 'add archer red 19 9 40 5'
        inp1Temp = inpTemp.split()
        commands[inp1Temp[0]].execute(inp1Temp)
        inpTemp = 'add archer red 19 11 40 5'
        inp1Temp = inpTemp.split()
        commands[inp1Temp[0]].execute(inp1Temp)
        inpTemp = 'add archer red 19 13 40 5'
        inp1Temp = inpTemp.split()
        commands[inp1Temp[0]].execute(inp1Temp)



        inpTemp = 'simulate'
        inp1Temp = inpTemp.split()
        commands[inp1Temp[0]].execute(inp1Temp)


