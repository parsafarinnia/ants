import random, matplotlib
import matplotlib.pyplot as plt
import numpy as np
class Ant:
    direction  = 1
    hungry =True
    x = 50
    y = 50

    def __init__(self):

        self.direction = random.randint(1 , 4)
        self.hungry = True
    def nextMove(self):
        self.direction = random.randint(1, 4)
        #1 rast
        if self.direction == 1:
            return [1, 0]
        #bala
        if self.direction == 2:
            return [0, 1]
        #chap
        if self.direction == 3:
            return [-1, 0]
        #payin
        if self.direction == 4:
            return [0, -1]

class Map:
    mapSize = [100, 100]
    rewardSize = [15, 15]
    houseSize = [30, 30]
    map = [[ 1 for x in range(mapSize[0])] for y in range(mapSize[1])]
    rewardX = random.randint(0,mapSize[0]-rewardSize[0]-1)
    rewardY = random.randint(0,mapSize[1]-rewardSize[1]-1)
    houseX = random.randint(0,mapSize[0]-houseSize[0]-1)
    houseY = random.randint(0, mapSize[0] - houseSize[1] - 1)
    # 1 free
    # 2 ant
    # 3 food
    # 4 house
    def setReward(self):
        print (self.rewardX)
        print (self.rewardY)
        for x in range (self.rewardX,self.rewardX+self.rewardSize[0]):
            for y in range(self.rewardY,self.rewardY+self.rewardSize[1]):
                self.map[x][y] = 3
    def setHouse (self):
        print (self.houseX)
        print (self.houseY)
        for x in range(self.houseX, self.houseX + self.houseSize[0]):
            for y in range(self.houseY, self.houseY + self.houseSize[1]):
                self.map[x][y] = 3

def main():

    map = Map()

    map.setReward()
    while not (map.houseX< map.rewardX <map.houseX+map.rewardSize[0] and  map.houseY< map.rewardY <map.houseY.+map.rewardSize[1] ):
        a=map.mapSize[0] - map.rewardSize[0] - 1
        b=map.mapSize[1] - map.rewardSize[1] - 1
        map.rewardX = random.randint(0, a)
        map.rewardY = random.randint(0,b)
    map.setReward()

    asghar = Ant()
    print ('x asghar :', asghar.x , ' y asghar :',asghar.y , ' reward x :', map.rewardX ,' reward y :' , map.rewardY)

    moveX = []
    moveY = []
    for x in range(100):
            nextMoveX = asghar.nextMove()[0] + asghar.x
            nextMoveY = asghar.nextMove()[1] + asghar.y
            # print ('x', asghar.x, ' y', asghar.y)
            while not (-1<nextMoveX <map.mapSize[0] and -1<nextMoveY <map.mapSize[1]):
                # print ('fuck   x',asghar.x,' y',asghar.y)
                nextMoveX = asghar.nextMove()[0] +asghar.x
                nextMoveY = asghar.nextMove()[1] + asghar.y
            if (map.map[asghar.x][asghar.y]) == 3:
                asghar.hungry= False
            if ( not asghar.hungry) and (map.map[asghar.x][asghar.y] == 4 ):
                nextMoveX = asghar.x
                nextMoveY = asghar.y
            asghar.x=nextMoveX
            asghar.y=nextMoveY
            moveX.append(asghar.x)
            moveY.append(asghar.y)
    print (asghar.hungry)
    plt.figure()
    plt.plot(moveX, moveY, lw=3)
    plt.autoscale
    plt.ylabel('some numbers')
    plt.show()

main()