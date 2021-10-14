from src.lv2.words_order import words_order


def test_words_order():
    results_exp = 'bag, hello, without, world'
    result = words_order('without, hello, bag, world')

    assert (result == results_exp) is True
