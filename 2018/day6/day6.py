import time
import re
from collections import Counter
import operator

start_time = time.time()

def getManhattanDistance(src, dest):
    return abs(src[0] - dest[0]) + abs(src[1] - dest[1])

with open("input") as f:
    coords = f.readlines()
coords = [list(map(int,re.findall(r"\d+",x.strip()))) for x in coords]

# === Part One and Two ===

ignoredAreas = [-1]

maxCoords = max(coords,key=lambda item:item[1])
coordMap = {}
maxDistance = 10000
inMaxDistanceCount = 0

for i in range(maxCoords[0]+1):
    for j in range(0,maxCoords[1]+1):
        distances = {}
        coordMap[str(i)+":"+str(j)] = -1
        totalDistance = 0
        for key, coord in enumerate(coords):
            distance = getManhattanDistance((i,j), coord)
            distances[key] = distance
            totalDistance += distance
            if(i == coord[0] and j == coord[1]):
                coordMap[str(i)+":"+str(j)] = key


        counts = Counter(distances.values())
        best = min(distances.items(), key=operator.itemgetter(1))
        if(counts[best[1]] > 1):
            coordMap[str(i)+":"+str(j)] = -1
        else:
            coordMap[str(i)+":"+str(j)] = best[0]
            if( best[0] not in ignoredAreas and (i==0 or j==0 or i==maxCoords[0] or j==maxCoords[1])):
                ignoredAreas.append(best[0])
        
        if(totalDistance < maxDistance) : inMaxDistanceCount+=1

finiteAreasCount = Counter([x for x in coordMap.values() if x not in ignoredAreas])
largestFiniteArea = max(finiteAreasCount.items(), key=operator.itemgetter(1))
print("Largest finite area is", largestFiniteArea[0],"with a total area of",largestFiniteArea[1])
print("Largest area with total distance to all points below",maxDistance,":",inMaxDistanceCount)

print("Time elapsed: ", time.time() - start_time)