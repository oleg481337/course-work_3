from funktion import create_ex_class


def test_create_ex_class():
    """Тест функции get_json_to_list"""
    assert type(create_ex_class()) == list
    assert create_ex_class() is not None
