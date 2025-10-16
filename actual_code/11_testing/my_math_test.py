from my_math import add, MathFunctions
import pytest

def test_adding_two_positive_numbers():
    # Arrange - Given
    num1 = 2
    num2 = 3
    expected = 5
    # Act  - When
    result = add(num1, num2)
    # Assert  - Then
    assert result == expected

def test_adding_two_negative_numbers():
    assert -4 == add(-1, -3)

@pytest.mark.parametrize(
    "expected, a, b",
    [
        (3, 1, 2),
        (-10, 20, -30),
        (0.1, 0.05, 0.05),
        (1_000_000, 999_990, 10),
        (1, 1,0),
        (0, 0,0),
        (1, 0, 1),
        (2, 1, 1)
    ]
)
def test_adding_pairs_correctly(expected, a, b):
    assert expected == add(a, b)

def test_adding_two_strings_raises_error():
    with pytest.raises(ValueError):
        add("hello", "world")

@pytest.mark.parametrize("a, b", [
    ([], ()),
    (True, False),
    (set(), dict())
])
def test_adding_invalid_types_raises_error(a, b):
    with pytest.raises(ValueError):
        add(a, b)

def test_math_functions_add_works():
    calc = MathFunctions(1,2)
    assert calc.add() == 3

















