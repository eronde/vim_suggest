from py_word_suggest.utils import *
import pytest 
@pytest.mark.parametrize("testInput,expected_output",
        [
            ('', True),
            (None, True),
            ('NonWwhiteSpaces', False),
            ('String with white-space', True),
            (10, False)
       ]
        )
def test_is_empty(testInput,expected_output):
    """utils, is_empty: Check if an object is empty or contains spaces
    :returns: TODO
    """
    assert is_empty(testInput) == expected_output
