"""mock.patch の動作を確認するテスト(実装)."""


class MyClass:

    def __init__(self, value: int) -> None:
        self._value = value

    def outer(self) -> int:
        return 1 + self._inner(2)

    def _inner(self, val: int) -> int:
        return val + 3
