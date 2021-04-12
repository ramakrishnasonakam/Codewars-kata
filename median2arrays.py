def median(arr1, arr2):
    '''
    Will be using middle element approach:
    diving the array from the middle and 
    comparing the sum of both sides till
    the right side is greater

    if len is odd then median will be the
    avg of the middle(th) and +1 element
    else middle(th) element
    '''

    arr1.extend(arr2)
    arr1 = sorted(arr1)
    l = len(arr1)
    m = l//2
    if (l%2==0):
        return ((arr1[m]+arr1[m-1])/2)
    else:
        return(arr1[m])

arr1 = [1,2]
arr2 = [3,4]
print(median(arr1, arr2))    
        