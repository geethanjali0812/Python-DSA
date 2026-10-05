# DSA Day 11
# Topic: Strings
# Pattern: Sliding Window + Frequency Counting
# Problem: Longest Repeating Character Replacement

def characterReplacement(s, k):
    left=0
    count={}    #stores frequencies
    max_freq=0
    max_len=0
    for r in range(len(s)):

        # count the current character
        count[s[r]]=count.get(s[r],0)+1

        # to find highest character frequency
        max_freq=max(max_freq,count[s[r]])

        # check how many replacements needed
        while(r-left+1)-max_freq>k:

            # remove left character from the window
            count[s[left]]-=1
            left+=1

        # longest valid window
        max_len=max(max_len,r-left+1)
    return max_len


# Practice
print(characterReplacement("ABAB", 2))     #4
print(characterReplacement("AABABBA", 1))  #4
print(characterReplacement("AAAA", 0))     #4
print(characterReplacement("ABCD", 1))     #2
print(characterReplacement("AABAB", 1))    #4