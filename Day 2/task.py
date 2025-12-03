from typing import Callable


def parseInput(file: str) -> list[list[str]]:
    with open(file) as f:
        return [r.split('-') for r in f.readline().strip().split(',')]
    

# checks if the number consists of two repeated sequences of digits, like 1212 or 34563456
def isInvalidIdV1(number: str) -> bool:
    if len(number) % 2 == 1:
        return False
    
    if number == number[:len(number) // 2] * 2:
        return True
    return False


# checks if the number consists of any number of repeated sequences of digits, like 121212, 333, 100100100100
def isInvalidIdV2(number: str) -> bool:    
    for subLength in range(1, len(number) // 2 + 1):
        if number == number[:subLength] * (len(number) // subLength):
            return True
        
    return False


def getInvalidIdsInRange(idsRange: list[str], validityChecker: Callable[[str], bool]) -> list[int]:
    return [number for number in range(int(idsRange[0]), int(idsRange[1]) + 1) if validityChecker(str(number))]


def sumInvalidIdsInRanges(file: str, validityChecker: Callable[[str], bool]) -> int:
    ranges = parseInput(file)
    ids = []
    for range in ranges:
        ids += getInvalidIdsInRange(range, validityChecker)
    
    return sum(ids)


print(sumInvalidIdsInRanges('input.txt', isInvalidIdV1))
print(sumInvalidIdsInRanges('input.txt', isInvalidIdV2))