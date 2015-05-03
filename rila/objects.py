class RilaObject(object):
    pass


class RilaNumber(RilaObject):
    def __init__(self, value):
        self.value = value

    def add(self, other):
        assert isinstance(other, RilaNumber)
        return RilaNumber(self.value + other.value)

    def sub(self, other):
        assert isinstance(other, RilaNumber)
        return RilaNumber(self.value - other.value)

    def mult(self, other):
        assert isinstance(other, RilaNumber)
        return RilaNumber(self.value * other.value)

    def div(self, other):
        assert isinstance(other, RilaNumber)
        return RilaNumber(self.value / other.value)

    def str(self):
        return str(self.value)


class RilaBoolean(RilaObject):
    def __init__(self, value):
        assert value in [True, False]
        self.value = value

    def str(self):
        return "True" if self.value else "False"
