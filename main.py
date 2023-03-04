nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


class FlatIterator:

    def __init__(self, lst):
        self.list = lst

    def __iter__(self):
        self.itm = []
        self.counter = 0
        return self

    def __next__(self):
        self.itm = sum(self.list, start=[])
        if self.counter < len(self.itm):
            res = self.itm[self.counter]
            self.counter += 1
            return res
        else:
            raise StopIteration


def open_list(list_):
    for item in FlatIterator(list_):
        print(item)


if __name__ == '__main__':

    open_list(nested_list)


