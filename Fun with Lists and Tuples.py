def sort_list_last(tuples):
    return sorted(tuples, key=lambda x: x[-1])

tuples = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
sorted_tuples = sort_list_last(tuples)
print(sorted_tuples)
