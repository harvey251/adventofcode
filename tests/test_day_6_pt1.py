# pylint: skip-file
import pytest

from src.day_6 import find_start_of_packet


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
        ("nppdvjthqldpwncqszvftbrmjlhg", 6),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
    ],
)
def test_find_unique_4_example(test_input, expected):
    assert find_start_of_packet(test_input) == expected


@pytest.fixture
def real_test_input(inputs_dir):
    return inputs_dir.joinpath("day6_input.txt").read_text()


def test_find_unique_4(real_test_input):
    result = find_start_of_packet(real_test_input)
    print(result)
    assert result != 7
    assert result == 1909
