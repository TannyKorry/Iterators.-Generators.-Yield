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


# fi = FlatIterator(nested_list)

# for item in FlatIterator(nested_list):
    # print(item)




# flat_list = [item for item in FlatIterator(nested_list)]
#
# print(flat_list)


nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

for i in range(0, len(nested_list)):
    # print(nested_list[i])
    for j in range(0, len(nested_list[i])):
        print(nested_list[i][j])


