from functools import reduce

def parseInput(file: str):
    with open(file) as f:
        output = []
        for element in f.readline().strip().split():
            output.append([int(element)])
        
        for line in f.readlines():
            for idx, el in enumerate(line.strip().split()):
                output[idx].append(int(el) if el not in ('*', '+') else el)

        return output


def calculate(numbers: list[int], operator: chr) -> int:
    aggFun = (lambda x, y: x * y) if operator == '*' else (lambda x,y: x + y)
    return reduce(aggFun, numbers)


def sumCalcs(data: list[list[int|str]]) -> int:
    return sum(calculate(row[:-1], row[-1]) for row in data)


## part II

def parseInputV2(file: str) -> tuple[list[list[chr], list[chr]]]:
    with open(file) as f:
        rawData = f.readlines()
        numbers = [[] for _ in rawData[0]]
        for y in range(len(rawData) - 1):
            for x in range(len(rawData[0])):
                numbers[x].append(rawData[y][x])
        
        return numbers, rawData[-1].strip().split()


def calcHorizontally(file: str) -> int:
    data, operators = parseInputV2(file)
    counter, opCounter, result = 0, 0, 0
    currentNumbers = []
    while counter < len(data):
        try:
            number = int(''.join(data[counter]))
            currentNumbers.append(number)
            counter += 1
        except:
            result += calculate(currentNumbers, operators[opCounter])
            currentNumbers = []
            counter += 1
            opCounter += 1

    return result


print(sumCalcs(parseInput('input.txt'))) 


print(calcHorizontally('input.txt'))
    