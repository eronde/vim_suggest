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

@pytest.mark.parametrize("testInput, collection, expectedOutput, errorState",
            [
            ('Love',['I', 'Love', 'python'], True, False),
            ('love',['I', 'Love', 'python'], False, False),
            ('',['I', 'Love', 'python'], False, False),
            (None,['I', 'Love', 'python'], False, False),
            (None,"String", "Error: collection is not iterable or is a string", True),
            ('Love',8, "Error: collection is not iterable or is a string", True),
            ('Love',None, "Error: collection is not iterable or is a string", True),
            ]
        )
def test_containing(testInput, collection,  expectedOutput, errorState):
    """utils: Check if collection contains an item"""
    if  errorState is False:
        assert containing(collection, testInput) == expectedOutput
    else:
        with pytest.raises(utilsError) as e:
            containing(collection, testInput)
            assert str(e.value) == expectedOutput
