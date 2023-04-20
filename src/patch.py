"""mock.patch の動作を確認するテスト(実装)."""


class MyClass:

    def __init__(self, value: int) -> None:
        self._value = value

    def outer1(self) -> int:
        return 1 + self._inner1(2)

    def _inner1(self, val: int) -> int:
        return val + 3

    def outer2(self) -> None:
        self._inner2(1, 2, 3)

    def _inner2(self, a: int, b: int, c: int) -> None:
        pass

    @property
    def value(self) -> int:
        return self._value
