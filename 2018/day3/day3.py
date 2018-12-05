import time
import re

starttime = time.time()

with open("input") as f:
    claims_input = f.readlines()
claims_input = [x.strip() for x in claims_input]

# === Format input ===
claims = {}
for x in claims_input:
    numbers = re.findall('\d+', x )
    claims[numbers[0]] = {
        'x': int(numbers[1]),
        'y': int(numbers[2]),
        'w': int(numbers[3]),
        'h': int(numbers[4])
    }

# === Part One ===

canvas = {}
total = 0

for key, claim in claims.items():
    for i in range(claim['x'],claim['x']+claim['w']):
        for j in range(claim['y'],claim['y']+claim['h']):
            index = str(i) + "x" + str(j)
            if index not in canvas:
                canvas[index] = 1
            else:
                canvas[index] += 1

for x in canvas.values():
    if(x>1): total += 1

print("Total overlaping claims in square inch:", total)

# === Part Two ===

not_overlaping_id = 0

for key, claim in claims.items():
    not_covered = True
    for i in range(claim['x'],claim['x']+claim['w']):
        for j in range(claim['y'],claim['y']+claim['h']):
            index = str(i) + "x" + str(j)
            if canvas[index] > 1:
                not_covered = False
    if not_covered:
        not_overlaping_id = key
        break

print("Claim", not_overlaping_id, "is not overlaping with others")

print("Time elapsed: ", time.time() - starttime)