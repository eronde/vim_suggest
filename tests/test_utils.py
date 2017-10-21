from py_word_suggest.utils import *
import pytest
def test_is_empty():
    """utils, is_empty: Check if an object is empty or contains spaces
    :returns: TODO
    """
    assert is_empty('') == True 
    assert is_empty('test') == False 
