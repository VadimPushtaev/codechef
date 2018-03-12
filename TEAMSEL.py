class Team(object):
    def __init__(self):
        self.power = 0
        self.size = 0
        self.players = []

    def add(self, player):
        self.power += player
        self.size += 1
        self.players.append(player)

    def pop(self):
        player = self.players.pop()
        self.power -= player
        self.size -= 1

        return player


def solve(players):
    players.sort(reverse=True)

    a = Team()
    b = Team()

    for player in players:
        if a.power > b.power:
            b.add(player)
        else:
            a.add(player)
  
    if a.size > b.size:
        a, b = b, a

    while a.size < b.size - 1:
        a.add(b.pop())

    if a.power > b.power:
        a, b = b, a
    
    print a.players
    print b.players

    return '{} {}'.format(a.power, b.power)

tests_cnt = int(raw_input())

for _ in xrange(0, tests_cnt):
    assert raw_input() == ''

    players_cnt = int(raw_input())
    players = []
    for i in xrange(0, players_cnt):
        players.append(int(raw_input()))
    print solve(players)
