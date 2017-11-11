# py_word_suggest/utils.py
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
    try:
        return targetItem in collection
    except TypeError:
        raise SelectorError("Error: collection is None")

def is_iterable(obj):
    """is_empty: Check if object is iterable.
    :obj:
    :returns: Bool
    """
    try:
        return bool(iter(obj))
    except TypeError as e:
        return False
