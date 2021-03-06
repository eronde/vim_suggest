from py_word_suggest.utils import *
import pytest
raw_json = """
{"lang:nl:0:ben":[["ik", 22.0], ["er", 8.0], ["een", 7.0], ["je", 5.0]],"lang:nl:0:Ik":[["heb", 66.0], ["ben", 52.0], ["denk", 15.0], [
    "wil", 13.0], ["acht", 1.0]],"lang:eng:0:I":[["am", 100], ["want", 246], ["love", 999]],"lang:eng:0:am":[["the",100], ["Alice", 50],["Bob", 45]]}
"""
invalid_json = """
test
"""


@pytest.fixture(scope="session")
def invalid_json_file(tmpdir_factory):
    fn = tmpdir_factory.mktemp("data_tmp").join("test_invalid.json")
    fn.write(invalid_json)
    invalid_json_fn = fn
    return fn


@pytest.fixture(scope="session")
def raw_json_file(tmpdir_factory):
    f = tmpdir_factory.mktemp("data_tmp").join("test.json")
    f.write(raw_json)
    return f


def setUp(invalid_json_file):
    invalid_json_file


@pytest.mark.parametrize("testInput, expectedOutput, state",
                         [
                             (b'{"lang:nl:0:Ik":[["heb", 66.0], ["ben", 52.0], ["denk", 15.0], ["wil", 13.0], ["acht", 1.0]]}', {
                              'lang:nl:0:Ik': [['heb', 66.0], ['ben', 52.0], ['denk', 15.0], ['wil', 13.0], ['acht', 1.0]]}, 'normalState'),
                             ('{"lang:nl:0:Ik":[["heb", 66.0], ["ben", 52.0], ["denk", 15.0], ["wil", 13.0], ["acht", 1.0]]}', {
                              'lang:nl:0:Ik': [['heb', 66.0], ['ben', 52.0], ['denk', 15.0], ['wil', 13.0], ['acht', 1.0]]}, 'normalState'),
                             ('"lang:nl"', "Error load_json_string, jsonString, '\"lang:nl\"' needs to be a string represetation of a json object, jsonString needs to be set between braces. A str item needs to be set between double quotes.", 'errorState'),
                             (b'"lang:nl"', "Error load_json_string, jsonString, 'b'\"lang:nl\"'' needs to be a string represetation of a json object, jsonString needs to be set between braces. A str item needs to be set between double quotes.", 'errorState'),
                             (b'\'lang\':0"', "Error load_json_string, jsonString, 'b'\\'lang\\':0\"'' needs to be a string represetation of a json object, jsonString needs to be set between braces. A str item needs to be set between double quotes.", 'errorState'),
                             (0, "Error load_json_string, jsonString, '0' needs to be a string represetation of a json object, jsonString needs to be set between braces. A str item needs to be set between double quotes.", 'errorState'),
                         ]
                         )
def test_load_json_from_string(testInput, expectedOutput, state):
    """utils, Json from string"""
    # Test normal behavior
    if state == 'normalState':
        assert load_json_string(testInput) == expectedOutput

    # Test expect error
    if state == 'errorState':
        with pytest.raises(utilsError) as e:
            load_json_string(testInput)
        assert str(e.value) == expectedOutput


@pytest.mark.parametrize("testInput, expectedOutput, state",
                         [
                             ('\"lang:nl:0:Ik\"', {"lang:nl:0:Ik": [["heb", 66.0], ["ben", 52.0], [
                              "denk", 15.0], ["wil", 13.0], ["acht", 1.0]]}, 'normalState'),
                             ('\"lang:nl:0:Ik', "Error, grep_jsonstring_from_system: '\"lang:nl:0:Ik' needs to be a str type and need to be between double quotes.", 'errorState'),
                             ('lang:nl:0:Ik\"', "Error, grep_jsonstring_from_system: 'lang:nl:0:Ik\"' needs to be a str type and need to be between double quotes.", 'errorState'),
                             ('lang:nl:0:Ik', "Error, grep_jsonstring_from_system: 'lang:nl:0:Ik' needs to be a str type and need to be between double quotes.", 'errorState'),
                             (0, "Error, grep_jsonstring_from_system: '0' needs to be a str type and need to be between double quotes.", 'errorState'),
                             ('\"NoKeyFound\"', False, 'normalState'),

                             ('\"NO-MATCH\"', False, 'normalState'),
                             ('\"NOEXISTINGFILE\"', "Error, grep_jsonstring_from_system: File NOEXISTINGFILE not exists or is busy.", 'fileError'),
                             # ('lang:nl:0:Ik' ,b'"lang:nl:0:Ik":[["heb", 66.0], ["ben", 52.0], ["denk", 15.0], ["wil", 13.0], ["acht", 1.0]]','":.*]]','defaultArguments'),
                         ]
                         )
def test_grep_jsonstring_from_system(raw_json_file, testInput, expectedOutput, state):
    """utils, Grep bigram from file with system jq util"""
    # Test default argument
    if state == 'fileError':
        raw_json_file = 'NOEXISTINGFILE'
        with pytest.raises(utilsError) as e:
            grep_jsonstring_from_system(testInput, raw_json_file)
        assert str(e.value) == expectedOutput
    # Test normal behavior
    if state == 'normalState':
        assert grep_jsonstring_from_system(
            testInput, raw_json_file) == expectedOutput

    # Test expect error
    if state == 'errorState':
        # pudb.set_trace()
        with pytest.raises(utilsError) as e:
            grep_jsonstring_from_system(testInput, raw_json_file)
            # pudb.set_trace()
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
def test_is_empty(testInput, expected_output):
    """utils, is_empty: Check if an object is empty or contains spaces"""
    assert is_empty(testInput) == expected_output


@pytest.mark.parametrize("testInput,expectedOutput",
                         [
                             ("String", True),
                             (['lol,lol2'], True),
                             (('lol', 'lol2'), True),
                             ({'lol', 'lol2'}, True),
                             (10, False),
                             (None, False)
                         ]
                         )
def test_is_iterable(testInput, expectedOutput):
    """utils, is_iterable Check if an object is iterable"""
    assert is_iterable(testInput) == expectedOutput


@pytest.mark.parametrize("testInput, collection, expectedOutput, errorState",
                         [
                             ('Love', ['I', 'Love', 'python'], True, False),
                             ('love', ['I', 'Love', 'python'], False, False),
                             ('', ['I', 'Love', 'python'], False, False),
                             (None, ['I', 'Love', 'python'], False, False),
                             (None, "String",
                              "Error: collection is not iterable or is a string", True),
                             ('Love', 8, "Error: collection is not iterable or is a string", True), (
                                 'Love', None, "Error: collection is not iterable or is a string", True),
                         ]
                         )
def test_containing(testInput, collection,  expectedOutput, errorState):
    """utils: Check if collection contains an item"""
    if errorState is False:
        assert containing(collection, testInput) == expectedOutput
    else:
        with pytest.raises(utilsError) as e:
            containing(collection, testInput)
        assert str(e.value) == expectedOutput


@pytest.mark.parametrize("testInput, expectedOutput, state",
                         [
                             (None, {"lang:nl:0:ben": [["ik", 22.0], ["er", 8.0], ["een", 7.0], ["je", 5.0]], "lang:nl:0:Ik":[["heb", 66.0], ["ben", 52.0], ["denk", 15.0], [
                                 "wil", 13.0], ["acht", 1.0]], "lang:eng:0:I":[["am", 100], ["want", 246], ["love", 999]], "lang:eng:0:am":[["the", 100], ["Alice", 50], ["Bob", 45]]}, 'normalState'),
                             (None, "Error, load_data_from_json: \'NOEXISTINGFILE\' does not exists.",
                              'noFileExistState'),
                             (None, "Error, load_data_from_json: '{}' needs to be a json object.",
                              'invalidJsonState'),
                             (None, "Error, load_data_from_json: Function recuires a filename (str).",
                              'ValueErrorState'),
                             (13458, "Error, load_data_from_json: Function recuires a filename (str).",
                              'ValueErrorState'),
                             (True, "Error, load_data_from_json: Function recuires a filename (str).",
                              'ValueErrorState'),
                             (False, "Error, load_data_from_json: Function recuires a filename (str).",
                              'ValueErrorState'),

                         ]
                         )
def test_load_json_from_file(raw_json_file, invalid_json_file, testInput, expectedOutput, state):
    """utils, load json data from file"""
    # Test default argument
    # Test normal behavior
    if state == 'normalState':
        assert load_data_from_json(str(raw_json_file)) == expectedOutput
    # Test noFileExistState
    if state == 'noFileExistState':
        raw_json_file = 'NOEXISTINGFILE'
        with pytest.raises(FileNotFoundError) as e:
            load_data_from_json(raw_json_file)
        assert str(e.value) == expectedOutput

    # Test invalid_json_file error
    if state == 'invalidJsonState':
        with pytest.raises(utilsError) as e:
            load_data_from_json(str(invalid_json_file))
        assert str(e.value) == expectedOutput.format(str(invalid_json_file))

    # Test noFileExistState
    if state == 'ValueErrorState':
        with pytest.raises(ValueError) as e:
            load_data_from_json(testInput)
        assert str(e.value) == expectedOutput
