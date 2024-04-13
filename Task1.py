array = list(map(int, input().split()))


def func1(a: list) -> list:

    if len(a) == 0:
        return []

    new_a = []

    for i in set(a):
        count = 0
        for j in range(len(a)):
            if i == a[j]:
                count += 1
        if count == 1:
            new_a.append(i)

    return new_a


print(func1(array))













