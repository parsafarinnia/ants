import random, matplotlib
import matplotlib.pyplot as plt
import numpy as np
class Ant:
    direction  = 1
    hungry =True
    x = 0
    y = 0

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
    map = [[ None for x in range(mapSize[0])] for y in range(mapSize[1])]


def main():

    # map = Map();
    # houseX = (map.mapSize[0]/2)(int) - (map.rewardSize[0]/2)(int)
    # houseY = (map.mapSize[1]/2)(int) - (map.rewardSize[1]/2)(int)
    # awardX = random.randint(0 ,100)
    # while not (houseX< awardX <houseX+map.rewardSize[0] ):
    #     awardX = random.randint(0, 100)
    # awardY = random.randint(1, 30)
    # while not (houseY< awardY <houseY+map.rewardSize[1] ):
    #     awardY = random.randint(0, 100)
    asghar = Ant()
    moveX = []
    moveY = []
    for x in range(1000):
        asghar.x = asghar.nextMove()[0] +asghar.x
        asghar.y = asghar.nextMove()[1] + asghar.y
        moveX.append(asghar.x)
        moveY.append(asghar.y)
    plt.figure()
    plt.plot(moveX, moveY, lw=3)
    plt.autoscale
    plt.ylabel('some numbers')
    plt.show()

main()