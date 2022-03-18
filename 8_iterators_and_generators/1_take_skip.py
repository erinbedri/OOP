class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.current_number = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_number < self.count:
            result = self.step * self.current_number
            self.current_number += 1
            return result
        else:
            raise StopIteration