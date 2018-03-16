from random import randrange

import sys


def is_palindrome(string):
    return string[::-1] == string


def naive(string):
    n = int(string) + 1
    while not is_palindrome(str(n)):
        n += 1

    return str(n)


def inc_char(c):
    return chr(ord(c) + 1)


def inc_array(array, position):
    while True:
        if position == -1:
            return ['1'] + array

        if array[position] != '9':
            array[position] = inc_char(array[position])
            return array
        else:
            array[position] = '0'
            position -= 1


def measure(array):
    length = len(array)
    mid = (length % 2 == 1)
    if mid:
        left_i = length // 2 - 1
        right_i = length // 2 + 1
    else:
        left_i = length // 2 - 1
        right_i = length // 2

    return length, left_i, mid, right_i


def solve(array):
    length, left_i, mid, right_i = measure(array)

    for i in range(length - right_i):
        if array[right_i + i] < array[left_i - i]:
            array[right_i + i] = array[left_i - i]
            if right_i + i + 1 < length:
                array[right_i + i + 1:] = array[left_i - i - 1::-1]
            break
        if array[right_i + i] > array[left_i - i]:
            array = inc_array(array, right_i + i)
            length, left_i, mid, right_i = measure(array)
            array[right_i + i + 1:] = ['0'] * (length - (right_i + i + 1))
            return solve(array)
    else:
        if mid and array[length // 2] != '9':
            array[length // 2] = inc_char(array[length // 2])
        else:
            array = inc_array(array, left_i)
            length, left_i, mid, right_i = measure(array)
            zero_start = right_i - 1 if mid else right_i
            array[zero_start:] = ['0'] * (length - zero_start)
            return solve(array)

    return ''.join(array)


def main():
    count = int(input())
    for _ in range(count):
        string = input()
        sys.stdout.write(solve(list(string)) + '\n')


def test():
    for i in range(1, 1001):
        naive_result = naive(str(i))
        result = solve(list(str(i)))
        assert result == naive_result, i


def test_fuzz():
    for _ in range(100):
        string = ''.join([str(randrange(8, 10)) for _ in range(randrange(1000, 100000))])
        assert is_palindrome(solve(list(string))), string
        print('*')


if __name__ == '__main__':
    try:
        main()
    except EOFError:
        pass

