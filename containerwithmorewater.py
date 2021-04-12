def maxContainer(h):
    l,r = 0, len(h)-1
    res=0
    while l<r:
        area = (r-l) * min(h[l], h[r])
        res = max(res, area)
        
        if h[l]<h[r]:
            l+=1
        else:
            r-=1
    return res
h = [1,8,6,2,5,4,8,3,7]
print(maxContainer(h))