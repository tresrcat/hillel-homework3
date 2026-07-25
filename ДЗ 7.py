from functools import wraps
def shout(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return result.upper()
        return result
    return wrapper
def positive_only(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)) or arg <= 0:
                raise ValueError("Усі позиційні аргументи мають бути додатними числами")
        return func(*args, **kwargs)
    return wrapper
@positive_only
def add_two(x):
    return x + 2
@shout
def add_suffix(value):
    return value + "suffix"