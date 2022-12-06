# pylint: skip-file

from pathlib import Path


def overlap(elf_1_start: int, elf_1_end: int, elf_2_start: int, elf_2_end: int):
    if elf_1_start <= elf_2_start <= elf_1_end:
        return True
    if elf_2_start <= elf_1_start <= elf_2_end:
        return True
    return False


def main(file_path: Path):
    pairs_assigned = 0
    for line in read_lines(file_path):
        elf_1_string, elf_2_string = line.strip().split(",")
        elf_1_start, _, elf_1_end = elf_1_string.partition("-")
        elf_2_start, _, elf_2_end = elf_2_string.partition("-")

        pairs_assigned += overlap(
            int(elf_1_start), int(elf_1_end), int(elf_2_start), int(elf_2_end)
        )

    return pairs_assigned


def read_lines(file_path: Path):
    with file_path.open("r") as f:
        for line in f.readlines():
            yield line.strip()


if __name__ == "__main__":
    answer = main(Path(__file__).parent.joinpath("day4_input.txt"))
    print(answer)
