def type_check(input_type):
    def decorator(ref_function):
        def wrapper(parameter):
            if isinstance(parameter, input_type):
                return ref_function(parameter)
            return "Bad Type"
        return wrapper
    return decorator