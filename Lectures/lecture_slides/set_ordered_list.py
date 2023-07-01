def make_set():
    return []

def is_empty_set(s):
    return not s

def is_element_of_set(x, s):
    if is_empty_set(s):
        return False
    for e in s:
        if e == x:
            return True
        elif e > x:
            return False
    return False
        

def adjoin_set(x, s):
    for i in range(len(s)):
        if x == s[i]:
            break
        elif x > s[i]:
            s.insert(i + 1, x)           
    
def intersection_set(s1, s2):
    if is_empty_set(s1) or is_empty_set(s2):
        return []

    result = []
    i, j = 0, 0
    while i<len(s1) and j<len(s2):
        if s1[i] == s2[j]:
            result.append(s1[i])
            i = i + 1
            j = j + 1
        elif s1[i] < s2[j]:
            i = i + 1
        else:
            j = j + 1
    return result


