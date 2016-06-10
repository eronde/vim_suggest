import unittest
import re
from app.util.utils import *


class utilsTest(unittest.TestCase):
    """Docstring for decorationsTest. """

    def setUp(self):
        """ decorators: setup
        """
        pass

    def tearDown(self):
        pass

    def test_is_empty(self):
        """utils, is_empty: Check if an object is empty or contains spaces
        :returns: TODO
        """
        self.assertTrue(is_empty(''))


if __name__ == '__main__':
    unittest.main()
