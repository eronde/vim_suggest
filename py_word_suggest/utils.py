# py_word_suggest/utils.py
from . import export

@export
def is_empty(obj):
    """is_empty: Check if object is empty.
    :obj:
    :returns: Bool

    """
    return obj == '' or str(obj).isspace()
