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

def main():
    name = "numbers.csv"
    data = read_data(name)
    return data


if __name__ == '__main__':
    hihi = main()
    print(hihi)

