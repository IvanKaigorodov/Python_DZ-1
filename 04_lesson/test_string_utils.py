import pytest
from string_utils import StringUtils
utils = StringUtils()


# 1.1 capitalize Негативный сценарий
@pytest.mark.parametrize("input_text, expected_output", [
    ("1негатив", "1негатив"),
    (".негатив", ".негатив"),
    ("234", "234"),
  ])
def test_capitiaize_negative(input_text, expected_output):
    assert utils.capitalize(input_text) == expected_output


# 1.2 capitalize Позитивный сценарий
@pytest.mark.parametrize("input_text, expected_output", [
    ("первый", "Первый"),
    ("second", "Second"),
    ("ТРЕТИЙ", "Третий"),
  ])
def test_capitalize_positive(input_text, expected_output):
    assert utils.capitalize(input_text) == expected_output


# 2.1 trim Негативный сценарий
@pytest.mark.parametrize("input_text, expected_output", [
    ("без пробела", "без пробела"),
    ("пробел в конце ", "пробел в конце "),
])
def test_trim_negative(input_text, expected_output):
    assert utils.trim(input_text) == expected_output


# 2.2 trim Позитивный сценарий
@pytest.mark.parametrize("input_text, expected_output", [
    (" пробел удален", "пробел удален"),
    ("   3 пробела удалены", "3 пробела удалены"),
    (" space removed", "space removed"),
])
def test_trim_positive(input_text, expected_output):
    assert utils.trim(input_text) == expected_output


# 3 to_list
@pytest.mark.parametrize("string, delimeter, output", [
    # 3.1 Негативный сценарий
    ("", "100", []),
    # 3.2 Позитивный сценарий
    ("раз,два,три", ",", ["раз", "два", "три"]),
    ("1*2*3*восемь", "*", ["1", "2", "3", "восемь"]),
])
def test_to_list(string, delimeter, output):
    result = utils.to_list(string, delimeter)
    assert result == output


# 4 contains
@pytest.mark.parametrize('string, symbol, output', [
    ("Кабинет", "б", True),
    ("рУЧКА", "Ч", True),
    ("Окно", "о", True),
    ("555", "п", False),
    ("QWER", "T", False),
    ("один", "1", False),
])
def test_contains(string, symbol, output):
    result = utils.contains(string, symbol)
    assert result == output


# 5 delete_symbol
@pytest.mark.parametrize('string, symbol, output', [
    # 5.1 Позитивный сценарий
    ("Кабинет", "нет", "Каби"),
    ("рУЧКА", "Ч", "рУКА"),
    ("Окно", "н", "Око"),
    ("6987", "98", "67"),
    # 5.2 Негативный сценарий
    ("555", "п", "555"),
    ("QWER", "", "QWER"),
    ("один", "1", "один"),
])
def test_delete_symbol(string, symbol, output):
    result = utils.delete_symbol(string, symbol)
    assert result == output


# 6 starts_with
@pytest.mark.parametrize('string, symbol, output', [
    # 6.1 Позитивный сценарий
    ("Кабинет", "К", True),
    ("рУЧКА", "р", True),
    ("Окно", "О", True),
    ("467", "4", True),
    # 6.2 Негативный сценарий
    ("555", "п", False),
    ("QWER", "Й", False),
    ("один", "1", False),
    # ("Без символа", "", False), # принимает True
])
def test_starts_with(string, symbol, output):
    result = utils.starts_with(string, symbol)
    assert result == output


# 7 end_with
@pytest.mark.parametrize('string, symbol, output', [
    # 7.1 Позитивный сценарий
    ("Кабинет", "т", True),
    ("рУЧКА", "А", True),
    ("Окно", "о", True),
    ("467", "7", True),
    # 7.2 Негативный сценарий
    ("555", "п", False),
    ("QWER", "К", False),
    ("один", "1", False),
    # ("Без символа", "", False), # принимает True
])
def test_end_with(string, symbol, output):
    result = utils.end_with(string, symbol)
    assert result == output


# 8 is_empty
@pytest.mark.parametrize('string, output', [
    # 8.1 Позитивный сценарий
    ("", True),
    (" ", True),
    ("  ", True),
    # 8.2 Негативный сценарий
    ("5 5 5", False),
    ("QWER ", False),
    (" один", False),
    ("Без символа", False),
])
def test_is_empty(string, output):
    result = utils.is_empty(string)
    assert result == output


# 9 list_to_string
@pytest.mark.parametrize('lst, joiner, output', [
    # 9.1 Позитивный сценарий
    ([1, 2, 3, 4], ", ", "1, 2, 3, 4"),
    (["Добрый", "вечер"], "-", "Добрый-вечер"),
    (["С", "О", "Н"], "", "СОН"),
    # 9.2 Негативный сценарий
    ([], "!", ""),
    ([], "слово", ""),
])
def test_list_to_string(lst, joiner, output):
    result = utils.list_to_string(lst, joiner)
    assert result == output
