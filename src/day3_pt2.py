import string
from functools import reduce
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
    count = 0
    groups = []
    for line in f.readlines():
        group = StringSet(line.strip())
        groups.append(group)
        if len(groups) == 3:
            group_unique = (
                groups[0].intersection(groups[1]).intersection(groups[2]).pop()
            )
            priority = string.ascii_letters.index(group_unique) + 1
            priority_total += priority
            print(group_unique, priority)
            groups = []

    print(priority_total)
