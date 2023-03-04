import types


list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
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


def test_1(lst):
    for flat_iterator_item, check_item in zip(
            FlatIterator(lst),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item
    assert list(FlatIterator(lst)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


def test_3(lst):
    for flat_iterator_item, check_item in zip(
            FlatIterator(lst),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item
    assert list(FlatIterator(lst)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

###############  ГЕНЕРАТОР  ###################


def flat_generator(lst):
    for i in range(0, len(lst)):
        for j in range(0, len(lst[i])):
            yield lst[i][j]


def open_list_gen(lst):
    for item in flat_generator(lst):
        print(item)


def test_2(lst):
    for flat_iterator_item, check_item in zip(
            flat_generator(lst),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item
    assert list(flat_generator(lst)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


def test_4(lst):
    for flat_iterator_item, check_item in zip(
            flat_generator(lst),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item
    assert list(flat_generator(lst)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    assert isinstance(flat_generator(lst), types.GeneratorType)

if __name__ == '__main__':

    print('\nЗадание 1\n')
    open_list(list_of_lists_1)
    print(f'\n{"*" * 5}\n')
    horizon_list(list_of_lists_1)
    test_1(list_of_lists_1)
    print(f'\n{"*" * 5}\n')

    print('\nЗадание 2\n')
    open_list_gen(list_of_lists_1)
    test_2(list_of_lists_1)

    print('\nЗадание 3\n')
    open_list_gen(list_of_lists_2)
    test_3(list_of_lists_2)

    print('\nЗадание 4\n')
    open_list_gen(list_of_lists_2)
    test_4(list_of_lists_2)