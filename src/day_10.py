"""
https://adventofcode.com/2022/day/10
"""
import re
from pathlib import Path

# X=1
#
# addx V takes two cycles to complete
# After two cycles, the X register is increased by the value V
#
# noop takes one cycle to complete. It has no other effect.


def x_calculator(command, X, duration):
    if re.findall("noop\n?", command):
        duration += 1
        yield X, duration
    elif match := re.findall("addx (.+)\n?", command):
        value = int(match[0])
        duration += 1
        yield X, duration
        duration += 1
        yield X + value, duration
    else:
        raise ValueError(f"Invalid command: {command}")


def is_lit(X: int, crt_location: int) -> bool:
    return X == crt_location or X == crt_location + 1 or X == crt_location - 1


def total_generator(file_path: Path):
    value_during = X = 1
    cycle_number = 0
    total = 0
    return_cycle = 20
    crt_position = 0
    with file_path.open() as file:
        for command in file:
            for X, cycle_number in x_calculator(command, X, cycle_number):
                if cycle_number == return_cycle:
                    total += value_during * cycle_number
                    return_cycle += 40

                print(("#" if is_lit(value_during, crt_position) else "."), end="")
                value_during = X

                if crt_position == 39:
                    crt_position = 0
                    print()
                else:
                    crt_position += 1
    return total


if __name__ == "__main__":
    file_path = Path(__file__).parents[1].joinpath("inputs").joinpath("day10_input.txt")
    total = total_generator(file_path)
