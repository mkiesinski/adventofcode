import re
import time
from collections import OrderedDict

with open("input") as f:
    RAW = f.readlines()
RAW = [x.strip() for x in RAW]

# === Part One

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