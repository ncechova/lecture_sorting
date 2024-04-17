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
    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)
        data = dict()
        for row_num, row in enumerate(reader):
            for key, value in row.items():
                if row_num == 0:
                    data[key] = []
                data[key].append(int(value))
    return data

def selection_sort(list_of_nums, direction="sestupne"):
    for x in range(len(list_of_nums)):
        if direction == "vzestupne":
            smallest_num = list_of_nums[x]
            smallest_pos = x
            for position in range(x, len(list_of_nums)):
                number = list_of_nums[position]
                if number < smallest_num:
                    smallest_num = number
                    smallest_pos = position
            list_of_nums[smallest_pos], list_of_nums[x] = list_of_nums[x], list_of_nums[smallest_pos]
        if direction == "sestupne":
            highest_num = list_of_nums[x]
            highest_pos = x
            for position in range(x, len(list_of_nums)):
                number = list_of_nums[position]
                if number > highest_num:
                    highest_num = number
                    highest_pos = position
            list_of_nums[highest_pos], list_of_nums[x] = list_of_nums[x], list_of_nums[highest_pos]
    return list_of_nums

def bubble_sort(list_of_nums):
    idx = 0
    while idx < (len(list_of_nums)-1):
        for x in range(idx, len(list_of_nums)):
            if list_of_nums[idx] > list_of_nums[x]:
                list_of_nums[idx], list_of_nums[x] = list_of_nums[x], list_of_nums[idx]
        idx += 1
    return list_of_nums

def insertion_sort(list_of_nums):
    for i in range(1, len(list_of_nums)):
        number = list_of_nums[i]
        sorted_numbers = list_of_nums[:i]
        for sorted_num in sorted_numbers:
            x = sorted_numbers.index(sorted_num)
            num_idx = list_of_nums.index(number)
            if number < sorted_num and num_idx > x:
                list_of_nums.pop(i)
                list_of_nums.insert(x, number)
    return list_of_nums

def main():
    name = "numbers.csv"
    data = read_data(name)
    nums = [88, 36, 21, 54, 99, 1, 81, 18, 61]
    sorted_nums = insertion_sort(nums)
    return sorted_nums


if __name__ == '__main__':
    hihi = main()
    print(hihi)

