"""実装."""


def add(a: int, b: int) -> int:
    return a+b


def sub(a: int, b: int) -> int:
    return a-b


class MyClass:

    def __init__(self, value: int) -> None:
        self._value = value

    def add(self, val: int) -> int:
        return self._value + val

    def sub(self, val: int) -> int:
        return self._value - val
