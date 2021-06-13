my_list = ['а', 'б', 'в', 'г', 'д', 'е']


def binary_search(mass, item):
    low = 0
    high = len(mass) - 1

    while low <= high:
        mid = round((low + high) / 2)
        guess = mass[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


print(binary_search(my_list, 'е'))
