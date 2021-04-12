def three_Sum(nums):
    res = []
    nums = sorted(nums)

    for i, a in enumerate(nums):
        if i > 0 and a == nums[i-1]:
            continue
        l, r = i+1, len(nums)-1
        while l<r:
            Sum = a + nums[l] + nums [r]
            if Sum > 0:
                r-=1
            elif Sum<0:
                l+=1
            else:
                res.append([a, nums[l], nums[r]])
                while nums[l] == nums[l-1] and l<r:
                    l+=1
    return res

nums = [-3,3,4,-3,1,2]
print(three_Sum(nums))