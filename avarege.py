#!/usr/bin/env python3

# Created by: Mariam
# Created on: Dec 2019
# This program uses a 2D array

import random


def average_of_numbers(passed_in_2D_list, row_1, columns_1):
    # this function adds up all the elements in  a 2D array

    total = 0
    average = 0
    for row_value in passed_in_2D_list:
        for single_element in row_value:
            total += single_element
            average = total / (columns_1*row_1)

    return average


def main():
    # this function uses a 2D array

    a_2d_list = []

    # input
    rows = int(input("How many row would you like: "))
    columns = int(input("How many columns would you like: "))

    for loop_counter_rows in range(0, rows):
        temp_column = []
        for loop_counter_columns in range(0, columns):
            a_random_number = random.randint(0, 51)
            temp_column.append(a_random_number)
            print("{0} ".format(a_random_number), end="")
        a_2d_list.append(temp_column)
        print("")

    average = average_of_numbers(a_2d_list, rows, columns)
    print("The average_of_numbers : {0} ".format(average))


if __name__ == "__main__":
    main()
