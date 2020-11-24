class Command_addSwordsman:
    def __init__(self, battlefield):
        self.battlefield = battlefield

    def execute(self,parameters):
        army = parameters[2]
        x = int(parameters[3])
        y= int(parameters[4])
        health = int(parameters[5])
        attack = int(parameters[6])


        if parameters[2] in self.battlefield.armies:
            self.battlefield.getEntity(parameters[2]).addSwordsman(x, y, health, attack,army)
            self.battlefield.update()
