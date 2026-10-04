# Longest substring without repeating characters
# sliding windoe technique
s=input()
def longSubstring(s):
    l=0
    exist=set()    # set doesn't contain duplicate values
    max_len=0
    for r in range(len(s)):
        while s[r] in exist:    # Duplicate found, so shrink the window
            exist.remove(s[l])
            l+=1
        exist.add(s[r])
        cur_len=r-l+1
        max_len=max(cur_len,max_len)
    return max_len
print(longSubstring(s))

# abcabcbb :3
# bbbbb :1
# pwwkew :3
# abba :2
