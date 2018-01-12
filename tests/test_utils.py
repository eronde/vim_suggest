from py_word_suggest.utils import *
import pytest 

raw_json = """
{"lang:nl:0:ben":[["ik", 22.0], ["er", 8.0], ["een", 7.0], ["je", 5.0]],\n"lang:nl:0:Ik":[["heb", 66.0], ["ben", 52.0], ["denk", 15.0], ["wil", 13.0], ["acht", 1.0]],\n"lang:eng:0:I":[["am", 100], ["want", 246], ["love", 999]],\n"lang:eng:0:am":[["the",100], ["Alice", 50],["Bob", 45]]\n}\n
"""


@pytest.fixture(scope="session")
def raw_json_file(tmpdir_factory):
    f = tmpdir_factory.mktemp("data_tmp").join("test.json")

    f.write(raw_json)
    return f

@pytest.mark.parametrize("testInput, expectedOutput, state",
            [
                (b'{"lang:nl:0:Ik":[["heb", 66.0], ["ben", 52.0], ["denk", 15.0], ["wil", 13.0], ["acht", 1.0]]}', {'lang:nl:0:Ik':[['heb', 66.0], ['ben', 52.0], ['denk', 15.0], ['wil', 13.0], ['acht', 1.0]]}, 'normalState'),
                ('{"lang:nl:0:Ik":[["heb", 66.0], ["ben", 52.0], ["denk", 15.0], ["wil", 13.0], ["acht", 1.0]]}', {'lang:nl:0:Ik':[['heb', 66.0], ['ben', 52.0], ['denk', 15.0], ['wil', 13.0], ['acht', 1.0]]}, 'normalState'),
                ('"lang:nl"', "Error load_json_string, jsonString, \'lang:nl\' needs to be string represetation of a json object, jsonString needs to be set between braces.  A str item needs to be set between double quotes.", 'errorState'),
                (b'"lang:nl"', "Error load_json_string, jsonString, \'lang:nl\' needs to be string represetation of a json object, jsonString needs to be set between braces.  A str item needs to be set between double quotes.", 'errorState'),
                (b'\'lang\':0"', "Error load_json_string, jsonString, \'lang:nl\' needs to be string represetation of a json object, jsonString needs to be set between braces.  A str item needs to be set between double quotes.", 'errorState'),
                (0, "Error load_json_string, jsonString, '0' needs to be a string.", 'errorState'),
            ]
        )
def test_load_json_from_string(testInput, expectedOutput, state):
    """utils, Json from string""" 
    #Test normal behavior  
    if state == 'normalState':
        assert load_json_string(testInput) == expectedOutput
        
    #Test expect error  
    if state == 'errorState':
        with pytest.raises(utilsError) as e:
            load_json_string(testInput)
            assert str(e.value) == expectedOutput

@pytest.mark.parametrize("testInput, expectedOutput, stripl, stripr, state",
            [
                ('lang:nl:0:Ik' ,b'"lang:nl:0:Ik":[["heb", 66.0], ["ben", 52.0], ["denk", 15.0], ["wil", 13.0], ["acht", 1.0]],\n',b'', b'','normalState'),
                ('lang:nl:0:Ik' ,b'lang:nl:0:Ik":[["heb", 66.0], ["ben", 52.0], ["denk", 15.0], ["wil", 13.0], ["acht", 1.0]]',b'"', b',\n','normalState'),
                ('lang:nl:0:Ik' ,b'lang:nl:0:Ik":[["heb", 66.0], ["ben", 52.0], ["denk", 15.0], ["wil", 13.0], ["acht", 1.0]],\n',b'"', b'','normalState'),
                ('NO-MATCH',False,False,False,'normalState'),
                ('NOEXISTINGFILE', "Error, grep_bigram_from_system: grep NOEXISTINGFILE: No such file or dictionary\n" , b'', b'','errorState'),
                ('lang:nl:0:Ik' ,b'"lang:nl:0:Ik":[["heb", 66.0], ["ben", 52.0], ["denk", 15.0], ["wil", 13.0], ["acht", 1.0]]',b'"', b',\n','defaultArguments'),
                ('lang:nl:0:Ik',"Error, grep_bigram_from_system: 'String_lstrip' needs to be a bytes type" , 'String_lstrip', b'','argErrorState'),
                ('lang:nl:0:Ik',"Error, grep_bigram_from_system: 'String_rstrip' needs to be a bytes type" , b'','String_rstrip','argErrorState'),
            ]
        )
def test_grep_bigram(raw_json_file,testInput, stripl, stripr, expectedOutput, state):
    """utils, Grep bigram from file with system grep""" 
    #Test default argument
    if state == 'defaultArguments':
        assert grep_bigram_from_system(testInput,raw_json_file) == expectedOutput
    #Test normal behavior  
    if state == 'normalState':
        assert grep_bigram_from_system(testInput,raw_json_file, stripl, stripr) == expectedOutput
        
    #Test expect error  
    if state == 'errorState':
        with pytest.raises(utilsError) as e:
            grep_bigram_from_system(testInput, testInput)
            assert str(e.value) == expectedOutput

    #Test expect error  
    if state == 'argErrorState':
        with pytest.raises(utilsError) as e:
            grep_bigram_from_system(testInput, raw_json_file, stripl, stripr)
            assert str(e.value) == expectedOutput
            
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
            ('love',['I', 'Love', 'python'],False, False),
            ('',['I', 'Love', 'python'], False, False),
            (None,['I', 'Love', 'python'], False, False),
            (None,"String", "Error: collection is not iterable or is a string", True),
            ('Love',8, "Error: collection is not iterable or is a string", True),
            ('Love',None, "Error: collection is not iterable or is a string",True),
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
