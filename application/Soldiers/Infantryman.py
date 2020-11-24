import random

class Infantryman:

    def __init__(self,x_coordinates,y_coordinates, health, attack, battlefield, army):
        self.x = x_coordinates
        self.y = y_coordinates
        self.health = health
        self.attack = attack
        self.battlefield = battlefield
        self.army = army
        self.alive = True
        self.type = 'swordsman'
        self.kills = 0

    def move(self,closestEnemyObject):
        self.battlefield.field[self.y][self.x] = '.'

        enemyX = closestEnemyObject.x
        enemyY = closestEnemyObject.y

        closestEnemyXY = abs(self.x - enemyX) + abs(self.y - enemyY)

        if closestEnemyXY != 0:
            if self.x > enemyX:
                self.x = self.x - 1
            elif self.x < enemyX:
                self.x = self.x + 1
            if self.y > enemyY:
                self.y = self.y - 1
            elif self.y < enemyY:
                self.y = self.y + 1
        else:
            randomMult = random.choice([1,1,1,1,2])
            print(f'{self.army} {self.type} - {self.health}hp strikes '
                  f'{closestEnemyObject.army} {closestEnemyObject.type} - {closestEnemyObject.health}hp, causing {self.attack*randomMult} of damage')
            closestEnemyObject.health = closestEnemyObject.health - self.attack*randomMult
            if closestEnemyObject.health <= 0:
                print(f'{closestEnemyObject.army} {closestEnemyObject.type} is killed by {self.army} {self.type}')
                self.kills = self.kills + 1
                self.battlefield.armies[closestEnemyObject.army].casualties += 1
                closestEnemyObject.alive = False
                self.battlefield.armies['dead'].soldiers.append(closestEnemyObject)
                self.battlefield.armies[closestEnemyObject.army].soldiers.remove(closestEnemyObject)

        self.battlefield.update()

    def act(self):
        armies = self.battlefield.armies
        closestEnemyXY = 1000
        closestEnemyObject = Infantryman(self.x,self.y,0,0,self.battlefield,self.army)
        closestEnemyObject.alive = False

        for i1 in armies:
            if i1 != self.army:
                for i2 in armies[i1].soldiers:
                    distance = abs(self.x-i2.x)+abs(self.y - i2.y)
                    if (distance < closestEnemyXY) and i2.alive == True:
                        closestEnemyXY = distance
                        closestEnemyObject = i2

        if closestEnemyObject.alive == True:
            self.move(closestEnemyObject)