from collections import Counter
import re
import time

start_time = time.time()

class MarbleRing:
    def __init__(self):
        self.elements = {}
        self.elements[0] = [0,0] # each element will have a list of two values: 'previous' and 'next' element index

    def insertAfter(self, index, item):
        # Don't allow same index inserting so we don't break relations
        if( item not in self.elements):
            prevel = self.elements[index]
            nextel = self.elements[prevel[1]]
            self.elements[item] = [nextel[0],prevel[1]]
            prevel[1] = item
            nextel[0] = item
            return self.elements[item]
        else:
            return None

    def removeItem(self, index):
        this = self.elements[index]
        previdx = this[0]
        nextidx = this[1]
        prevel = self.elements[previdx]
        nextel = self.elements[nextidx]
        del self.elements[index]
        prevel[1] = nextidx
        nextel[0] = previdx

    def getRight(self, start, n):
        if n < 1:
            return start

        current = self.elements[start]
        for i in range(n-1):
            current = self.elements[current[1]]

        # we traverse to the element before the target one and return the 'next' index
        return current[1]

    def getLeft(self, start, n):
        if n < 1:
            return start

        current = self.elements[start]
        for i in range(n-1):
            current = self.elements[current[0]]

        # we traverse to the element before the target one and return the 'previous' index
        return current[0]

    def getElement(self, index):
        return self.elements[index]
    
    def getElements(self):
        return self.elements

    def getOrder(self, start):
        order = [start]
        current = self.elements[start]
        while current[1] != start:
            order.append(current[1])
            current = self.elements[current[1]]
        return order
        

def turnGenerator(max):
    while True:
        for i in range(max):
            yield i


def game_on(players: int, marbles: int) -> int:
    scores = Counter()
    turn = turnGenerator(players)
    SCORING_MARBLE = 23
    current_marble = 0
    ring = MarbleRing()

    for n in range(players):
        scores[n] = 0

    for marble in range(1,marbles+1):
        current_turn = next(turn)

        if( marble % SCORING_MARBLE == 0 ):
            # calculate score
            scores[current_turn] += marble
            toRemove = ring.getLeft(current_marble,7)
            scores[current_turn] += toRemove
            current_marble = ring.getElement(toRemove)[1]
            ring.removeItem(toRemove)

        else:
            #place marble
            after = ring.getRight(current_marble,1)
            ring.insertAfter(after,marble)
            current_marble = marble     

    return max(scores.values())

# test data
assert game_on(9,25) == 32
assert game_on(9,48) == 63
assert game_on(10,1618) == 8317
assert game_on(13,7999) == 146373
assert game_on(17,1104) == 2764
assert game_on(21,6111) == 54718
assert game_on(30,5807) == 37305


with open("input") as f:
    data = [int(x) for x in re.findall("\d+",f.readline())]

print( "Highscore with",data[0], "players and highest marble",data[1],":", game_on(data[0],data[1]))
print( "Highscore with",data[0], "players and highest marble",data[1]*100,":",game_on(data[0],data[1]*100))

print("Time elapsed: ", time.time() - start_time)