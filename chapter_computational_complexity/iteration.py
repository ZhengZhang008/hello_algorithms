def for_loop(n: int) -> int:
    result = 0
    # result = 1 + 2 + ... + (n-1) + n
    for i in range(1, n + 1):
        result += i
    return result


def while_loop(n: int) -> int:
    result = 0
    i = 1
    # result = 1 + 2 + ... + (n-1) + n
    while i <= n:
        result += i
        i += 1
    return result


def while_loop_ii(n: int) -> int:
    result = 0
    i = 1
    # result = 1 + 4 + 10
    while i <= n:
        result += i
        i += 1
        i *= 2
    return result


def nested_for_loop(n: int) -> str:
    result = ""
    # result = (1, 1), (1, 2), ... , (n, n)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            result += f"({i}, {j}), "
    return result


if __name__ == "__main__":
    n = 5
    result = for_loop(n)
    print(result)

    result = while_loop(n)
    print(result)

    result = while_loop_ii(n)
    print(result)

    result = nested_for_loop(n)
    print(result)
