from src.lv1.number_tuple_sequencie import sequenci


def test_sequenci():
    result = (
      [34, 67, 55, 33, 12, 98],
      (34, 67, 55, 33, 12, 98)
    )

    assert (sequenci((34, 67, 55, 33, 12, 98)) == result) is True
