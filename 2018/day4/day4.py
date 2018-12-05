import time
import re
import operator
from collections import Counter

start_time = time.time()

with open("input") as f:
    inp = f.readlines()
inp = sorted([x.strip() for x in inp])

#strategy 1

guardsTotalSleep = {}
guardsMinuteStats = {}
guardID = 0
start = 0

for x in inp:
    data = re.findall('\d+',x)
    if 'Guard' in x:
        guardID = data[5]
        if guardID not in guardsTotalSleep:
            guardsTotalSleep[guardID] = 0
            guardsMinuteStats[guardID] = Counter()
    if 'falls' in x:
        start = int(data[4])
    if 'wakes' in x:
        guardsTotalSleep[guardID] += int(data[4]) - start
        for i in range(start,int(data[4])):
            guardsMinuteStats[guardID][i] += 1

mostSleepyGuard = max(guardsTotalSleep.items(), key=operator.itemgetter(1))[0]
print("=== Strategy 1 ===")
print("#", mostSleepyGuard, ": ", guardsTotalSleep[mostSleepyGuard], " hours slept total")
bestMinute = guardsMinuteStats[mostSleepyGuard].most_common(1)[0][0]
print("Best minute to approach: ", bestMinute)
print("Answer:", (int(mostSleepyGuard) * int(bestMinute)))


#strategy 2

mostSleepyGuard = 0
bestMinute = -1
currentFrequency = 0

for key, stat in guardsMinuteStats.items():
    common = stat.most_common(1)
    
    if( len(common) != 0 and common[0][1] > currentFrequency):
        currentFrequency = common[0][1]
        bestMinute = common[0][0]
        mostSleepyGuard = key

print("=== Strategy 2 ===")
print("#", mostSleepyGuard, "slept on minute", bestMinute, "more than others")
print("Answer:", (int(mostSleepyGuard) * int(bestMinute)))

print("Time elapsed: ", time.time() - start_time)