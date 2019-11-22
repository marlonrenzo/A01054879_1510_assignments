def selection_sort(items):
    if not len(items):
        raise ValueError("Cannot enter an empty or non-sortable list")
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
    print(selection_sort([]))


if __name__ == '__main__':
    main()
