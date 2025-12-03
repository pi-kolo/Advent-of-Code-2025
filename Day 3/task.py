from typing import Callable

def parseInput(file: str) -> list[str]:
    with open(file) as f:
        return [line.strip() for line in f.readlines()]


# finds biggest 2-digit number created by picking numbers from sequence (in order)
def findMaxTwoDigitJoltage(seq: str) -> int:
    firstDigitIdx, firstDigit = max(enumerate(seq[:-1]), key=lambda v: v[1])
    secondDigit = max(seq[firstDigitIdx + 1 :])
    return int(firstDigit + secondDigit)


# finds biggest n-digit number created by picking digits from sequence (in order)
def findMaxNDigitJoltage(seq: str, n: int) -> int:
    digits = []
    for i in range(0, n):
        subsequence = seq[0 if i == 0 else digits[i-1][0] + 1 : len(seq) - n + i + 1]
        ithIdx, ithDigit = max(enumerate(subsequence), key=lambda v: v[1])
        offset = 0 if i == 0 else digits[i-1][0] + 1
        digits.append([ithIdx + offset, ithDigit])

    return int(''.join([str(el[1]) for el in digits]))


def sumJoltages(file: str, maxJoltageFunc: Callable[[str], int]) -> int:
    return sum(maxJoltageFunc(battery) for battery in parseInput(file))


print(sumJoltages('input.txt', findMaxTwoDigitJoltage))

print(sumJoltages('input.txt', lambda x: findMaxNDigitJoltage(x, 12)))
