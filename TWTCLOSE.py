class Twits(object):
    def __init__(self):
        self._clicked = {}
        self._opened_cnt = 0

    def click(self, n):
        if self._clicked.get(n):
            self._clicked[n] = 0
            self._opened_cnt -= 1
        else:
            self._clicked[n] = 1
            self._opened_cnt += 1

    def close_all(self):
        self._clicked = {}
        self._opened_cnt = 0
    
    def get_opened_cnt(self):
        return self._opened_cnt


raw_input()
tw = Twits()
while True:
    try:
        x = raw_input().split()
    except EOFError:
        break

    if len(x) == 1:
        tw.close_all()
    else:
        tw.click(int(x[1]))

    print tw.get_opened_cnt()

        
