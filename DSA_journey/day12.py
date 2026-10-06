# DSA day 12
# Topic : Strings
# Pattern: Hashing
# Problem: Group

def GroupAnagrams(s):
    groups={}      #empty dictionary
    for i in s:
        key=tuple(sorted(i))   #sorted() gives a list, then convert it to tuple
        if key not in groups:
            groups[key]=[]    #empty list
        groups[key].append(i)
    return list(groups.values())

s = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(GroupAnagrams(s))

# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

# Practice 1
print(GroupAnagrams(["eat", "tea", "ate"]))
# [['eat', 'tea', 'ate']]

# Practice 2
print(GroupAnagrams(["bat", "tab", "cat"]))
# [['bat', 'tab'], ['cat']]

# Practice 3
print(GroupAnagrams(["", ""]))
# [['', '']]

# Practice 4
print(GroupAnagrams(["a", "b", "a"]))
# [['a', 'a'], ['b']]

# Practice 5
print(GroupAnagrams(["abc", "bca", "cab", "xyz", "zyx"]))
# [['abc', 'bca', 'cab'], ['xyz', 'zyx']]