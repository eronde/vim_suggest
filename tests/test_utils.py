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
    """utils, is_empty: Check if an object is empty or contains spaces"""
    assert is_empty(testInput) == expected_output

@pytest.mark.parametrize("testInput,expectedOutput",
            [
            ("String", True),
            (['lol,lol2'], True),
            (('lol','lol2'), True),
            ({'lol','lol2'}, True),
            (10, False),
            (None, False)
            ]
        )
def test_is_iterable(testInput,expectedOutput):
    """utils, is_iterable Check if an object is iterable"""
    assert is_iterable(testInput) == expectedOutput
