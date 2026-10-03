# Valid palindrome
# using two pointers
def isPalindrome(s):
    l=0
    r=len(s)-1
    while l<r:
        if not s[l].isalnum():
            l+=1
        elif not s[r].isalnum():
            r-=1
        elif s[l].lower()!=s[r].lower():
            return False
        else:
            l+=1
            r-=1
    return True
s=input()
print(isPalindrome(s))   

# madam : True
# hello : False
# racecar : True
# A man, a plan, a canal: Panama : True
