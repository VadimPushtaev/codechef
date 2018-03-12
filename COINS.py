def exchange(x):
    return (x/2, x/3, x/4)

cache = {0: 0}
def best_exchange(x):
    if x in cache:
        return cache[x]

    result = 0
    exchanged = exchange(x)
    if sum(exchanged) >= x:
        result = sum(best_exchange(y) for y in exchanged)
    else:
        result = x

    cache[x] = result
    return result

while True:
    try:
        x = raw_input()
    except EOFError:
        break

    print best_exchange(int(x))
