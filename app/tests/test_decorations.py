import unittest
import re
from app.util.decorators import empty_arguments

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

    def test_is_empty(self):
        """decorations:
        :returns: TODO
        """
        # True
        self.assertTrue(_function_with_arg('bla', "bla"))
        # Raiss error on empty argument
        with self.assertRaises(Exception) as e:
            _function_with_arg('bla', '')
        error = str(e.exception)
        print(error)
        regex = re.search("^Error in '_function_with_arg': One of the given arguments .*\'bla', ''\)' are empty\.$", error)
        assert regex is not None
if __name__ == '__main__':
    unittest.main()
