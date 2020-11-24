from Soldiers.Infantryman import *

class Archer(Infantryman):
    def __init__(self, x_coordinates, y_coordinates, health, attack, battlefield, army):
        self.x = x_coordinates
        self.y = y_coordinates
        self.health = health
        self.attack = attack
        self.battlefield = battlefield
        self.army = army
        self.alive = True
        self.type = 'archer'
        self.kills = 0

    def move(self,closestEnemyObject):
        self.battlefield.field[self.y][self.x] = '.'

        enemyX = closestEnemyObject.x
        enemyY = closestEnemyObject.y

        closestEnemyXY = abs(self.x - enemyX) + abs(self.y - enemyY)

        if closestEnemyXY > 8:
            if self.x > enemyX:
                self.x = self.x - 1
            elif self.x < enemyX:
                self.x = self.x + 1
            if self.y > enemyY:
                self.y = self.y - 1
            elif self.y < enemyY:
                self.y = self.y + 1
        else:
            randomMult = random.choice([1, 1, 1, 1, 2])
            print(f'{self.army} {self.type} - {self.health}hp strikes '
                  f'{closestEnemyObject.army} {closestEnemyObject.type} - {closestEnemyObject.health}hp, causing {self.attack*randomMult} points of damage')
            closestEnemyObject.health = closestEnemyObject.health - self.attack*randomMult
            if closestEnemyObject.health <= 0:
                print(f'{closestEnemyObject.army} {closestEnemyObject.type} is killed by {self.army} {self.type}')
                self.kills = self.kills + 1
                self.battlefield.armies[closestEnemyObject.army].casualties += 1
                closestEnemyObject.alive = False
                self.battlefield.armies['dead'].soldiers.append(closestEnemyObject)
                self.battlefield.armies[closestEnemyObject.army].soldiers.remove(closestEnemyObject)

        self.battlefield.update()
