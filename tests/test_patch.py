"""mock.patch の動作を確認するテスト."""

import unittest
from unittest import mock
from unittest.mock import MagicMock

import patch


def setUpModule():
    """モジュールのテスト開始時に一度だけ呼ばれる."""
    print('\n*** setUpModule(patch)')


def tearDownModule():
    """モジュールのテスト終了時に一度だけ呼ばれる."""
    print('*** tearDownModule(patch)')


class TestMyClass(unittest.TestCase):

    def test_outer_with(self):
        # mock で my_class オブジェクトの _inner メソッドを乗っ取る(with 句)
        print(f'{self.id()}')

        my_class = patch.MyClass(1)
        with mock.patch.object(my_class, '_inner') as mp_inner:
            my_class.outer()
            mp_inner.assert_called()  # mp_inner が呼ばれたか

    def test_outer_local(self):
        # mock で my_class オブジェクトの _inner メソッドを乗っ取る(ローカル変数)
        print(f'{self.id()}')

        my_class = patch.MyClass(1)
        mp_inner = MagicMock()
        my_class._inner = mp_inner
        my_class.outer()
        mp_inner.assert_called()  # mp_inner が呼ばれたか

    @mock.patch('patch.MyClass._inner')
    def test_outer_decorator(self, mp_inner):
        # mock で my_class オブジェクトの _inner メソッドを乗っ取る(デコレータ)
        print(f'{self.id()}')

        my_class = patch.MyClass(1)
        my_class.outer()
        mp_inner.assert_called()  # mp_inner が呼ばれたか


if __name__ == '__main__':
    unittest.main()
