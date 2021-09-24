import pytest
from src.lv1.double_the_item import double


def test_double():
    results = [
        {1: 1, 2: 4},
        {1: 1, 2: 4, 3: 9, 4: 16},
    ]

    for result in results:
        assert (double(len(result)) == result) is True
