"""subTest 機能を確認するテスト."""

import unittest

import basic


class TestMyClass(unittest.TestCase):

    def test_add(self):
        params = (
            ('name1', 0, 0, 0),
            ('name2', 1, 2, 3),
            ('name3', -1, -2, -3),
        )
        for name, a, b, expected in params:
            with self.subTest(name, a=a, b=b, expected=expected):
                my_class = basic.MyClass(a)
                answer = my_class.add(b)
                self.assertEqual(expected, answer)


if __name__ == '__main__':
    unittest.main()
