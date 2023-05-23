# Question 1

def accumulate(op, init, seq):
    if not seq:
        return init
    else:
        return op(seq[0], accumulate(op, init, seq[1:]))
def accumulate_n(op, init, sequences):
    if (not sequences) or (not sequences[0]):
        return type(sequences)()
    else:
        T1 = [seq[0] for seq in sequences]
        T2 = [seq[1:] for seq in sequences]
        # T1 = list(map(lambda x: x[0], sequences))
        # T1 = list(map(lambda x: x[1:], sequences))
        return ([accumulate(op, init, T1)]
               + accumulate_n(op, init, T2))
    
    
# Question 2

def col_sum(m):
    return accumulate_n(lambda x,y: x+y, 0, m)


# Question 3

def transpose(m):
    return accumulate_n(lambda x,xs: [x] + xs, [], m)

def transpose(m):
    op = lambda x,xs: [x] + xs
    init = []
    sequences = m
    return accumulate_n(op, init, sequences)

"""
def transpose(m):
    if m == []:
        return []
    return [list(map(lambda x: x[i],m)) for i in range(len(m[0]))]
"""

def row_sum(m):
    return accumulate_n(lambda x,y: x+y, 0, transpose(m))

# Question 4

def count_words(sentence):
    return accumulate(lambda x,y: 1+y, 0, sentence)

def count_letters(sentence):
    return accumulate(lambda x,y: len(x)+1+y, -1, sentence)

def count_sentence(sentence):
    return [count_words(sentence), count_letters(sentence)]

"""
TA Jiaqi's answer:

def count_sentence(sentence):
    n_words = len(sentence)
    n_letters = n_words - 1
    for word in sentence:
        n_letters += len(word)
    return [n_words, n_letters]

# Time: O(w), where w is the number of words
# Space: O(1)

def count_sentence(sentence):
    n_words = len(sentence)
    n_letters = n_words - 1
    n_letters += sum(list(map(len, sentence)))
    return [n_words, n_letters]

# Time: O(w), where w is the number of words
# Space: O(w) (since we use map over w elements, we need O(w) space to
#             store the results.)

def count_sentence(sentence):
    n_words = len(sentence)
    n_letters = n_words - 1
    n_letters += sum(map(len, sentence))
    return [n_words, n_letters]

# Time: O(w), where w is the number of words
# Space: O(1). Without the list conversion, we don't need to store
# the elements in the map object (which will be lazily evaluated 
# i.e. evaluated after it is passed to sum, not before)

# Why is n_letters defined as n_words - 1?
# Because that's the number of spaces we have before we account for
# the rest of the letters in the sentence

def count_sentence(sentence):
    n_words = len(sentence)
    op = lambda x,y: len(x) + y
    init = n_words - 1 
    sequence = sentence
    n_letters = accumulate(op, init, sequence)
    return [n_words, n_letters]
"""

# Question 5

def letter_count(sentence):
    result = []
    
    # Best case: O(1) if result is an empty list
    # Worst case: O(n) (where n is the number of letters in the sentence)
    #             if the letter being inserted is the last one in the sentence
    #             In that case, result will be n-1 elements long
    # Number of operations: 3 + 4 + 6 + 8 + 10 + ... + (2(n-1)+2)
    # By AP sum, 3 + ((n-1)/2)*(2(4) + ((n-1)-1)(2))
    #           = 3 + ((n-1)/2)*(4 + 2n)
    #           = 3 + (n-1)*(2+n)
    #           = 3 + (n^2 + n - 2)
    #           => O(n^2)
    def insert_letter(letter):
        for index in range(len(result)):
            if result[index][0] == letter:
                result[index] = [letter, result[index][1] + 1]
                return result
        result.append([letter, 1])
        return result
    
    # O(n) op is repeated n times
    for word in sentence:
        for letter in word:
            insert_letter(letter)
    return result

"""
TA Jiaqi's answers:

def letter_count(sentence):
    freq = [0] * 26
    for word in sentence:
        for c in word:
            idx = ord(c) - ord('a')
            freq[idx] += 1
    res = []
    for i in range(26):
        if freq[i] != 0:
            c = chr(i + ord('a'))
            res.append([c, freq[i]])
    return res

def letter_count(sentence):
    freq = {}
    for word in sentence:
        for c in word:
            freq[c] = freq.get(c,0) + 1
    res = []
    for key in freq:
        res.append([key,freq[key]])
    return res

# Time: O(n), where n = no. of letters in the sentence
# Space: O(1)

from collections import defaultdict

def letter_count(sentence):
    freq = defaultdict(int)
    for word in sentence:
        for c in word:
            freq[c] += 1
    res = []
    for key in freq:
        res.append([key,freq[key]])
    return res
"""


# Question 6

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

# TA Jiaqi's answer
def who_wins(m, lst):
    q = make_queue()
    for player in lst:
        enqueue(q, player)
    while size(q) > m - 1:
        for i in range(m):
            first_player = dequeue(q)
            enqueue(q, first_player)
    print(dequeue(q))
    return q

print(set(who_wins(3, ['val', 'hel', 'jam', 'jin', 'tze', 'eli', 'zha', 'lic'])))
print(who_wins(2, ['poo', 'ste', 'sim', 'nic', 'luo', 'ibr', 'sie', 'zhu']))
