def missingno(n, arr):
    sumtotal = (n+1)*n//2
    total = sum(arr)
    missing = total-sumtotal
    return missing

arr = [1,2,4,5,6]
l = len(arr)
print(missingno(l, arr))