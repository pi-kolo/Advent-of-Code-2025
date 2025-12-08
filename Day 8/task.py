def parseInput(file: str) -> list[tuple[int, int, int]]:
    with open(file) as f:
        return [[int(el) for el in line.strip().split(',')] for line in f.readlines()]


def distance(A: tuple[int, int, int], B: tuple[int, int, int]) -> float:
    return ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2 + (A[2] - B[2]) ** 2) ** 0.5


def findClosest(distances: list[float]):
    currIdx, currMin = -1, distances[0]
    for idx, el in enumerate(distances):
        if el <= currMin and el != 0:
            currIdx, currMin = idx, el

    return currIdx, currMin


def connectBoxes(boxes: list[tuple[int, int, int]], limit: int):
    connections = {}
    circuits = []
    distances = []
    for i, box1 in enumerate(boxes):
        for j, box2 in enumerate(boxes):
            if i < j:
                dist = distance(box1, box2)
                connections[dist] = (i, j)
                distances.append(dist)
    
    sortedDistances = sorted(distances)
    for _ in range(limit):
        shortestDistance = sortedDistances.pop(0)
        box1, box2 = connections[shortestDistance]
        firstCircuit: set = set()
        secondCircuit: set = set()
        for circuit in circuits:
            if box1 in circuit:
                firstCircuit = circuit
            elif box2 in circuit:
                secondCircuit = circuit
            if firstCircuit and secondCircuit:
                break
        
        if (len(firstCircuit) > 0 and len(secondCircuit) > 0):
            for el in firstCircuit:
                secondCircuit.add(el)
            firstCircuit.clear()
        elif len(firstCircuit) > 0:
            firstCircuit.add(box2)
        elif len(secondCircuit) > 0:
            secondCircuit.add(box1)
        else:
            circuits.append(set([box1, box2]))

    return [el for el in circuits if len(el) > 0]



def connectBoxesUntilOneCircuit(boxes: list[tuple[int, int, int]]) -> int:
    connections = {}
    circuits = []
    distances = []
    for i, box1 in enumerate(boxes):
        for j, box2 in enumerate(boxes):
            if i < j:
                dist = distance(box1, box2)
                connections[dist] = (i, j)
                distances.append(dist)
    
    sortedDistances = sorted(distances)
    while True:
        shortestDistance = sortedDistances.pop(0)
        box1, box2 = connections[shortestDistance]
        firstCircuit: set = set()
        secondCircuit: set = set()
        for circuit in circuits:
            if box1 in circuit:
                firstCircuit = circuit
            elif box2 in circuit:
                secondCircuit = circuit
            if firstCircuit and secondCircuit:
                break
        
        if (len(firstCircuit) > 0 and len(secondCircuit) > 0):
            for el in firstCircuit:
                secondCircuit.add(el)
            firstCircuit.clear()
        elif len(firstCircuit) > 0:
            firstCircuit.add(box2)
        elif len(secondCircuit) > 0:
            secondCircuit.add(box1)
        else:
            circuits.append(set([box1, box2]))

        if (checkCircuit := [el for el in circuits if len(el) > 0]) and len(checkCircuit) == 1 and len(checkCircuit[0]) == len(boxes):
            return boxes[box1][0] * boxes[box2][0]

    
def countScore(circuits: list[set[int]]) -> int:
    lengths = sorted([len(el) for el in circuits], reverse=True)
    return lengths[0] * lengths[1] * lengths[2]


print(countScore(connectBoxes(parseInput('input.txt'), 1000)))

print(connectBoxesUntilOneCircuit(parseInput('input.txt')))
