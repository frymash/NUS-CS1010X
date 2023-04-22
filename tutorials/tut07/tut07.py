def make_queue():
    return []

def enqueue(q, item):
    q.insert(0, item)

def dequeue(q):
    return q.pop()
    
def size(q):
    return len(q)

def who_wins(m, players):
    q = make_queue()
    for player in players:
        enqueue(q, player)
    players_in_result = m-1
    players_until_bomb = m
    
    while size(q) != players_in_result:
        curr = dequeue(q)
        if players_until_bomb != 0:
            enqueue(q, curr)
            players_until_bomb -= 1
        else:
            players_until_bomb = m
    return q


print(set(who_wins(3, ['val', 'hel', 'jam', 'jin', 'tze', 'eli', 'zha', 'lic'])))
print(who_wins(2, ['poo', 'ste', 'sim', 'nic', 'luo', 'ibr', 'sie', 'zhu']))
