import unittest
from mbleven import compare

class TestFastComp(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(compare('abc', 'abc'), 0)

    def test_insert(self):
        self.assertEqual(compare('abc', 'xabc'), 1)
        self.assertEqual(compare('abc', 'axbc'), 1)
        self.assertEqual(compare('abc', 'abxc'), 1)
        self.assertEqual(compare('abc', 'abcx'), 1)
        self.assertEqual(compare('abc', 'xxabc'), 2)
        self.assertEqual(compare('abc', 'axxbc'), 2)
        self.assertEqual(compare('abc', 'abxxc'), 2)
        self.assertEqual(compare('abc', 'abcxx'), 2)
        self.assertEqual(compare('abc', 'xabcx'), 2)

    def test_replace(self):
        self.assertEqual(compare('abc', 'xbc'), 1)
        self.assertEqual(compare('abc', 'axc'), 1)
        self.assertEqual(compare('abc', 'abx'), 1)
        self.assertEqual(compare('abc', 'xxc'), 2)
        self.assertEqual(compare('abc', 'axx'), 2)
        self.assertEqual(compare('abc', 'xbx'), 2)

    def test_delete(self):
        self.assertEqual(compare('abc', 'ab'), 1)
        self.assertEqual(compare('abc', 'ac'), 1)
        self.assertEqual(compare('abc', 'bc'), 1)
        self.assertEqual(compare('a', 'abc'), 2)
        self.assertEqual(compare('b', 'abc'), 2)
        self.assertEqual(compare('c', 'abc'), 2)

    def test_insert_delete(self):
        self.assertEqual(compare('abcde', 'eabcd'), 2)
        self.assertEqual(compare('abcde', 'acdeb'), 2)
        self.assertEqual(compare('abcde', 'abdec'), 2)
        self.assertEqual(compare('ababa', 'babab'), 2)

    def test_transpose(self):
        self.assertEqual(compare('abc', 'bac', True), 1)
        self.assertEqual(compare('abc', 'acb', True), 1)
        self.assertEqual(compare('abc', 'cba', True), 2)
        self.assertEqual(compare('abc', 'ba', True), 2)
        self.assertEqual(compare('abc', 'ca', True), 2)

    def test_emptystr(self):
        self.assertEqual(compare('', ''), 0)
        self.assertEqual(compare('', 'a'), 1)
        self.assertEqual(compare('', 'ab'), 2)
        self.assertEqual(compare('', 'abc'), -1)
        self.assertEqual(compare('abc', ''), -1)

    def test_beyond(self):
        self.assertEqual(compare('abc', 'def'), -1)

if __name__ == '__main__':
    unittest.main()
