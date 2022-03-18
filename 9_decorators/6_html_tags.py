def tags(tag):
    def decorator(func):
        def wrapper(*args):
            arguments = args
            return f"<{tag}>{func(*arguments)}</{tag}>"
        return wrapper
    return decorator
