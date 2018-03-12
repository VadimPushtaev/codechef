total = raw_input()

def even(x):
    return x % 2 == 0

while True:
    try:
        games = int(raw_input())
        for _ in xrange(0, games):
            init, n, question = map(int, raw_input().split())
            if even(n):
                print n/2
            else:
                if question == init:
                    print n/2
                else:
                    print n/2 + 1
    except EOFError:
        break
