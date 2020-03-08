# Testy dla programu rycerze.py

import rycerze
import pytest

def test_get_input():
# Correct input test
    rycerze.get_input('24')

# Invalid input test
    with pytest.raises(SystemExit) as error:
        rycerze.get_input('asffsa')
    assert error.type == SystemExit
    assert error.value.code == 2

    with pytest.raises(SystemExit) as error:
        rycerze.get_input('2dwa')
    assert error.type == SystemExit
    assert error.value.code == 2

    with pytest.raises(SystemExit) as error:
        rycerze.get_input('-231')
    assert error.type == SystemExit
    assert error.value.code == 2

    with pytest.raises(SystemExit) as error:
        rycerze.get_input('5.63')
    assert error.type == SystemExit
    assert error.value.code == 2

# No input test
    with pytest.raises(SystemExit) as error:
        rycerze.get_input(None)
    assert error.type == SystemExit
    assert error.value.code == 1

def test_generate_knights():
    assert rycerze.generate_knights(10) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert rycerze.generate_knights(0) == []

    with pytest.raises(SystemExit) as error:
        rycerze.generate_knights(None) == []
    assert error.type == SystemExit
    assert error.value.code == 3


def test_simulate_problem():
    test_array = rycerze.generate_knights(42)
    assert rycerze.simulate_problem(test_array) == [21]

    test_array = rycerze.generate_knights(10)
    assert rycerze.simulate_problem(test_array) == [5]

    with pytest.raises(SystemExit) as error:
        rycerze.simulate_problem(None) == []
    assert error.type == SystemExit
    assert error.value.code == 3