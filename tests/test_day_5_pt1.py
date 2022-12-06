# pylint: skip-file

from queue import LifoQueue

from src.day5_pt1 import (
    convert_instruction_str_to_int,
    convert_table_to_array,
    convert_to_table_and_instructions,
    main,
    make_move,
)


def test_convert_to_table_and_instructions(inputs_dir):
    file_path = inputs_dir.joinpath("day5_input_example.txt")
    table, instructions = convert_to_table_and_instructions(file_path)
    assert table == ["    [D]    ", "[N] [C]    ", "[Z] [M] [P]", " 1   2   3 "]
    assert instructions == [
        "move 1 from 2 to 1",
        "move 3 from 1 to 3",
        "move 2 from 2 to 1",
        "move 1 from 1 to 2",
    ]


def test_convert_table_to_array():
    table_input = ("    [D]    ", "[N] [C]    ", "[Z] [M] [P]", " 1   2   3 ")
    table = convert_table_to_array(table_input)

    assert [list(r.queue) for r in table] == (("Z", "N"), ("M", "C", "D"), ("P",))


def test_convert_instruction_str_to_int():
    instruction_strs = (
        "move 1 from 2 to 1",
        "move 3 from 1 to 3",
        "move 2 from 2 to 1",
        "move 1 from 1 to 2",
        "move 13 from 7 to 8",
    )
    instructions = convert_instruction_str_to_int(instruction_strs)

    assert [list(i) for i in instructions] == [
        [1, 2, 1],
        [3, 1, 3],
        [2, 2, 1],
        [1, 1, 2],
        [13, 7, 8],
    ]


def test_make_move_example_1():
    instruction = (1, 2, 1)
    table = []
    for idx, row in enumerate((["Z", "N"], ["M", "C", "D"], ["P"]), 0):
        table.append(LifoQueue())
        for item in row:
            table[idx].put(item)

    new_table = make_move(instruction, table)

    assert [list(r.queue) for r in new_table] == [["Z", "N", "D"], ["M", "C"], ["P"]]


def test_make_move_example_2():
    instruction = (2, 2, 1)
    table = []
    for idx, row in enumerate(
        [
            [],
            ["M", "C"],
            [
                "P",
                "D",
                "N",
                "Z",
            ],
        ],
        0,
    ):
        table.append(LifoQueue())
        for item in row:
            table[idx].put(item)

    new_table = make_move(instruction, table)

    assert [list(r.queue) for r in new_table] == [
        [
            "C",
            "M",
        ],
        [],
        [
            "P",
            "D",
            "N",
            "Z",
        ],
    ]


def test_make_move_example_3():
    instruction = (1, 1, 2)
    table = []
    for idx, row in enumerate(
        [
            [
                "C",
                "M",
            ],
            [],
            [
                "P",
                "D",
                "N",
                "Z",
            ],
        ],
        0,
    ):
        table.append(LifoQueue())
        for item in row:
            table[idx].put(item)

    new_table = make_move(instruction, table)

    assert [list(r.queue) for r in new_table] == [
        [
            "C",
        ],
        [
            "M",
        ],
        [
            "P",
            "D",
            "N",
            "Z",
        ],
    ]


def test_main(inputs_dir):
    file_path = inputs_dir.joinpath("day5_input_example.txt")
    result = main(file_path)
    assert result == "CMZ"
