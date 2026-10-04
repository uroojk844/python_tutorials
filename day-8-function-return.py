# def absquare(a: int, b: int) -> int:  # a,b = parameters
#     res = a * a + b * b + 2 * a * b
#     return res


# result = absquare(1, 3)  # 2, 3 arguments
# print(result)


# def square(num: int):
#     return num * num


# print(square(2))


def anySum(*params):
    return sum(params)


print(anySum(1, 2, 3, 4, 5, 6))
