from enum import IntEnum
from pathlib import Path


class Moves(IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    def __gt__(self, other):
        if self == other:
            return False
        elif self == self.ROCK and other == self.SCISSORS:
            return True
        elif self == self.PAPER and other == self.ROCK:
            return True
        elif self == self.SCISSORS and other == self.PAPER:
            return True
        return False


mapping = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3,
}

LOSE = 0
DRAW = 3
WIN = 6

total = 0
with Path(__file__).parent.joinpath("day2_input.txt").open("r") as f:
    for line in f.readlines():
        opponent, _, you = line.partition(" ")

        opponent, you = Moves(mapping[opponent]), Moves(mapping[you.strip()])

        if you > opponent:
            t_total = you + WIN
            print("win", t_total)
        elif you == opponent:
            t_total = you + DRAW
            print("draw", t_total)
        else:
            t_total = you + LOSE
            print("lose", t_total)

        total += t_total

    print("total", total)
