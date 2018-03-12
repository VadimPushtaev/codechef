from math import sqrt

def primes(n, m):
    if n == 1:
        n = 2
    candidates = range(n, m+1)
    for divider in xrange(2, int(sqrt(m)) + 1):
        mod = n % divider
        i = divider - mod if mod else 0
        while i < len(candidates):
            if candidates[i] != divider:
                candidates[i] = 0
            i += divider
    
    return candidates            


first = True
raw_input()
while True:
    try:
        n, m = map(int, raw_input().split())
    except EOFError:
        break
    
    if not first:
        print

    for i in primes(n, m):
        if i > 0:
            print i

    first = False
