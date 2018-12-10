import re
import time

start_time = time.time()

class Star:
    def __init__(self, x,y,vx,vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def drift(self, sec: int):
        self.x += self.vx * sec
        self.y += self.vy * sec

def getBounds(stars) -> tuple:

    x_min = min([x.x for x in stars])
    x_max = max([x.x for x in stars])

    y_min = min([x.y for x in stars])
    y_max = max([x.y for x in stars])    

    return (x_min, x_max, y_min, y_max)

def getArea(bounds) -> int:
    return (bounds[1] - bounds[0]) * (bounds[3] - bounds[2])

def printMessage(stars):
    bounds = getBounds(stars)
    coords = set()
    for star in stars:
        coords.add((star.x, star.y))

    grid = [['#' if (x, y) in coords else '.'
             for x in range(bounds[0]-1, bounds[1] + 2)]
            for y in range(bounds[2]-1, bounds[3] + 2)]

    return "\n".join("".join(row) for row in grid)

def getMessage(lines):
    stars = []
    second = 0
    for line in lines:
        stars.append( Star(line[0],line[1],line[2],line[3]) )

    bounds = getBounds(stars)
    currentArea = getArea(bounds)
    previousArea = currentArea

    while currentArea <= previousArea:
        second += 10
        for star in stars:
            star.drift(10)

        bounds = getBounds(stars)
        previousArea = currentArea
        currentArea = previousArea
        currentArea = getArea(bounds)

    second -= 10
    for star in stars:
        star.drift(-10)
    currentArea = previousArea
    previousArea = currentArea

    while currentArea <= previousArea:
        second += 1
        for star in stars:
            star.drift(1)    

        bounds = getBounds(stars)
        previousArea = currentArea
        currentArea = previousArea
        currentArea = getArea(bounds)

    second -=1
    for star in stars:
        star.drift(-1)

    print("Message appears on second ", second)
    print(printMessage( stars ))


with open("input") as f:
    RAW = f.readlines()
lines = [list(map(int,re.findall(r"[+-]?\d+",x.strip()))) for x in RAW ]

getMessage(lines)

print("Time elapsed: ", time.time() - start_time)