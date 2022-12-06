# pylint: skip-file
import re
from pathlib import Path
from queue import LifoQueue


class CrateMover9000:
    """Can only move one bos at a time"""

    @staticmethod
    def make_move(instruction, table: list[LifoQueue]):
        number_of_crates, row, new_row = instruction
        for _ in range(number_of_crates):
            table[new_row - 1].put(table[row - 1].get())
        return table


class CrateMover9001:
    """Can move multiple at a time"""

    @staticmethod
    def make_move(instruction, table: list[LifoQueue]):
        number_of_crates, row, new_row = instruction
        items = []
        for _ in range(number_of_crates):
            items.append(table[row - 1].get())

        for item in reversed(items):
            table[new_row - 1].put(item)
        return table


def main(file_path: Path, crate_mover):
    table_rows, instruction_strs = convert_to_table_and_instructions(file_path)

    table = convert_table_to_array(table_rows)
    instructions = convert_instruction_str_to_int(instruction_strs)

    for instruction in instructions:
        table = crate_mover.make_move(instruction, table)

    results = ""
    for row in table:
        results += row.get()

    return results


def convert_instruction_str_to_int(instruction_strs):
    p = re.compile(r"^move (\d+) from (\d+) to (\d+)$")
    for instruction in instruction_strs:
        yield (int(i) for i in p.findall(instruction)[0])


def convert_to_table_and_instructions(file_path):
    table_rows = []
    instructions = read_lines(file_path)
    for line in instructions:
        if line != "\n":
            table_rows.append(line)
        else:
            break
    return table_rows, instructions


def convert_table_to_array(table: list) -> list[LifoQueue]:
    index_row = table[-1]
    number_of_rows = int(re.findall(r"(\d+)\s?$", index_row)[-1])
    array: list[LifoQueue] = [LifoQueue() for _ in range(number_of_rows)]
    p = re.compile(r"(?:\s{3}|\[(\w)\])\s?")
    for row in reversed(table[:-1]):
        row_elements = p.findall(row)
        for idx, element in enumerate(row_elements, 0):
            if element:
                array[idx].put(element)
    return array


def read_lines(file_path: Path):
    with file_path.open("r") as f:
        yield from f.readlines()


if __name__ == "__main__":
    answer = main(Path(__file__).parent.joinpath("day5_input.txt"), CrateMover9001)
    print(answer)
