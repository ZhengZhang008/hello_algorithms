def recur(n: int) -> int:
    # f(n) = n + f(n - 1)
    if n == 1:
        return 1
    result = recur(n - 1)
    return n + result


def for_loop_recur(n: int) -> int:
    # Use an explicit stack to emulate a system call stack
    stack = []
    result = 0
    # Recursive
    for i in range(n, 0, -1):
        stack.append(i)
    # Return
    while stack:
        result += stack.pop()
    return result


def tail_recur(n, result):
    # Tail recursion
    if n == 0:
        return result
    return tail_recur(n - 1, result + n)


def fib(n: int) -> int:
    # f(1) = 0, f(2) = 1
    if n == 1 or n == 2:
        return n - 1
    # f(n) = f(n-1) + f(n-2)
    result = fib(n - 1) + fib(n - 2)
    return result


if __name__ == "__main__":
    n = 5
    result = recur(n)
    print(result)

    result = for_loop_recur(n)
    print(result)

    result = tail_recur(n, 0)
    print(result)

    result = fib(n)
    print(result)
