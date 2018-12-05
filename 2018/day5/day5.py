import time
import re
from string import ascii_lowercase

starttime = time.time()

#part 1

def reactPolymer(poly):
    while True:
        process = re.subn(r"(.)(?!\1)(?i:\1)", '', poly)
        poly = process[0]
        if process[1] == 0: break
    return poly

with open("input") as f:
    poly = f.readline()

poly = reactPolymer(poly)

print("Polymer length after reaction:", len(poly))

bestLength = len(poly)
for letter in ascii_lowercase:
    tested = re.sub("("+letter+")", '', poly, flags=re.IGNORECASE)
    tested = reactPolymer(tested)
    if(len(tested) < bestLength ) : bestLength = len(tested)

print("Best possible length:", bestLength)

print("Time elapsed: ", time.time() - starttime)