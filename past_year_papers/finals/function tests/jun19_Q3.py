def C(n):
    if n<=1:
        return 0
    else:
        return n + C(n//2) + D(n-1)
def D(n):
    if n<=1:
        return 0
    else:
        return n + D(n//2) + C(n-1)
    
dic = {}
def C_memo(n):
    if n in dic:
        return dic[n]
    elif n <= 1:
        dic[n] = 0
        return 0
    else:
        dic[n] = n + C_memo(n//2) + C_memo(n-1)
        return dic[n]
    
print(f"C(8) = {C(8)}")
print(f"C_memo(8) = {C_memo(8)}")