from sar_handler import first_func


def test_first_func():
    assert first_func._sum(10, 12) == (10 + 12)
