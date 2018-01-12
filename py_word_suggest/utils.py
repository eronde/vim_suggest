# py_word_suggest/utils.py
class utilsError(Exception): pass
from json import dump, load, loads
from . import export
from subprocess import PIPE, Popen

@export
def is_empty(obj):
    """is_empty: Check if str object is empty.
    :obj:
    :returns: Bool

    """
    if isinstance(obj, str):
        return not bool(obj.strip() and ' ' not in obj)
    elif obj is None:
        return True
    else:
        return obj == '' or str(obj).isspace()

def containing(collection, targetItem):
    """containing: Checks if a item is or is not in a collection of items
    :items: collection of items
    :targetItem: 
    :returns: bool
    """
    if is_iterable(collection) and not isinstance(collection,str):
        return targetItem in collection
    else:
        raise utilsError("Error: collection is not iterable or is a string")

def is_iterable(obj):
    """is_empty: Check if object is iterable.
    :obj:
    :returns: Bool
    """
    try:
        return bool(iter(obj))
    except TypeError as e:
        return False

def load_data_from_json(filename):
    """load_data_from_json: Load data from json file 
    :obj:
    :returns: dict
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return load(f)
    except Exception as e:
        print(e)

def grep_bigram_from_system(pattern, filename, stripl=b'', stripr=b',\n'):
    """grep_bigram_from_system: Check if pattern exists in a file, using gnu_grep
    :pattern: str, pattern to find 
    :filename: file
    :stripl: bytes, strip output starting at the left
    :stripr: bytes, strip output starting at the right
    :returns: str/exception/False

    """
    grep = Popen(['grep', pattern, filename], stdout=PIPE, stderr=PIPE)
    pat, err = grep.communicate()
    #Return if pattern not exists
    if len(err) is 0 and len(pat) is 0:
        return False
   #Return error if grep produces an error 
    if len(err) is not 0:
        raise utilsError("Error, grep_bigram_from_system: {}".format(err))

    #Strip output of grep
    if isinstance(stripl, bytes):
        pat = pat.lstrip(stripl)
    else:
        raise utilsError("Error, grep_bigram_from_system: {} needs to be a bytes type".format(stripl))
    if isinstance(stripr, bytes):
        pat = pat.rstrip(stripr)
    else:
        raise utilsError("Error, grep_bigram_from_system: '{}' needs to be a bytes type".format(stripr))
    return pat

def load_json_string(jsonString):
    """load_json_string: Load json  object from string
    :jsonString: str/bytes, string represetation of a json object, like {"key":"value"}. A str item needs to be set between double quotes 
    :returns: dict
    """
    hasBraces = 0 
    if isinstance(jsonString, bytes):
        if jsonString.endswith(b'}') and jsonString.startswith(b'{'):
            hasBraces = 1
        # else:pass
    # else:pass
    #Check if jsonString str is set between braces
    if isinstance(jsonString, str):
        if jsonString.endswith('}') and jsonString.startswith('{'):
            hasBraces = 1
        # else:pass
    # else:pass

    if not hasBraces:
            raise utilsError("Error load_json_string, jsonString, '{k}' needs to be string represetation of a json object, jsonString needs to be set between braces. A str item needs to be set between double quotes.".format(k=jsonString))
    # else:pass 
    
    if not isinstance(jsonString, str) and not isinstance(jsonString, bytes):
        raise utilsError("Error load_json_string, jsonString, '{}' needs to be a string.".format(jsonString))                   
    # else:pass
    try:
        return loads(jsonString)
    except Exception as e:
            raise utilsError("Error load_json_string, jsonString, '{k}' needs to be string represetation of a json object, jsonString needs to be set between braces. A str item needs to be set between double quotes.".format(k=jsonString))
