import pytest
from exceptions import get_int, RangeError

inputs = iter([5, 10, 20, -5])

def fake_input(prompt):
    return next(inputs)

class TestGetInt:
    def test_valid(self, monkeypatch):
        monkeypatch.setattr('builtins.input', fake_input)
        assert get_int() == 5
        assert get_int() == 10

    def test_above_range(self, monkeypatch):
        monkeypatch.setattr('builtins.input', fake_input)
        with pytest.raises(RangeError):
            get_int()

    def test_below_range(self, monkeypatch):
        monkeypatch.setattr('builtins.input', fake_input)
        with pytest.raises(RangeError):
            get_int()
