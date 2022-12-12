import pytest

from src.day_10 import is_lit, total_generator, x_calculator


def test_noop():
    X_in = Y = 1
    duration_in = 0
    for (
        X_out,
        duration,
    ) in x_calculator("noop", Y, duration_in):
        assert X_out == X_in
        assert duration == duration_in + 1


def test_addx():
    X_in = 1
    duration_in = 1
    iter_magic = iter(x_calculator("addx 3", X_in, duration_in))

    X_out_1, duration_1 = next(iter_magic)
    assert X_out_1 == X_in
    assert duration_1 == duration_in + 1

    X_out_2, duration_2 = next(iter_magic)
    assert X_out_2 == 4
    assert duration_2 == duration_in + 2


def test_addx_negative():
    X_in = 4
    duration_in = 1
    iter_magic = iter(x_calculator("addx -5", X_in, duration_in))

    X_out_1, duration_1 = next(iter_magic)
    assert X_out_1 == X_in
    assert duration_1 == duration_in + 1

    X_out_2, duration_2 = next(iter_magic)
    assert X_out_2 == -1
    assert duration_2 == duration_in + 2


@pytest.fixture
def input_real(inputs_dir):
    with inputs_dir.joinpath("day10_input.txt").open() as file:
        yield file.readlines()


@pytest.fixture
def input_example(inputs_dir):
    with inputs_dir.joinpath("day10_input_example.txt").open() as file:
        yield file.readlines()


def test_result_example_1(input_example, check):
    X = 1
    cycle_number = 1
    total = 0
    for command in input_example:
        for X, cycle_number in x_calculator(command, X, cycle_number):
            if cycle_number == 20:
                check.equal(X, 21)
                check.equal(X * cycle_number, 420)
            elif cycle_number == 60:
                check.equal(X, 19)
                check.equal(X * cycle_number, 1140)
            elif cycle_number == 100:
                check.equal(X, 18)
                check.equal(X * cycle_number, 1800)
            elif cycle_number == 140:
                check.equal(X, 21)
                check.equal(X * cycle_number, 2940)
            elif cycle_number == 180:
                check.equal(X, 16)
                check.equal(X * cycle_number, 2880)
            elif cycle_number == 220:
                check.equal(X, 18)
                check.equal(X * cycle_number, 3960)

            if (cycle_number + 20) % 40 == 0:
                total += X * cycle_number

    assert total == 13140


def test_result_real_1(input_real, check):
    value_during = new_value = 1
    cycle_number = 0
    total = 0
    return_cycle = 20
    for command in input_real:
        for new_value, cycle_number in x_calculator(command, new_value, cycle_number):
            if cycle_number == return_cycle:
                total += value_during * cycle_number
                return_cycle += 40
            value_during = new_value
    assert total < 14000
    assert total == 12880


def test_total_generator_example(inputs_dir):
    assert total_generator(inputs_dir.joinpath("day10_input_example.txt")) == 13140


def test_total_generator_real(inputs_dir):
    assert total_generator(inputs_dir.joinpath("day10_input.txt")) == 12880


def test_crt_position_example_1(check):
    """
    Sprite position: ###.....................................

    Start cycle   1: begin executing addx 15
    During cycle  1: CRT draws pixel in position 0
    Current CRT row: #
    Sprite position: ###.....................................
    """
    lit = is_lit(X=1, crt_location=0)
    check.is_true(lit)


def test_crt_position_example_3(check):
    """
    Sprite position (16): ...............###......................

    Start cycle   3: begin executing addx -11
    During cycle  3: CRT draws pixel in position 2
    Current CRT row: ##.
    """
    lit = is_lit(X=16, crt_location=2)
    check.is_false(lit)
