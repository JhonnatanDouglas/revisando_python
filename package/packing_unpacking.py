def packing(a: int, b: int, c: int) -> None:
    values = a, b, c
    total = sum(values)
    print(values)
    print(total)


def unpacking(values: list[int]) -> None:
    # a, b, c, d = values
    # print(a, b, c, d)

    n1, n2, *rest = values  # n1, n2, rest... = values  ||| no js
    print(n1, n2, rest)


def unpacking_dict(values: dict) -> None:
    key_1, key_2, key_3 = values
    print(key_1, key_2, key_3)
