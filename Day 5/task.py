def parseInput(file: str) -> tuple[list[tuple[int, int]], list[int]]:
    with open(file) as f:
        ranges = []
        while (line := f.readline()) != '\n':
            ranges.append(list(map(lambda x: int(x), line.strip().split('-'))))
        
        ids = [int(line) for line in f.readlines()]

        return ranges, ids


def checkIfNumberInRanges(number: int, ranges: list[tuple[int, int]]) -> bool:
    for range in ranges:
        if number >= range[0] and number <= range[1]:
            return True
    else:
        return False


def checkAllNumbers(numbers: list[int], ranges: list[tuple[int, int]]) -> list[int]:
    numbersInRanges = []
    for number in numbers:
        if checkIfNumberInRanges(number, ranges):
            numbersInRanges.append(number)

    return numbersInRanges


def countNumbersInRanges(file: str) -> int:
    ranges, numbers = parseInput(file)
    return len(checkAllNumbers(numbers, ranges))


print(countNumbersInRanges('input.txt'))
