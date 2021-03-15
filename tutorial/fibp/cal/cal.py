def f(n):
    if n < 2:
        return n
    else:
        return f(n-1) + f(n-2)
    
def fl(n):
    return list(map(f, range(5)))