import pytest
from exceptions import get_int, RangeError

class TestGetInput:
    def test_valid_input(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: 5)
        assert get_int() == 5
    def test_above_range(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: 20)
        with pytest.raises(RangeError):
            get_int()
