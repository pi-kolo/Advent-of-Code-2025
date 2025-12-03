# counts every time when rotation ends in 0 point
def countZerosAfterRotations(moves: list[str]):
    position = 50
    counter = 0
    for line in moves:
        direction = 1 if line[0] == 'R' else -1
        move = int(line[1:]) % 100
        position = (position + (direction * move)) % 100
        if position == 0:
            counter += 1
    return counter


# counts every time dial points at 0 during rotations
def countZerosDuringRotations(moves: list[str]):
    position = 50
    counter = 0
    for line in moves:
        direction = 1 if line[0] == 'R' else -1
        move = int(line[1:])
        for _ in range(move):
            position += direction
            position = position % 100
            if position == 0:
                counter += 1
    return counter


with open('input.txt') as f:
    print(countZerosAfterRotations(f.readlines()))

with open('input.txt') as f:
    print(countZerosDuringRotations(f.readlines()))
