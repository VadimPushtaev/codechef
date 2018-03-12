import sys

a, b = raw_input().split()

result = int(a) - int(b) + 1

print(result if result % 10 else result - 2)
