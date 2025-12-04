from typing import Callable

def parseInput(file: str) -> list[list[str]]:
    with open(file) as f:
        return [list(line.strip()) for line in f.readlines()]
    

def addSurrounding(board: list[str]) -> list[list[str]]:
    result = [['.'] * (len(board[0]) + 2) ]
    for line in board:
        result.append(['.'] + line + ['.'])
    
    result.append(['.'] * (len(board[0]) + 2))
    return result


def checkAdjacents(board: list[str], row: int, col: int, checkFunction: Callable[[chr], bool]) -> int:
    adjacents = [[-1, 0], [-1, -1], [0, -1], [0, 1], [1, 1], [1, 0], [1, -1], [-1, 1]]
    return sum(checkFunction(board[row + adjacent[0]][col + adjacent[1]]) for adjacent in adjacents)


def isValid(el: chr) -> bool: 
    return el == '@'


def checkBoard(file: str) -> int:
    board = addSurrounding(parseInput(file))
    counter = 0
    for y, row in enumerate(board[1:-1], 1):
        for x, el in enumerate(row[1:-1], 1):
            if isValid(el) and checkAdjacents(board, y, x, isValid) < 4:
                counter += 1
    
    return counter


def removeRolls(file) -> int:
    board = addSurrounding(parseInput(file))
    counter = 0
    anyChanges = True
    while anyChanges:
        anyChanges = False
        for y, row in enumerate(board[1:-1], 1):
            for x, el in enumerate(row[1:-1], 1):
                if isValid(el) and checkAdjacents(board, y, x, isValid) < 4:
                    board[y][x] = '.'
                    counter += 1
                    anyChanges = True
        
    return counter


print(checkBoard('input.txt'))

print(removeRolls('input.txt'))