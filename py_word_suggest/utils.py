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
