import unittest
import perm_lex

# Starter test cases - write more!


class TestAssign1(unittest.TestCase):

    def test_perm_gen_lex(self):
        self.assertEqual(perm_lex.perm_gen_lex('ab'), ['ab', 'ba'])

    def test_perm_gen_lex_01(self):
        self.assertEqual(perm_lex.perm_gen_lex('abc'), ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])

    def test_perm_gen_lex_02(self):
        self.assertEqual(perm_lex.perm_gen_lex(''), [])

    def test_perm_gen_lex_03(self):
        self.assertEqual(perm_lex.perm_gen_lex('a'), ['a'])


if __name__ == "__main__":
    unittest.main()
