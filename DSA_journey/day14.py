# DSA Day 14
# Topic: Strings
# Pattern: Prefix Comparison
# Problem: Longest Common Prefix

def longestCommomPrefix(s):
    if not s:
        return "" 
    prefix=s[0]
    for i in s[1:]:
        while not i.startswith(prefix):
            prefix=prefix[:-1]
            if prefix=="":
                return ""
    return prefix
s=["flower", "flow", "flight"]   #fl
print(longestCommomPrefix(s))

# challenge
print(longestCommomPrefix(["prefix", "prevention", "presentation", "prevent"]))
# pre

# practice
print(longestCommomPrefix(["dog","racecar","car"]))
# ""