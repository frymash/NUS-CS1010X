def insertion_sort(lst):
    if lst == []:
        return []
    else:
        return insert_x(lst[0], insertion_sort(lst[1:]))

def insert_x(n, lst):
    if lst == []:
        return [n]
    else:
        if n <= lst[0]:
            return [n] + lst
        else:
            return [lst[0]] + insert_x(n, lst[1:])
        
print(insertion_sort([1,5,7,6,2,3,4]))