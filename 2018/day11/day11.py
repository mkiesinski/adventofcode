import time
import numpy as np

start_time = time.time()

def getPowerLevel(x, y, serial):
    return ((((x+10)*y + serial)*(x+10))//100)%10 - 5

assert getPowerLevel(122,79,57) == -5
assert getPowerLevel(217,196,39) == 0
assert getPowerLevel(101,153,71) == 4

GRID_SIZE = 300

def getAreaSum(x,y,size,SAT):
    asum = SAT[x+size-1][y+size-1]

    if( x > 0 ):
        asum -= SAT[x-1][y+size-1]
    if( y > 0):
        asum -= SAT[x+size-1][y-1]
    if( x>0 and y>0):
        asum += SAT[x-1][y-1]

    return asum


def getBestAreaForSize(size, SAT):
    values = [(x+1,y+1,getAreaSum(x,y,size,SAT),size) for x in range(GRID_SIZE - size+1) for y in range(GRID_SIZE-size+1)]
    return max(values,key=lambda item:item[2])

def getAllAreaBest(SAT):
    sizes = []
    for size in range(300):
        sizes.append(getBestAreaForSize(size,SAT))

    return max(sizes,key=lambda item:item[2])

SERIAL = 7989 # the input

cells = [[getPowerLevel(x+1,y+1, SERIAL) for y in range(GRID_SIZE)] for x in range(GRID_SIZE)]
SAT = np.array(cells).cumsum(axis=0).cumsum(axis=1)

print("Best area for size of 3:", getBestAreaForSize(3,SAT))

print("Best area for any size:", getAllAreaBest(SAT))

print("Time elapsed: ", time.time() - start_time)