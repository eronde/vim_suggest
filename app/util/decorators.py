import wrapt
# from utils import is_empty
from app.util.utils import is_empty


class DecoratorError(Exception): pass


def empty_arguments(errorType):
    """empty_arguments: Decorator, to check if any given args (not kwargs) has a space or is empty
    :errorType: Raise this type of Exception
    :TODO: Validate errorType, test
    :return: function/raiss
    """
    @wrapt.decorator
    def wrapper(wrapped, instance, args, kwargs):
        #Test if given args are empty
        for item in (x for x in args):
            if is_empty(item):
                raise errorType("Error in '{f}': One of the given arguments '{a}' are empty.".format(f=wrapped.__name__,a=args))
        return wrapped(*args, **kwargs)
    return wrapper

# @empty_arguments(IndexError)
# def function(text):
#     print(text)

# if __name__ == "__main__":
#     function("",'')
