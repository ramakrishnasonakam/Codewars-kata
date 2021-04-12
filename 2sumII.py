def twosum(arr, t):
    arr = sorted(arr)
    d = len(arr)
    l=0
    r=d-1
    while l<r:
        if arr[l]+arr[r]==t:
            return (arr[l],arr[r])
        elif arr[l]+arr[r] > t:
            r-=1
        else:
            l+=1
arr = [1,2,3,4,5,6,7,7]
t = 8
print(twosum(arr, t))
