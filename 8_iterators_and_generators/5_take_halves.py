def solution():
    def integers():
        current_number = 1
        while True:
            yield current_number
            current_number += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        result = []
        for i in range(n):
            result.append(next(seq))
        return result

    return take, halves, integers