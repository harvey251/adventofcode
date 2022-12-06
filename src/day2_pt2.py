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

    def win_move(self):
        if self == self.ROCK:
            return self.PAPER
        if self == self.PAPER:
            return self.SCISSORS
        return self.ROCK

    def lose_move(self):
        if self == self.ROCK:
            return self.SCISSORS
        if self == self.PAPER:
            return self.ROCK
        return self.PAPER


mapping = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3,
}

LOSE_VALUE = 0
DRAW_VALUE = 3
WIN_VALUE = 6

LOSE = "X"
DRAW = "Y"
WIN = "Z"

total = 0
with Path(__file__).parent.joinpath("day2_input.txt").open("r") as f:
    for line in f.readlines():
        opponent, _, response = line.partition(" ")

        opponent = Moves(mapping[opponent])
        response = response.strip()

        if response == WIN:
            t_total = opponent.win_move() + WIN_VALUE
            print("win", t_total)
        elif response == DRAW:
            t_total = opponent + DRAW_VALUE
            print("draw", t_total)
        else:
            t_total = opponent.lose_move() + LOSE_VALUE
            print("lose", t_total)

        total += t_total

    print("total", total)
