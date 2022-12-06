# pylint: skip-file
import re
from pathlib import Path
from queue import LifoQueue


def main(file_path: Path):
    table_rows, instruction_strs = convert_to_table_and_instructions(file_path)

    table = convert_table_to_array(table_rows)
    instructions = convert_instruction_str_to_int(instruction_strs)

    for instruction in instructions:
        table = make_move(instruction, table)

    results = ""
    for row in table:
        results += row.get()

    return results


def make_move(instruction, table: list[LifoQueue]):
    number_of_crates, row, new_row = instruction
    for _ in range(number_of_crates):
        table[new_row - 1].put(table[row - 1].get())
    return table


def convert_instruction_str_to_int(instruction_strs):
    instruction_tuple = []
    for instruction in instruction_strs:
        instruction_tuple.append(
            int(i)
            for i in re.findall(r"^move (\d+) from (\d+) to (\d+)$", instruction)[0]
        )
    return instruction_tuple


def convert_to_table_and_instructions(file_path):
    table_rows = []
    table_complete = False
    instructions = []
    for line in read_lines(file_path):
        if line and table_complete is False:
            table_rows.append(line)
        elif line and table_complete is True:
            instructions.append(line)
        else:
            table_complete = True
    return table_rows, instructions


def convert_table_to_array(table: list) -> list[LifoQueue]:
    index_row = table[-1]
    number_of_rows = int(re.findall(r"(\d+)\s?$", index_row)[-1])
    array: list[LifoQueue] = [LifoQueue() for _ in range(number_of_rows)]

    for row in reversed(table[:-1]):
        row_elements = re.findall(r"(?:\s{3}|\[(\w)\])\s?", row)
        for idx, element in enumerate(row_elements, 0):
            if element:
                array[idx].put(element)
    return array


def read_lines(file_path: Path):
    with file_path.open("r") as f:
        for line in f.readlines():
            yield line.strip("\n")


if __name__ == "__main__":
    answer = main(Path(__file__).parent.joinpath("day5_input.txt"))
    print(answer)
