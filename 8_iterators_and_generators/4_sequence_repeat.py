class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.current_idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_idx < self.number:
            output = self.sequence[self.current_idx % len(self.sequence)]
            self.current_idx += 1
            return output
        else:
            raise StopIteration