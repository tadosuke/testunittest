"""parameterized を使用したテスト.

このモジュールを使うには、PyPI から parameterized パッケージをインストールする必要があります。
"""

import unittest

from parameterized import parameterized

import basic


class MyTestCase(unittest.TestCase):

    @parameterized.expand([
        ('test_a', 1, 2, 3),
        ('test_b', 2, 3, 5),
        ('test_c', 3, 4, 7),
    ])
    def test_add(self, name, a, b, c):
        self.assertEqual(c, basic.add(a, b))


if __name__ == '__main__':
    unittest.main()
