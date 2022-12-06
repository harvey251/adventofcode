from pathlib import Path

import pytest


@pytest.fixture
def inputs_dir():
    return Path(__file__).parents[1].joinpath( "inputs")