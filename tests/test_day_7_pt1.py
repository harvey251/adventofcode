import pytest

from src.day_7 import TerminalParser


@pytest.mark.parametrize(
    "test_input,expected_mode",
    [
        ("$ cd /", "cd"),
        ("$ ls", "ls"),
    ],
)
def test_find_unique_4_example(test_input, expected_mode):
    parser = TerminalParser()
    parser.parse_line(test_input)
    assert parser.mode == expected_mode


@pytest.fixture
def input_real(inputs_dir):
    with inputs_dir.joinpath("day7_input.txt").open() as file:
        yield file.readlines()


@pytest.fixture
def input_example(inputs_dir):
    with inputs_dir.joinpath("day7_input_example.txt").open() as file:
        yield file.readlines()


@pytest.fixture
def loaded_parser_example(input_example):
    parser = TerminalParser()
    for line in input_example:
        parser.parse_line(line)
    return parser


@pytest.fixture
def loaded_parser_real(input_real):
    parser = TerminalParser()
    for line in input_real:
        parser.parse_line(line)
    return parser


def test_result_example_1(loaded_parser_example):
    assert loaded_parser_example.folders == {}


def test_result_real_1(loaded_parser_real):
    assert len(loaded_parser_real.folders) == 175
