import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.parametrize("input_text, expected_output", [
    (" кот", "кот"),
    ("   кот", "кот"),
    ("кот ", "кот "),
    ])
def test_trim_positive(input_text, expected_output):
    assert string_utils.trim(input_text) == expected_output


@pytest.mark.parametrize("input_text, expected_output",
    [
        ("кот", "кот"),
    ])
def test_trim_negative(input_text, expected_output):
    assert string_utils.trim(input_text) == expected_output


