from src.lv2.matriz import calc_and_create_matriz


def test_calc_and_create_matriz():
    results_exp = [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
    result = calc_and_create_matriz(3, 5)

    assert result == results_exp is True
