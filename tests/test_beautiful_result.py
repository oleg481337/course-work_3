from funktion import beautiful_result
from main import operation


def test_beautiful_result():
    """Тест функции beautiful_result"""
    assert beautiful_result(operation) == True
