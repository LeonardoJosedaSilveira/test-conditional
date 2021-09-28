from src.lv1.fatorial import fatorial


def test_fatorial():
    value = fatorial(8)
    assert (40320 == value) is True
