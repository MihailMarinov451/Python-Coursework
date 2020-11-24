class Command_showCommands:
    def execute(self,parameters):
        print('help - shows information')
        print('view - shows battlefield')
        print('add [swordsman/archer] [army name(red/blue)] [x coordinate 0-19] [y coordinate 0-19] [health] [damage] - adds combat unit')
        print('\"add swordsman red 2 5 50 10\"')
        print('simulate - initiates the simulation')
        print('example - simulates pre-made combat scenario')