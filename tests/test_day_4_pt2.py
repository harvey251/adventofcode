# pylint: skip-file
from pathlib import Path

import pytest

from src.day4_pt2 import main, overlap
from tests.conftest import inputs_dir


@pytest.mark.parametrize(
    "elf_1_start, elf_1_end, elf_2_start, elf_2_end, expected",
    [
        ("2", "4", "6", "8", False),
        ("6", "8", "2", "4", False),
        ("2", "3", "4", "5", False),
        ("5", "8", "7", "9", True),
        ("2", "8", "3", "7", True),
        ("2", "8", "2", "8", True),
        ("6", "6", "4", "6", True),
        ("6", "6", "6", "6", True),
        ("2", "6", "4", "8", True),
        ("4", "8", "2", "6", True),
    ],
)
def test_overlap(elf_1_start, elf_1_end, elf_2_start, elf_2_end, expected):
    assert overlap(elf_1_start, elf_1_end, elf_2_start, elf_2_end) is expected


def test_main(inputs_dir):
    overlaps = main(inputs_dir.joinpath("day4_input_example.txt"))
    assert overlaps == 4
