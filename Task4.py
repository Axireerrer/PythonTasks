array = list(map(str, input().split()))


def func4(a: list, flag=True) -> list:

    if len(a) <= 1:
        return a

    pivot = a[0]

    if flag:

        left_part = [x for x in a[1:] if len(x) <= len(pivot)]
        right_part = [x for x in a[1:] if len(x) > len(pivot)]
        increase = func4(left_part) + [pivot] + func4(right_part)

        return increase

    else:

        left_part = [x for x in a[1:] if len(x) <= len(pivot)]
        right_part = [x for x in a[1:] if len(x) > len(pivot)]
        increase = func4(left_part) + [pivot] + func4(right_part)
        decrease = increase[::-1]

        return decrease


print("Сортировка по возрастанию: ", func4(array, True))
print("Сортировка по убыванию: ", func4(array, False))



