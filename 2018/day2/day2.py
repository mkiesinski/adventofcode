import time

start_time = time.time()

with open("input") as f:
    boxes = f.readlines()
boxes = [x.strip() for x in boxes]

double = 0
triple = 0

# === Part One ===

for box in boxes:
    cnt = {}
    for letter in box:
        if not letter in cnt:
            cnt[letter] = 1
        else:
            cnt[letter] += 1
    if 2 in cnt.values():
        double += 1
    if 3 in cnt.values():
        triple += 1

print("List checksum:", double*triple)

# === Part Two ===

def compare(str1, str2):
    diff = ''
    for i in range(0,len(str1)):
        if( str1[i] == str2[i]):
            diff += str1[i]
    return diff

found = False
for b1i in range(0,len(boxes)):
    for b2i in range(b1i + 1, len(boxes)) :
        compared = compare(boxes[b1i],boxes[b2i])
        if( len(boxes[b1i]) - len(compared) == 1):
            found = True
            break
    if found: break

print("Common letters: " + compared)
            
print("Time elapsed: ", time.time() - start_time)