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


def selection_sort(my_list, direction='upward'):
    """
    selection sorting
    :param direction: ('downward'/'upward') upward/downward sorting
    :param my_list: unordered list of int
    :return: my_list (ordered list of int)
    """
    right_border = 0
    while right_border < len(my_list) - 1:
        min_no = my_list[right_border]
        min_idx = 0
        for idx, no in enumerate(my_list[right_border:]):
            if no < min_no:
                min_no = no
                min_idx = idx
        my_list[right_border], my_list[min_idx + right_border] = my_list[min_idx + right_border], my_list[right_border]
        right_border += 1
    if direction == 'downward':
        my_downward_list = []
        for number in my_list:
            my_downward_list.insert(0, number)
        return my_downward_list
    return my_list


def main():
    numbers = read_data("numbers.csv")
    print(numbers)
    sorted_list = selection_sort(numbers['series_1'], 'downward')
    print(sorted_list)


if __name__ == '__main__':
    main()
