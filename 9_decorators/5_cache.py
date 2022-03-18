def cache(func):
    log = {}

    def wrapper(n):
        if n in log:
            return log[n]
        else:
            log[n] = func(n)
            return log[n]

    wrapper.log = log

    return wrapper