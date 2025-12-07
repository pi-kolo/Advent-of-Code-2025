from collections import Counter

def parseInput(file: str) -> list[str]:
    with open(file) as f:
        return [line.strip() for line in f.readlines()]
    

def countParticleSplits(lines: list[str]) -> int:
    columns = Counter()
    source = lines[0].index('S')
    columns = set([source])
    splits = 0
    for line in lines[1:]:
        for idx, el in enumerate(line):
            if el == '^' and idx in columns:
                splits += 1
                columns.add(idx-1)
                columns.add(idx+1)
                columns.discard(idx)
    return splits


def countParticlePaths(lines: list[str]) -> int:
    source = lines[0].index('S')
    columns = Counter([source])
    for line in lines[1:]:
        for idx, el in enumerate(line):
            if el == '^' and idx in columns:
                columns[idx + 1] += columns[idx]
                columns[idx - 1] += columns[idx]
                columns[idx] = 0
    return columns.total()


print(countParticleSplits(parseInput('input.txt')))

print(countParticlePaths(parseInput('input.txt')))
