def c_n_k(n, k):
    m = min(n - k, k)
    result = 1

    for i in range(1, m + 1):
        result *= (n - m + i)
        result //= i

    return result


def main():
    count = int(input())
    for _ in range(count):
        try:
            n, k = map(int, input().split())
        except EOFError:
            break

        print(int(c_n_k(n - 1, k - 1)))


if __name__ == '__main__':
    main()
