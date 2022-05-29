import unittest


def merge_sort(a):
    if len(a) < 2:
        return a[:]
    else:
        median = int(len(a) / 2)
        left = merge_sort(a[:median])
        right = merge_sort(a[median:])
        return merge(left, right)


def merge(left, right):
    res = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    while i < len(left):
        res.append(left[i])
        i += 1
    while j < len(right):
        res.append(right[j])
        j += 1
    return res


class TestMergeSort(unittest.TestCase):

    def test1(self):
        lst = [7, 2, 4, 1, 9, 12, 63, 21, 34]
        self.assertEqual(merge_sort(lst), sorted(lst))

    def test2(self):
        lst = [0, 2, 4, 1, 9, 12, 0, 21]
        self.assertEqual(merge_sort(lst), sorted(lst))

    def test3(self):
        lst = [100, -2, 0, 6]
        self.assertEqual(merge_sort(lst), sorted(lst))


unittest.main()
