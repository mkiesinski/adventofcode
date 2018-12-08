import re
import time
from collections import OrderedDict, Counter

start_time = time.time()

with open("input") as f:
    RAW = f.readlines()
RAW = [x.strip() for x in RAW]

# === Part One ===

def parse_input(lines):
    parsed = []
    for line in lines:
        found = [re.sub("\s", '', x) for x in re.findall(r'[A-Z]\s', line)]
        parsed.append((found[0], found[1]))
    return parsed

def get_preconditions(cond) -> dict:
    preconditions = {}
    for x in cond:
        if(x[1] not in preconditions):
            preconditions[x[1]] = []
        if(x[0] not in preconditions):
            preconditions[x[0]] = []
        preconditions[x[1]].append(x[0])
    return preconditions


def assemble(cond) -> str:
    result = []
    
    preconditions = get_preconditions(cond)

    while(preconditions):
        candidates = [x for x,y in preconditions.items() if not y]
        next_item = min(candidates)

        result.append(next_item)
        for pre in preconditions.values():
            if next_item in pre:
                pre.remove(next_item)

        del preconditions[next_item]

    return "".join(result)

conditions = parse_input(RAW)

print("Assembly order:",assemble(conditions))

# === Part Two ===

BASETIME = 60 # base time of 60s
CHRSHIFT = 64 # shift this much so that A = 1, B = 2 etc

def indexOfFreeWorker(workers):
    for key, worker in workers.items():
        if(worker[1]) == 0: return key
    return None

def getTimeToFinish(value: str):
    return BASETIME + (ord(value) - CHRSHIFT)

def assembleWithWorkers(cond, worker_count) -> int:
    preconditions = get_preconditions(cond)
    workers = {}
    seconds_passed = 0
    
    for i in range(worker_count):
        workers[i] = ['',0]

    while( preconditions ) :
        freeWorker = indexOfFreeWorker(workers)
        candidates = sorted([x for x,y in preconditions.items() if not y])
        while( (freeWorker != None) and candidates ):
            # we got free workers, try to assign them jobs
            next_item = candidates.pop(0)
            workers[freeWorker] = [next_item, getTimeToFinish(next_item)]
            del preconditions[next_item]
            freeWorker = indexOfFreeWorker(workers)

        # check what items have been done and reduce time spent
        for worker in workers.values():
            if(worker[1] != 0):
                worker[1] -= 1
                # check if item is done
                if( worker[1] == 0):
                    for pre in preconditions.values():
                        if worker[0] in pre:
                            pre.remove(worker[0])

        #print("second:", seconds_passed," - ",workers)
        seconds_passed += 1
    
    for worker in workers.values():
        seconds_passed += worker[1]
            
    return seconds_passed


print("Assembly time with 5 workers:", assembleWithWorkers(conditions, 5))

print("Time elapsed: ", time.time() - start_time)