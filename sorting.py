import os
import csv


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    data = {}
    with open(file_path, mode="r") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            for key in row:
                if key not in data:
                    data[key] = []
                data[key].append(int(row[key]))
    return data


def selection_sort(my_list, direction='ascending'):
    """
    selection sorting
    :param direction: ('ascending'/'descending') ascending/descending sorting
    :param my_list: unordered list of int
    :return: my_list (ordered list of int)
    """
    left_border = 0
    while left_border < len(my_list) - 1:
        min_no = my_list[left_border]
        min_idx = 0
        for idx, no in enumerate(my_list[left_border:]):
            if direction == 'ascending':
                if no < min_no:
                    min_no = no
                    min_idx = idx
            if direction == 'descending':
                if no > min_no:
                    min_no = no
                    min_idx = idx
        my_list[left_border], my_list[min_idx + left_border] = my_list[min_idx + left_border], my_list[left_border]
        left_border += 1
    return my_list


def bubble_sort(my_list):
    """
    upward buble sorting of int
    :param my_list: unordered list of int
    :return: my_list (ordered list of int)
    """
    right_border = len(my_list) - 1
    while right_border > 0:
        right = 0
        idx = 0
        while idx < right_border:
            if my_list[idx] > my_list[idx + 1]:
                my_list[idx], my_list[idx + 1] = my_list[idx + 1], my_list[idx]
                right = idx
            idx += 1
        right_border = right
    return my_list


def insertion_sort(my_list):
    """
    insertion sort of int
    :param my_list: unordered list of int
    :return: my list (ordered list of int)
    """
    sort_idx = 1
    while sort_idx < len(my_list):
        num = my_list[sort_idx]
        i = sort_idx - 1
        while i >= 0:
            if num < my_list[i]:
                my_list[i + 1] = my_list[i]
                i -= 1
                if i == -1:
                    my_list[0] = num
            else:
                my_list[i + 1] = num
                i = -1
        sort_idx += 1
    return my_list


def main():
    numbers = read_data("numbers.csv")
    print(numbers)
    selected_list = selection_sort(numbers['series_1'], 'descending')
    print(selected_list)
    bubbled_list = bubble_sort(numbers['series_2'])
    print(bubbled_list)
    inserted_list = insertion_sort(numbers['series_3'])
    print(inserted_list)


if __name__ == '__main__':
    main()
