def main():
    the_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    the_number_n = 5
    greater(the_list, the_number_n)


def greater(the_list, the_number_n):

    for num in the_list:
        if num > the_number_n:
            print(num)


main()
