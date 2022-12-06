import string
from pathlib import Path

elf = 1
elf_total = 0
t_elf = 1
t_total = 0

elves = []

d = set()
d.intersection()


class StringSet(str):
    def intersection(self, other):
        return set(self).intersection(set(other))


with Path(__file__).parent.joinpath("day3_input.txt").open("r") as f:
    priority_total = 0
    for line in f.readlines():
        total = line.strip()

        half = len(total) // 2
        first, second = StringSet(total[:half]), StringSet(total[half:])
        unique = first.intersection(second).pop()
        priority = string.ascii_letters.index(unique) + 1
        priority_total += priority
        print(first, second, unique, priority)
    print(priority_total)
