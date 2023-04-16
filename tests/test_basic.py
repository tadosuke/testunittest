"""基本的な呼び出しを確認するテスト."""

import unittest

import basic


# モジュール変数
module_value = 0


def setUpModule():
    """モジュールのテスト開始時に一度だけ呼ばれる."""
    print('\n*** setUpModule(basic)')

    global module_value
    module_value = 5


def tearDownModule():
    """モジュールのテスト終了時に一度だけ呼ばれる."""
    print('*** tearDownModule(basic)')


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
        self.assertEqual(3, basic.add(1, 2))
        # self.assertEqual(4, basic.add(1, 2))  失敗するテスト
        self.assertNotEqual(2, basic.add(1, 2))

        # setUpModule で設定した値が有効
        self.assertEqual(5, module_value)

    def test_sub(self):
        print(f'{self.id()}')
        self.assertEqual(2, basic.sub(3, 1))
        self.assertNotEqual(1, basic.sub(3, 1))


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
        self.my_class = basic.MyClass(3)

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
