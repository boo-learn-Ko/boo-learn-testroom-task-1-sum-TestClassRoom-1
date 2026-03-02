import pytest
from solution import add


def test_basic_sum():
    """Проверка сложения положительных чисел"""
    assert add(2, 2) == 4


def test_negative_numbers():
    """Проверка работы с отрицательными числами"""
    assert add(-1, 1) == 0
    assert add(-5, -5) == -10


def test_zero():
    """Проверка сложения с нулем"""
    assert add(0, 10) == 10


@pytest.mark.parametrize("a, b, expected", [
    (10, 20, 30),
    (0.1, 0.2, 0.3),
    (100, 200, 300),
])
def test_multiple_values(a, b, expected):
    """Массовая проверка разных входных данных"""
    assert add(a, b) == pytest.approx(expected)
