import time

start_time = time.time()

with open("input") as f:
    data = f.readline()
data = [int(x) for x in data.split(" ")]

def getinput(data):
    for x in data:
        yield x
    return None

# === Part One ===
    
def calculateSum(gen) -> int:
    child_nodes = next(gen)
    metadata = next(gen)

    sum = 0

    for i in range(child_nodes):
        sum += calculateSum(gen)

    for i in range(metadata):
        value = next(gen)
        sum += value
    
    return sum

print("The sum of all metadata entries:",calculateSum(getinput(data)))

# === Part Two ===

def calculateComplicatedSum(gen) -> int:
    child_nodes_count = next(gen)
    metadata_count = next(gen)

    child_nodes = []
    sum = 0

    if( child_nodes_count > 0) :
        for i in range(child_nodes_count):
            child_nodes.append( calculateComplicatedSum(gen) )
        for i in range(metadata_count):
            index = next(gen) - 1
            if( index >= 0 and index < len(child_nodes) ):
                sum+=child_nodes[index]
    else:
        for i in range(metadata_count):
            sum += next(gen)
    return sum

print("The value of the root node:",calculateComplicatedSum(getinput(data)))

print("Time elapsed: ", time.time() - start_time)