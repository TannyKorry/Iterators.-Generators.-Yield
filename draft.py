# nested_list = [
# 	['a', 'b', 'c'],
# 	['d', 'e', 'f', 'h', False],
# 	[1, 2, None],
# ]
#
# class FlatIterator:
#
#     def __init__(self, list):
#         self.list = list
#
#     def __iter__(self):
#         self.itm = []
#
#         return self
#
#     def __next__(self):
#         summ = 0
#         for i in range(0, len(self.list)):
#             summ += len(self.list[i])
#             for j in range(0, len(self.list[i])):
#                 if summ < len(self.itm):
#                     raise StopIteration
#                 self.itm.append(self.list[i][j])
#         print(self.itm)
#         for x in range(0, len(self.itm)):
#             print(self.itm[x])
#             return self.itm[x]
##############################################################################################

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

for item in FlatIterator(nested_list):
    print(item)

# itm = []
#
# for i in nested_list:
#     for j in i:
#         itm.append(j)
# print(itm)
# for x in itm:
#     print(x)
