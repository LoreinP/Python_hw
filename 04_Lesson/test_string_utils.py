import pytest
from string_utils import StringUtils


string_utils = StringUtils


@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])


def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected
def test_capitalize_negative(input_str, expected):
    # негатив
    assert string_utils.capitalize(" ") == " " # с пробелом
    assert string_utils.capitalize("") == "" # пустая строка

def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected
    # позитив
    assert string_utils.capitalize("кот") == "Кот"
    assert string_utils.capitalise("Кот") == "Кот"


def test_trim_positive():
    assert string_utils.trim("   кот") == ("кот")
    assert string_utils.trim("кот   ") == ("кот")

def test_trim_negative():
    assert string_utils.trim("") == ""
    assert string_utils.trim(" ") == " "












