#!/usr/bin/env python3

from collections import defaultdict
from sys import stdin
from typing import Dict, List, Tuple

# Maximum average distance between a digit and all other digits observed at the
# given position for the digit to become a position candidate (be used to
# generate final guesses).
MAX_SCORE = 2.5

# Maximum number of candidate digits per position.
# The upper limit on the number guesses produced is MAX_CAND ** NUM_OF_DIGITS,
# down from 10 ** NUM_OF_DIGITS for straight up brute force.
MAX_CAND = 5

Pos = int # digit position
Digit = int
Count = int
Distance = int
Score = float
Scores = List[Tuple[Score, Digit]] # sorted
DigitCounts = Dict[Digit, Count]
PosDigitCounts = Dict[Pos, DigitCounts]
PosCandidates = List[Digit]
Candidates = List[PosCandidates]

def input() -> PosDigitCounts:
    ret : PosDigitCounts = defaultdict(lambda: defaultdict(lambda: 0))
    for line in stdin:
        for pos, digit in enumerate(line.strip()):
            ret[pos][int(digit)] += 1
    return ret

def candidates(input : PosDigitCounts) -> Candidates:
    pos_count = len(input)
    sample_count = sum(count for count in input[0].values())

    def distance(a : Digit, b : Digit) -> Distance:
        return min((a - b) % 10, (b - a) % 10)

    def score(a : Digit, counts : DigitCounts) -> Score:
        return sum(distance(a, digit) * count for digit, count in counts.items()) \
             / sample_count

    def scores(counts : DigitCounts) -> Scores:
        return sorted((score(digit, counts), digit) for digit in range(10))

    return [[digit for score, digit in scores(input[pos]) if score <= MAX_SCORE][:MAX_CAND]
            for pos in range(pos_count)]

def main() -> None:
    def print_guesses(candidates : Candidates, i = 0, acc = "") -> None:
        if i == len(candidates):
            print(acc)
        else:
            for digit in candidates[i]:
                print_guesses(candidates, i + 1, acc + str(digit))

    print_guesses(candidates(input()))

if __name__ == "__main__":
    main()
