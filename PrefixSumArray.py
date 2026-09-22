def prefixsum(a):
  ar=[]
  sum=0
  for i in a:
    sum+=i
    ar.append(sum)

  return ar
a=[3,1,4,1,5,9,2,6]
print(prefixsum(a))

def prefixsum(a):
  ar=[0]*len(a)
  ar[0]=a[0]
  for i in range(1,len(a)):
    ar[i]=ar[i-1]+a[i]
  return ar
a=[3,1,4,1,5,9,2,6]
print(prefixsum(a))

def rangesum(a,l,r):
  if l==0:
    return a[r]
  return a[r]-a[l-1]
a=[3,1,4,1,5,9,2,6]
print(rangesum(a,2,5))


def equilibriumsum(a):
  ts=sum(a)
  ls=0
  for i in range(len(a)):
    rs=ts-ls-a[i]
    if ls==rs:
      return i
    ls+=a[i]
  return -1
a=[-7, 1, 5, 2, -4, 3, 0]
print(equilibriumsum(a))


st='abcdabc'
sub='ab'
def check(st,sub,i):
  temp=i
  for k in range(len(sub)):
    if st[i]!=sub[k]:
      return -1
    i+=1
  return temp
for i in range(len(st)):
  j=0
  if sub[j]==st[i]:
    print(check(st,sub,i))
    j+=1

#ANAGRAM
s='hello'
s1='ollhe'
def is_anagram(s,s1):
  if len(s)!=len(s1):
    return False
  a=["" for _ in range(len(s))]
  b=["" for _ in range(len(s1))]
  for i in range(len(s)):
    a[i]=s[i]
  for i in range(len(s1)):
    b[i]=s1[i]
  a.sort()
  b.sort()
  for i in range(len(s)):
    if a[i]!=b[i]:
      return False
  return True
print(is_anagram(s,s1))
