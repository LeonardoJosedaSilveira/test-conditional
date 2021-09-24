from src.lv1.square_root import calc_extra_sqrt


def test_square():
    results_exp = [18, 22, 24]
    items = (100, 150, 180)

    assert (calc_extra_sqrt(items) == results_exp) is True
