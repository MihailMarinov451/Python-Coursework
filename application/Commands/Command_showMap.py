import sys
import random

class Command_showMap:
    def __init__(self, battlefield):
        self.battlefield = battlefield

    def execute(self,parameters):
        self.battlefield.print()