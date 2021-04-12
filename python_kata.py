from math import sqrt, log
def isPP(n):
    # n = int(n)
    # if n<4: return None
    # sr = round(sqrt(n),6)
    # if sr == round(sr): return [sr, 2]
    # for m in xrange(2, n//2):
    #     k = round(log(n,m), 6)
    #     if k == round(k): return [m, k]
    # return None
    for i in range(2, n+1):
        for j in range(2, n+1):
            if i**j > n:
                break
            elif i**j == n:
                return [i, j]

    return None

print(isPP(4))