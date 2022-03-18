def even_parameters(ref_func):
    def wrapper(*args):
        arguments = args
        for argument in arguments:
            if not isinstance(argument, int) or not argument % 2 == 0:
                return "Please use only even numbers!"
        return ref_func(*arguments)

    return wrapper