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
    return False

def adjoin_set(x, s):
    if not is_element_of_set(x, s):
        s.append(x)
    return s
    
def intersection_set(s1, s2):
    ''' Homework '''
    return None


