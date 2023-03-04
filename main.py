nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

###############  ИТЕРАТОР  ###################

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


def horizon_list(list_):
    flat_list = [item for item in FlatIterator(list_)]
    print(flat_list)

###############  ГЕНЕРАТОР  ###################

def flat_generator(lst):
    for i in range(0, len(nested_list)):
        for j in range(0, len(nested_list[i])):
            yield nested_list[i][j]


def open_list_gen(lst):
    for item in flat_generator(nested_list):
        print(item)


if __name__ == '__main__':

    print('\nЗадание 1\n')
    open_list(nested_list)
    print(f'{"*" * 50}\n')
    horizon_list(nested_list)

    print('\nЗадание 2\n')
    open_list_gen(nested_list)
