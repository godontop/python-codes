# 如果没有下一个元素，会抛出异常。在本例中，若迭代器的元素的个数为奇数，则会抛出
# StopIteration异常
iter1 = iter([2, 3, 4, 5, 6, 7, 8, 9])
for i in iter1:
    n = next(iter1)
    print(n)
