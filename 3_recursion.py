def recursion_sum(mass):
    if not mass:
        return 0
    else:
        return mass[0] + recursion_sum(mass[1:])


def recursion_count(mass):
    if not mass:
        return 0
    else:
        return 1 + recursion_count(mass[1:])


def recursion_max(mass):
    if len(mass) == 2:
        if mass[0] > mass[1]:
            return mass[0]
        else:
            return mass[1]
    sub_max = max(mass[1:])
    return mass[0] if mass[0] > sub_max else sub_max


arr = [5123, 1095, 12, 4, 5]
print("summ = ", recursion_sum(arr))
print("count = ", recursion_count(arr))
print("max = ", recursion_max(arr))
