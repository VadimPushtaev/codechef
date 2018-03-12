def order(steps):
    ordered = []
    result = []

    i = 1
    for step in steps:
        ordered.insert(len(ordered) - step, i)
        i += 1
   
    index = {ordered[j]: j+1 for j in xrange(0, len(ordered))}

    for j in xrange(0, len(ordered)):
        result.append(index[j+1])
    
    return ' '.join(map(str, result))

raw_input()
while True:
    try:
        raw_input()
        steps = map(int, raw_input().split())
    except EOFError:
        break

    print order(steps)

