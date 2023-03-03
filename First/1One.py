# Sum of all list elements using recursion

list1 = [1, 2, 3, 4, 5, 63, 7, 8, 9]

def sum_list(list):
    if len(list) == 1:
        return list[0]
    else:
        return list[0] + sum_list(list[1:])


if __name__ == '__main__':
    s = sum_list(list1)
    print(s)
