def logged(func_ref):
    def wrapper(*args):
        arguments = args
        return f"you called {func_ref.__name__}{arguments}\n" \
               f"it returned {func_ref(*args)}"

    return wrapper


@logged
def func(*args):
    return 3 + len(args)