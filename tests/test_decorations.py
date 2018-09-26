import unittest
import re
from py_word_suggest.decorators import empty_arguments

@empty_arguments(Exception)
def _function_with_arg(text, text2):
    return True


class decorationsTest(unittest.TestCase):
    """Docstring for decorationsTest. """
    def setUp(self):
        """ decorators: setup
        """
        pass

    def tearDown(self):
        pass

    def test_empty_arguments(self):
        """decorations: empty_arguments,  Check if args of functions are empty, not kwargs
        :returns: TODO
        """
        # True
        self.assertTrue(_function_with_arg('bla', "bla"))
        # Raiss error on empty argument
        with self.assertRaises(Exception) as e:
            _function_with_arg('bla', '')
        error = str(e.exception)
        pat =r"^Error in '_function_with_arg': One of the given arguments .*\'bla', ''\)' are empty\.$"
        regex = re.search(pat, error)
        assert regex is not None, r"'{e}' should be: ^Error in '_function_with_arg': One of the given arguments .*\'bla', ''\)' are empty\.$".format(e=pat)
if __name__ == '__main__':
    unittest.main()
