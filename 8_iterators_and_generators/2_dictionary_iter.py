class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.dict_lst = list(dictionary.items())
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < len(self.dictionary):
            output = self.dict_lst[self.idx]
            self.idx += 1
            return output
        else:
            raise StopIteration