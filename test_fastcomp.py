import unittest
from fastcomp import compare

class TestFastComp(unittest.TestCase):
    def test_all(self):
        self.assertEqual(compare("abc", "abc"), 0)
        self.assertEqual(compare("abc", "abcd"), 1)
        self.assertEqual(compare("abc", "abd"), 1)
        self.assertEqual(compare("abc", "bc"), 1)
        self.assertEqual(compare("abcde", "acdfe"), 2)
        self.assertEqual(compare("acdfe", "abcde"), 2)
        self.assertEqual(compare("abc", "bcd"), 2)
        self.assertEqual(compare("bcd", "abc"), 2)
        self.assertEqual(compare("abc", "ade"), 2)
        self.assertEqual(compare("abc", "eabf"), 2)
        self.assertEqual(compare("abc", "ebfc"), 2)
        self.assertEqual(compare("abc", "a"), 2)
        self.assertEqual(compare("c", "abc"), 2)
        self.assertEqual(compare("abcde", "bcdgf"), -1)
        self.assertEqual(compare("abc", "efg"), -1)
        self.assertEqual(compare("abc", ""), -1)
        self.assertEqual(compare("", "abc"), -1)
        self.assertEqual(compare("", "ab"), 2)
        self.assertEqual(compare("", "a"), 1)
        self.assertEqual(compare("", ""), 0)

if __name__ == "__main__":
    unittest.main()
