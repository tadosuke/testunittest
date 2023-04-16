"""hoge のテスト."""

import unittest

import hoge


# モジュール変数
module_value = 0


def setUpModule():
    """モジュールのテスト開始時に一度だけ呼ばれる."""
    print('\n*** setUpModule')

    global module_value
    module_value = 5


def tearDownModule():
    """モジュールのテスト終了時に一度だけ呼ばれる."""
    print('*** tearDownModule')


class TestModuleFunc(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('** setUpClass(ModuleFunc)')

    @classmethod
    def tearDownClass(cls):
        print('** tearDownClass(ModuleFunc)')

    def setUp(self):
        print('\n* setUp(ModuleFunc)')

    def tearDown(self):
        print('* tearDown(ModuleFunc)')

    def test_add(self):
        print(f'{self.id()}')
        self.assertEqual(3, hoge.add(1, 2))
        # self.assertEqual(4, hoge.add(1, 2))  失敗するテスト
        self.assertNotEqual(2, hoge.add(1, 2))

        # setUpModule で設定した値が有効
        self.assertEqual(5, module_value)

    def test_sub(self):
        print(f'{self.id()}')
        self.assertEqual(2, hoge.sub(3, 1))
        self.assertNotEqual(1, hoge.sub(3, 1))


class TestMyClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('** setUpClass(MyClass)')
        cls.value = 10

    @classmethod
    def tearDownClass(cls):
        print('** tearDownClass(MyClass)')

    def setUp(self):
        print('\n* setUp(MyClass)')
        self.my_class = hoge.MyClass(3)

    def tearDown(self):
        print('* tearDown(MyClass)')

    def test_add(self):
        print(f'{self.id()}')
        # setUp で生成したオブジェクトを使える
        self.assertEqual(4, self.my_class.add(1))

    def test_sub(self):
        print(f'{self.id()}')
        self.assertEqual(2, self.my_class.sub(1))
        # setUpClass で入れたメンバーを使える
        self.assertEqual(10, self.value)


if __name__ == '__main__':
    unittest.main()
