def make_bold(ref_func):
    def wrapper(*text):
        return "<b>" + f"{ref_func(*text)}" + "</b>"
    return wrapper


def make_italic(ref_func):
    def wrapper(*text):
        return "<i>" + f"{ref_func(*text)}" + "</i>"
    return wrapper


def make_underline(ref_func):
    def wrapper(*text):
        return "<u>" + f"{ref_func(*text)}" + "</u>"
    return wrapper