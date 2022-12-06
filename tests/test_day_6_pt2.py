# pylint: skip-file
import pytest

from src.day_6 import find_start_of_packet

MARKER_SIZE = 14


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
        ("nppdvjthqldpwncqszvftbrmjlhg", 23),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26),
    ],
)
def test_find_unique_4_example(test_input, expected):
    assert find_start_of_packet(test_input, MARKER_SIZE) == expected


@pytest.fixture
def real_test_input(inputs_dir):
    return inputs_dir.joinpath("day6_input.txt").read_text()


def test_find_unique_4(real_test_input):
    result = find_start_of_packet(real_test_input, MARKER_SIZE)
    print(result)
    assert result == 3380
