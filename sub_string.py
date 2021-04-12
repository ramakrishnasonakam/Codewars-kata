def sub_String():
        '''
supposedly the string is [a,b,c,d,a,c,d,d,b]
the function will return "4" (abcd).
A set will contain all the unique characters.
A sliding window to roll through the string to 
get the required output. 
But at the point, the left character in the set will
be removed and the current character will be added to 
the set.
        '''    
    charSet = set()
    l = 0
    for r in range(len(s)):
        while r[s] in charSet:
            s.remove(s[l])
            l+=1
        charSet.add(s[r])
    res = max(res, r-1, l+1)
