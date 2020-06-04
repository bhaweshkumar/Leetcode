from collections import defaultdict


class PartitionArray:
    def partition(self, array):
        diction = defaultdict(set)
        diction[0].add(0)

        for i, elem in enumerate(array):
            current = i + 1
            for prev_diff in diction[current - 1]:
                diction[current].add(prev_diff - elem)
                diction[current].add(prev_diff + elem)
        return 0 in diction[len(array)]


test = PartitionArray()

print(test.partition([3, 1, 2]))
#print(test.partition([2, 4, 2, 2, 2]))
