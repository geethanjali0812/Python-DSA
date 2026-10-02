#DSA Day 8--Strings
#A string is a sequence of characters
name="Geethanjali"
print(name[0])
print(name[3])
print(name[8])
# G
# t
# a
# Traversing a String
# using characters
s="python"
for i in s:
    print(i)
# p
# y
# t
# h
# o
# n
# using indexes
m="hello"
for i in range(len(m)):
    print(m[i])
# h
# e
# l
# l
# o
# string slicing
n="charan"
print(n[:3])     # cha
print(n[2:])     # aran
print(n[::2])    # caa
print(n[::-1])   # narahc

# Strings are immutable
s="geetha"
s="G"+s[1:]
print(s)   # Geetha

# frequency counting
s = "Geethanjali"
frequency = {}
for ch in s:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1
print(frequency)   
# {'G': 1, 'e': 2, 't': 1, 'h': 1, 'a': 2, 'n': 1, 'j': 1, 'l': 1, 'i': 1}

# Valid anagram
# anagram: same characters with same frequency
def isAnagram(a,b):
    if len(a)!=len(b):   
        return False    # len(a)==len(b)
    freq={}
    for i in a:
        freq[i]=freq.get(i,0)+1
    for i in b:
        if i not in freq:
            return False
        freq[i]-=1
        if freq[i]<0:
            return False
    return True
a="listen"   # {'l':1,'i':1,'s':1,'t':1,'e':1,'n':1}
b="silent"   # {'s':1,'i':1,'l':1,'e':1,'n':1,'t':1}
print(isAnagram(a,b))   # True

# practice 1
s=input()   # apple
def frequency(s):
    freq={}
    for i in s:
        freq[i]=freq.get(i,0)+1
    return freq
print(frequency(s))    # {'a': 1, 'p': 2, 'l': 1, 'e': 1}

# practice 2
# Are these anagrams?  
s = input()  # python
t = input()  # typhon
def isAnagram(s,t):
    if len(s)!=len(t):
        return False
    freq={}
    for i in s:
        freq[i]=freq.get(i,0)+1
    for i in t:
        if i not in freq:
            return False
        freq[i]-=1
        if freq[i]<0:
            return False
    return True
print(isAnagram(s,t))  # True 


