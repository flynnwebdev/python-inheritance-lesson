from calculator import square

class TestSquare:
    def test_positive(self):
        assert square(2) == 4
        assert square(3) == 9

    def test_negative(self):
        assert square(-2) == 4
        assert square(-3) == 9

    def test_zero(self):
        assert square(0) == 0


class TestCube:
    pass
