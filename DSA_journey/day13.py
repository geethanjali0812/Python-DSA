def longestPalindrome(s):

    # if string has 0 ot 1 character
    if len(s)<2:
        return s
    start=0
    end=0
    def expand(left,right):
        while left>=0 and right<len(s) and s[left]==s[right]:
            left-=1
            right+=1
        return left+1,right-1
    for i in range(len(s)):

        # odd length palindrome
        left1,right1=expand(i,i)

        # even length palindrome
        left2,right2=expand(i,i+1)
        if right1-left1>end-start:
            start=left1
            end=right1
        if right2-left2>end-start:
            start=left2
            end=right2
    return s[start:end+1]
s = "cbbd"
print(longestPalindrome(s))

# pactice
print(longestPalindrome("babad")) #bab
print(longestPalindrome("a")) #a
print(longestPalindrome("ac")) #a
print(longestPalindrome("racecar")) #racecar
print(longestPalindrome("aaaa")) #aaaa

# challenge
print(longestPalindrome("forgeeksskeegfor")) #geeksskeeg
