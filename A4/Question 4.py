# def swap_indices(a_list, index_one, index_two):
#     a_list[index_one], a_list[index_two] = a_list[index_two], a_list[index_one]
#     return a_list
#
#
# def loop_through_items(a_list):
#     for number in a_list:
#         if a_list[number] > (a_list[number + 1]):
#             a_list = swap_indices(a_list, number, number + 1)
#     return a_list


def selection_sort(items):
    if not len(items):
        raise ValueError("Cannot enter an empty/ non-sortable list")
    sorted_items = []
    while items:
        lowest_num = items[0]
        for number in items:
            if number < lowest_num:
                lowest_num = number
        items.remove(lowest_num)
        sorted_items.append(lowest_num)

    return sorted_items


def main():
    print(selection_sort([10, 9, 8, 3, 2, 1]))


if __name__ == '__main__':
    main()
