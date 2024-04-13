num1 = int(input())
num2 = int(input())


def func2(a: int, b: int) -> list:

    if a == 0 and b == 0:
        return []

    simple_num = []

    for i in range(a, b + 1):

        count = 0

        for j in range(a, b + 1):

            if i % j == 0:
                count += 1

        if count <= 2:
            simple_num.append(i)

    return simple_num


print(func2(num1, num2))

