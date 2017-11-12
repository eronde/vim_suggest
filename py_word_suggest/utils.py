# py_word_suggest/utils.py
class utilsError(Exception): pass
from . import export

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

