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

    def setUp(self):
        self.my_class = patch.MyClass(1)

    def test_outer_local(self):
        # mock で my_class オブジェクトの _inner メソッドを乗っ取る(ローカル変数)
        print(f'{self.id()}')

        mp_inner = MagicMock()
        self.my_class._inner = mp_inner
        self.my_class.outer()
        mp_inner.assert_called()  # mp_inner が呼ばれたか

    def test_outer_with(self):
        # mock で my_class オブジェクトの _inner メソッドを乗っ取る(with 句)
        print(f'{self.id()}')

        with mock.patch.object(self.my_class, '_inner') as mp_inner:
            self.my_class.outer()
            mp_inner.assert_called()  # mp_inner が呼ばれたか

    @mock.patch('patch.MyClass._inner')
    def test_outer_decorator(self, mp_inner):
        # mock で my_class オブジェクトの _inner メソッドを乗っ取る(デコレータ)
        print(f'{self.id()}')

        self.my_class.outer()
        mp_inner.assert_called()  # mp_inner が呼ばれたか

    def test_outer_return_value(self):
        # 内部関数の戻り値を書き換える
        print(f'{self.id()}')

        # _inner 関数の戻り値を強制的に 3 にする
        with mock.patch.object(self.my_class, '_inner', return_value=3):
            ret = self.my_class.outer()
            self.assertEqual(4, ret)

    def test_outer_side_effect(self):
        # 内部関数が呼ばれた時に別の関数を呼ぶ
        print(f'{self.id()}')

        def my_side_effect(val: int):  # 元の引数も受け取れる
            return val + 2

        # _inner が呼ばれるタイミングで my_side_effect が呼ばれる。モックオブジェクトが作成される
        with mock.patch.object(self.my_class, '_inner', side_effect=my_side_effect) as mp_inner:
            ret = self.my_class.outer()
            self.assertEqual(5, ret)
            mp_inner.assert_called()

    def test_outer_new(self):
        # 内部関数を別関数に置き換える
        print(f'{self.id()}')

        def my_new(val: int):  # 元の引数も受け取れる
            return val + 2

        # _inner の代わりに my_new が呼ばれる。モックオブジェクトは作成されない
        with mock.patch.object(self.my_class, '_inner', new=my_new) as mp_inner:
            ret = self.my_class.outer()
            self.assertEqual(5, ret)
            # mp_inner.assert_called()  # モックオブジェクトが作られないので、assert_called などは使えない

    def test_outer_spec(self):
        # spec に渡したオブジェクトに存在しないメソッドを呼ぼうとするとエラーになるようにする

        # spec を使わない場合
        mock_myclass = MagicMock()
        mock_myclass.outer()
        mock_myclass.ouner()  # 存在しないメソッドを呼んでもエラーにならない(Mock 内で勝手に作ってしまうため)

        # spec を使う場合
        mock_myclass = MagicMock(spec=patch.MyClass)
        mock_myclass.outer()
        # mock_myclass.ouner()  # MyClass に存在しないメソッドを呼ぶとエラーになる

        # create_autospec() でも同じ効果が得られる
        mock_myclass = mock.create_autospec(patch.MyClass)
        mock_myclass.outer()
        # mock_myclass.outer()


if __name__ == '__main__':
    unittest.main()
